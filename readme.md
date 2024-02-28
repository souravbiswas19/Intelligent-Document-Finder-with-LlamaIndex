# Intelligent Document Finder using LlamaIndex and Gemini

![Intelligent Document Finder](/logos/frontend.png)

## Contents:
### 1. [Overview](#overview)
### 2. [Objectives](#objectives)
### 3. [Tech stack](#tech-stack)
### 4. [Design and Implementation](#design-and-implementation)
### 5. [Project Structure](#project-structure)
### 6. [Installation and Execution](#installation-and-executation) 
### 7. [Google Cloud Credentials for Google Drive Integration with Llama Index](#google-cloud-credentials-for-google-drive-integration-with-llama-index)


## Overview
The Intelligent Document Finder project aims to create a seamless, user-friendly platform 
that allows for the uploading and automatic indexing of various document formats, 
including PDFs, PPTs, Word documents, and other forms of unstructured data. By 
leveraging Llama Index for data indexing and retrieval, the system will enable precise query 
handling through a front-end application, enhancing the user's ability to find specific 
information efficiently.

## Objectives
### 1. User Data Upload:
- Enable users to upload documents of various formats (PDF, PPT, Word, etc.) to a designated Google Drive folder.
- Support for multiple file formats allows for a broad range of document types to be indexed and searched.

### 2. Automated Data Storage and Indexing:
- Automate the process of transferring uploaded documents from Google Drive to a server environment where they can be processed and indexed.
- Use Llama Index to create a searchable database of the uploaded documents, incorporating detailed metadata for each file, such as titles, paragraph numbers, page numbers, etc.

### 3. Development of a Query Interface:
- Develop a Streamlit application or a similar frontend-based system that interfaces with the indexed data.
- Allow users to perform searches with the indexed data, returning relevant document 
snippets along with comprehensive metadata.

## Tech stack
![Gemini](/logos/techstack.png)

#### 1. [Google Gemini](https://gemini.google.com/)
#### 2. [Llama Index](https://www.llamaindex.ai/)
#### 3. [Python](https://www.python.org/)
#### 4. [Huggingface](https://huggingface.co/)
#### 5. [Streamlit](https://docs.streamlit.io/)

## Design and Implementation

1. Interface of the Intelligent Document Finder

![Frontend](/logos/frontend.png)

2. Result of the Intelligent Document Finder

![Result](/logos/result.png)

## Project Structure
The project structure consists of the following files:

- `config.py`: This python file implements the env variables for API coniguration
- `extract_metadata.py`: This python file is for extraction of metadata
- `gemini_llm.py`: This module is responsible for initializing LLM, Embedding and Prompts
- `google_drive_reader.py`: This python module implements the access of files from the Google Drive Folder
- `main.py`: This a python file for frontend of the Intelligent Document Finder using LlamaIndex
- `rag_query.py`: This python module performs query generation
- `store_vector_index.py`: This python module performs the function of storing the vectors along with the implementation of TitleExtractor
- `requirements.txt`: 


## Installation and Executation
### Clone the Project Repository
Clone the repository or download the project files. Navigate to the project directory by using:
    
```bash
git clone https://github.com/souravbiswas19/Intelligent-Document-Finder-with-LlamaIndex.git
```

### Setup Python Virtual Environment
To set up the project environment, follow these steps:

1. Ensure you have Python 3.11.8 installed. This project has been run on `Python 3.11.8`. Download the python 

2. Create a virtual environment using `venv`.

    ```bash
    python -m venv <virtual-environment-name>
    ```

3. Update the pip.

    ```bash
    python.exe -m pip install --upgrade pip
    ```

4. Actiavte the virtual environment using:
    
    A. **Git Bash** - Navigate to the folder containing the virtual environment in Git Bash and run the command.
    ```bash
    source ./<venv>/Scripts/activate
    ``` 
    
    B. **Command-prompt** - Navigate to the folder containing the virtual environment in Command-Prompt and run the command.
    ```bash
    <venv>\Scripts\activate.bat
    ``` 
        
    C. **Powershell** - Navigate to the folder containing the virtual environment in Powershell and run the command.
    ```bash
    <venv>\Scripts\activate.psl
    ```

5.  Install the dependencies listed in requirements.txt using pip:

    ```bash
    pip install -r requirements.txt
    ```

6. Setting up the `.env` file is provided in the `.env.examples` file in the Project directory. Assign the `FOLDER_ID` of your respective Google Drive Folder. Assign your GOOGLE_API_KEY, HF_TOKEN, and OPENAIR_API_KEY as per the requirement of services used, and save the `.env.examples` file as `.env` file only. If you don't have a GOOGLE_API_KEY generate one from here [Google API Key Documentation] (#google-cloud-integration)

    ```bash
    GOOGLE_API_KEY = "<YOUR GOOGLE API KEY>"
    OPENAI_API_KEY = "<YOUR OPENAI KEY>"
    HF_TOKEN = "<YOUR HUGGING FACE TOKEN>"
    FOLDER_ID = "<YOUR FOLDER ID>"
    ```
    
    **How can we get a FOLDER_ID?**

    Open the Google Drive Folder you want, copy the url. The URL should look like this: `https://drive.google.com/drive/folders/<FOLDER_ID>`.
    The `FOLDER_ID` shall be string with a combination of alphanumeric characters. Copy the string and paste the `FOLDER_ID` in the `.env` file

7. Create a credentials.json from Google Cloud Console by creating a Service Account as mentioned in [Google Drive Integration](#google-cloud-credentials-for-google-drive-integration-with-llama-index)

8. To run the Intelligent Document Finder system, execute the following command in the Git bash/Command Prompt/Powershell by activating the environment as mentioned above:

    ```bash
    streamlit run main.py
    ```


## Google Cloud Credentials for Google Drive Integration with Llama Index
1. For fetching the files from Goodle Drive folder, we need to first create a Project on [Google Cloud Console](https://console.cloud.google.com/).

![Google Cloud Console](/logos/Screenshot%20(15).png)

2. Go to the `Navigation Menu` on the top left corner and choose `API and Services`.

![Google Cloud Console Navigation Menu](/logos/Screenshot%20(16).png)

3. Click on `+Enable APIs and Services`

![API and Services](/logos/Screenshot%20(17).png)

4. Search for the `Google Drive API`

![Google Drive API](/logos/Screenshot%20(18).png)

5. Click on the first `Google Drive API` Service

![Google Drive API](/logos/Screenshot%20(19).png)

6. If you haven't enabled the `Google Drive API` service it will be showing `Enable` button. In my case it is showing `Manage` button as I have already enabled it. Click on `Enable` button and navigate to `API and Services` menu again from the `Navigation Menu`.

![Google Drive API Enable](/logos/Screenshot%20(20).png)

7. After navigating to `API and Services`, click on `Credentials` from the menu.

![Google Credentials](/logos/Screenshot%20(21).png)

8. In the Credentials Dashboard, click on `+ CREATE CREDENTIALS`

![Google Credentials](/logos/Screenshot%20(23).png)

9. From the dropdown menu, click on `Service Account`.

![Service Account](/logos/Screenshot%20(24).png)

10. Create a Service Account by providing the necessary details.

![Create Service Account](/logos/Screenshot%20(25).png)

11. Go to the Credentials Dashboard and in the Service Account Section go to the edit button.

![Edit Service Account](/logos/Screenshot%20(27).png)

12. The Service Account details are displayed here, now you need to create a key and a json file will be downloaded.

![Create Service Account](/logos/Screenshot%20(28).png)

13. Go to Key menu

![Create Key](/logos/Screenshot%20(29).png)

14. Click on Add Key

![Create Key](/logos/Screenshot%20(34).png)

15. Create new Key

![Create Key](/logos/Screenshot%20(30).png)

16. Create the key, download the JSON file and rename the JSON file as `credentials.json`. Put the `credentials.json` file inside the project directory.

![JSON File](/logos/Screenshot%20(31).png)
