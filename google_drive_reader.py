"""This python module implements the access of files from the Google Drive Folder"""
#from config import config
#import os
"""This python module implements the access of files from the Google Drive Folder"""
#from config import config
#import os
from instance_flag import old_file_id, new_file_id
from llama_index.readers.google import GoogleDriveReader
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
# Intialization of the Google Drive Loader
loader = GoogleDriveReader(credentials_path="./credentials.json")

def load_data(folder_id: str):
    """Function to load data from the Google Drive"""
    doc = loader.load_data(folder_id=folder_id)
    return doc

def load_all_data():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("mytoken.json"):
        creds = Credentials.from_authorized_user_file("mytoken.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "driveaccess.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("mytoken.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)
        resource = service.files() 
        # Initialize variables
        all_files = []
        page_token = None # Change this to the desired MIME type

        # Loop until all files are fetched
        while True:
            # Call the Drive v3 API
            query = "mimeType='application/pdf' or mimeType='application/vnd.openxmlformats-officedocument.presentationml.presentation' or mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document' and 'me' in owners and trashed=false"
            results = resource.list(q=query, pageSize=1000, fields="nextPageToken, files(id, name, mimeType)", pageToken=page_token).execute()
            items = results.get("files", [])
            
            # Add fetched files to the list
            all_files.extend(items)

            # Check if there are more files to fetch
            page_token = results.get('nextPageToken')
            if not page_token:
                break
        document_id = []
        for file in all_files:
            document_id.append(file["id"])
        docs = loader.load_data(file_ids=document_id)
        for i in docs:
            old_file_id.add(i.id_)
        return docs
    except HttpError as error:
        raise HttpError

def load_new_data(old_docs, all_docs):
    """Function to separate out the new data from the Google Drive"""
    # Loop to store the unique id_ if each file of the old data
    for i in old_docs:
            old_file_id.add(i.id_)
    # Loop to store the unique id_ if each file of the new data
    for i in all_docs:
        new_file_id.add(i.id_)
    unique_file_id = new_file_id.symmetric_difference(old_file_id)
    # Extraction of the only new documents
    new_docs=[]
    # New documents id_ are being stored in a new list of Llama index documents
    for i in unique_file_id:
        for j in all_docs:
            if i == j.id_:
                new_docs.append(j)
    # To update the old file id with the newly added ones
    for i in unique_file_id:
        old_file_id.add(i)
    return new_docs # new files only returned

# End of File