from store_vector_index import index
query_engine = index.as_query_engine()
response = query_engine.query("What is Natural Language Processing?")
print(response)