"""This python module performs query generation"""
from store_vector_index import store_index

def generate_answer(prompt):
    """Generates the query as per the prompt given"""
    # Query Engine is being initialized
    index = store_index()
    query_engine = index.as_query_engine()
    # Response is being generated as per the prompt
    response = query_engine.query(prompt)
    # Response is being returned
    return response