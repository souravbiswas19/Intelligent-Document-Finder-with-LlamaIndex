from store_vector_index import index

def generate_answer(prompt):
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    return response