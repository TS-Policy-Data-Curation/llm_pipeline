# from sqlalchemy import create_engine, text
from utils.db import connect_to_db
import logging
import json
from urllib.parse import quote  # For URL-encoding


def write_to_singlestore(embedded_docs) -> None:    
# Create connection string
    # connection_string = f"mysql://{os.environ['SINGLESTORE_USER']}:{os.environ['SINGLESTORE_PASSWORD']}@{os.environ['SINGLESTORE_HOST']}:{os.environ['SINGLESTORE_PORT']}/{os.environ['SINGLESTORE_DATABASE']}"
    # engine = create_engine(connection_string)
    
    connection = connect_to_db()
    cursor = connection.cursor()


    # Drop existing table if it exists
    cursor.execute("DROP TABLE IF EXISTS document_embeddings")
    
    # Create table with a VECTOR column for embeddings
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS document_embeddings (
            id VARCHAR(255) PRIMARY KEY,
            text_representation TEXT,
            metadata JSON,
            embedding VECTOR(384)  -- Adjust dimension based on your embedding model
        )
    """)
    connection.commit()

    # Prepare records for insertion
    records = []
    for d in embedded_docs.take_all():
        if 'embedding' in d:
            records.append({
                'id': d.doc_id,
                'text_representation': d.text_representation,
                'source': d.get('source', 'unknown'),
                'file_path': d.get('path', 'unknown'),
                'embedding': d['embedding']  # Ensure this is a list of floats
            })

    # Insert records in batches
    batch_size = 10
    for i in range(0, len(records), batch_size):
        batch = records[i:i + batch_size]
        values = []
        for record in batch:
            # Ensure the embedding is a valid JSON array of numbers
            embedding_json = json.dumps(record['embedding'])  # Convert list to JSON string
            # Construct metadata as a JSON string
            metadata_json = json.dumps({
                "source": record['source'],
                "file_path": record['file_path']
            })
            values.append((
                record['id'],
                record['text_representation'],
                metadata_json,
                embedding_json  # Pass the JSON string directly
            ))

        # Construct the INSERT query with parameterized values
        insert_query = """
            INSERT INTO document_embeddings (id, text_representation, metadata, embedding)
            VALUES (%s, %s, %s, JSON_ARRAY_PACK(%s))
        """
        # Execute the query for each batch
        cursor.executemany(insert_query, values)
        connection.commit()
    
    return cursor, connection
