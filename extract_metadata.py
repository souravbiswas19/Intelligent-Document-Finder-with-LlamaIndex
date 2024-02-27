def extract_metadata_from_response(response):
    metadata=response.source_nodes[0].node.metadata
    # meta_data="The above answer has been extracted from "
    # if metadata:
    #     meta_data=meta_data+" page " + metadata['page_label'] + " of "+f"{metadata['file name']} file which is uploaded in the Google Drive folder of '"+ metadata['author']+ "' Google Account"
    # else:
    #     meta_data="No metadata found"
    # return meta_data
    meta_data="Sources :\n"
    meta_data=meta_data+"File Name -"+metadata['file name']+"\n"
    # meta_data=meta_data+"Title -"+metadata['document_title']+"\n"
    meta_data=meta_data+"Page number -"+metadata['page_label']+"\n"
    # print(metadata['author'])
    return meta_data