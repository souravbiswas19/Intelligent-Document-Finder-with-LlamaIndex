"""This python file is for extraction of metadata"""
def extract_metadata_from_response(response):
    """Extract metadata from response"""
    try:
        metadata = response.source_nodes[0].node.metadata
        return metadata  # metadata is being returned to main.py for displaying in the frontend
    except (AttributeError, IndexError) as e:
        # If response or its attributes are not as expected, handle the exception
        print(f"Error occurred while extracting metadata: {e}")
        return None  # Return None indicating failure
