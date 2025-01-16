from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from threading import Thread, Event
import os
from dotenv import load_dotenv
from sycamore.llms.openai import OpenAIModels, OpenAI
from sycamore.data import Element, Document
from utils.embeddings import embed_docs
from utils.singlestore import write_to_singlestore
from utils.inference import create_qa_chain, query_vector_store
from utils.data_loading import load_docs
from utils.transform_docs import tableglom
from sycamore.transforms.partition import ArynPartitioner

import logging

load_dotenv()

app = Flask(__name__, static_folder="frontend/build")
CORS(app, origins=["http://localhost:3000"])

# Declare variables within the function to avoid global usage
cursor = None
connection = None
qa = None
stop_event = Event()

def initialize_resources():
    global cursor, connection, qa

    try:
        # Load docs
        docs = load_docs("s3://current-events-supply-chain")

        # Partitioning
        partitioned_doc = docs.partition(ArynPartitioner(extract_table_structure=True, extract_images=True, use_ocr=True))

        # Transforming
        doc_transformed = partitioned_doc.map(tableglom)

        # Embedding
        embedded_docs = embed_docs(doc_transformed)

        # Write to SingleStore
        cursor, connection = write_to_singlestore(embedded_docs)

        # Inference
        qa = create_qa_chain(cursor, connection)

        logging.info("Resources initialized successfully.")

        # Sample query to test setup
        # query = "What are likely outcomes to the US supply chain after new tariff policies?"
        # result, qa_response = query_vector_store(query, qa)
        # print(result)
        # print(qa_response)

        return qa  # Return QA chain for future use
    except Exception as e:
        print(f"Error initializing resources: {e}")
        return None

@app.route("/query", methods=["POST"])
def query():
    """Endpoint to query the vector store."""
    global qa

    # Check if QA chain is initialized
    if not qa:
        return jsonify({"error": "QA chain not initialized, please try again later."}), 500

    # Log the incoming request
    app.logger.debug(f"Received request: {request.json}")

    # Ensure the request contains JSON
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400

    query_text = request.json.get("query")
    if not query_text:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        # Replace with your actual query logic
        qa_response = query_vector_store(query_text, qa)
        return jsonify({"qa_response": qa_response})
    except Exception as e:
        app.logger.error(f"Error during query: {str(e)}")
        return jsonify({"error": f"Error during query: {str(e)}"}), 500


def run_background_task():
    """Background task to continually initialize resources."""
    while not stop_event.is_set():
        logging.info("Initializing resources...")
        initialize_resources()
        stop_event.wait(3600)  # Wait for 1 hour before reinitializing resources


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})

@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, "index.html")

# Serve static assets (e.g., JS, CSS)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    background_thread = Thread(target=run_background_task, daemon=True)
    background_thread.start()

    app.run(host="0.0.0.0", port=5000)
