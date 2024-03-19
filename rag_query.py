"""This python module performs query generation"""
from store_vector_index import load_index
from gemini_llm import load_Gemini
# Error Handling
def generate_answer(prompt):
    """Generates the query as per the prompt given"""
    # Query Engine is being initialized
    index = load_index()
    query_engine = index.as_query_engine(llm=load_Gemini())
    # Response is being generated as per the prompt
    response = query_engine.query(prompt)
    # Response is being returned
    return response