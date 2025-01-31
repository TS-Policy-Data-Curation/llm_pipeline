from utils.db import connect_to_db

import numpy as np
import json

def cosine_similarity(vec1, vec2):
    """
    Compute the cosine similarity between two vectors.
    
    Args:
        vec1 (list or np.array): First vector.
        vec2 (list or np.array): Second vector.
    
    Returns:
        float: Cosine similarity between the two vectors.
    """
    # Ensure that both vec1 and vec2 are numpy arrays for easier mathematical operations
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    # Compute dot product and norms
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    # Return cosine similarity
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0  # To handle division by zero if any vector has zero magnitude
    return dot_product / (norm_vec1 * norm_vec2)

def find_similar_documents(query_vector, top_k=5):
    """Function to find the most similar documents in the SingleStore database.
    
    Args:
        query_vector (list or np.array): Query vector as a list of floats.
        top_k (int): Number of top similar documents to retrieve. Default is 5.
    
    Returns:
        list: A list of dictionaries with document metadata and similarity scores.
    """
    # Convert the numpy array or list to a string or format that matches your database storage
    query_vector_str = ','.join(map(str, query_vector))  # Assuming vectors are stored as comma-separated strings

    # SQL query to find the top K similar documents based on vector similarity
    sql_query = """
        SELECT id, metadata, vector
        FROM documents
        WHERE cosine_similarity(vector, %s) > 0.9
        ORDER BY similarity_score DESC
        LIMIT %s;
    """
    
    # Connect to the database
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)

    try:
        # Execute the query with the query vector and top_k limit
        cursor.execute(sql_query, (query_vector_str, top_k))
        results = cursor.fetchall()

        # Process and return the results
        similar_documents = []
        for result in results:
            metadata = json.loads(result['metadata'])  # Parsing the JSON metadata
            similarity_score = cosine_similarity(query_vector, result['vector'])  # Calculate the similarity score
            similar_documents.append({
                'doc_id': metadata['doc_id'],
                'text_representation': metadata['text_representation'],
                'source_file': metadata['source_file'],
                'similarity_score': similarity_score  # Adding the calculated similarity score
            })

        return similar_documents

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Example usage (not in this file, but in your main script):
# query_vector = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
# similar_docs = find_similar_documents(query_vector)
# print(similar_docs)
