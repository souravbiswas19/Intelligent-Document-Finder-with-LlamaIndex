# Intelligent Document Finder using LlamaIndex and Gemini

![Intelligent Document Finder](/logos/frontend.png)

- ### **Demonstration Video:** [Video Link](https://drive.google.com/drive/folders/1Wq2-ABC6EsmYIvGRnTWptNC2aS4L5Ac1?usp=sharing)

## Contents:
### 1. [Overview](#overview)
### 2. [Objectives](#objectives)
### 3. [Tech stack](#tech-stack)
### 4. [System Workflow](#system-workflow) 
### 5. [Design and Implementation](#design-and-implementation)
### 6. [Project Structure](#project-structure)
### 7. [Installation and Execution](#installation-and-executation) 
### 8. [Google Cloud Credentials for Google Drive Integration with Llama Index](#google-cloud-credentials-for-google-drive-integration-with-llama-index)


## Overview
The Intelligent Document Finder project aims to create a seamless, user-friendly platform 
that allows for the uploading and automatic indexing of various document formats, 
including PDFs, PPTs, Word documents, and other forms of unstructured data. By 
leveraging Llama Index for data indexing and retrieval, the system will enable precise query 
handling through a front-end application, enhancing the user's ability to find specific 
information efficiently.

## Objectives

### A. **Intelligent Document Finder Application**
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

### B. **Add Login and Signup Functionality to Intelligent Document Finder Project**

### 1) Signup and Login (JWT Authentication)
Enhance the existing Intelligent Document Finder project by adding user signup and login 
functionality using FastAPI. 
- Develop API endpoint for user signup, allowing new users to create an account.
- Implement password hashing to securely store user passwords.
- Create API endpoint for user login, verifying user credentials.
- Generate and return JWT tokens upon successful login. 
- Test the API endpoints using tools like Swagger UI or Postman to ensure correct 
behavior.
### 2) User-Defined Search Folder:
- Allow users to add a folder link from their Google Drive.
- Limit search functionality to only the specified folder.
- Implement search functionality restricted to the user's specified Drive folder.
### 3) Bonus Task - OneDrive Integration:
- Extend the functionality of project to support OneDrive.

## Tech stack
![Gemini](/logos/Untitled%20design.png)

#### 1. [Google Gemini](https://gemini.google.com/)
#### 2. [Llama Index](https://www.llamaindex.ai/)
#### 3. [Python](https://www.python.org/)
#### 4. [Huggingface](https://huggingface.co/)
#### 5. [Streamlit](https://docs.streamlit.io/)
#### 6. [FastAPI](https://fastapi.tiangolo.com/)
#### 7. [JSON Webs Tokens](https://jwt.io/)

## System Workflow

![Flowchart](/logos/Retrieved%20Context.png)

## Design and Implementation

1. Interface of the Intelligent Document Finder

![Frontend](/logos/frontend.png)

2. Result of the Intelligent Document Finder

![Result](/logos/result.png)

3. SignUp Endpoint

![Register](/logos/Screenshot%20(39).png)

4. Signup Endpoint Result

![Register](/logos/Screenshot%20(40).png)

5. Login Endpoint

![Register](/logos/Screenshot%20(41).png)

6. Login Endpoint Result

![Register](/logos/Screenshot%20(42).png)

7. JWT Token Authorization

![Auth](/logos/Screenshot%20(43).png)

![Auth](/logos/Screenshot%20(44).png)

8. Providing the Google Drive Link

![Set link](/logos/Screenshot%20(45).png)

9. Output of Setting the Google Drive Link

![Output](/logos/Screenshot%20(46).png)

10. Querying 

![Query](/logos/Screenshot%20(48).png)

11. Output after querying

![Output](/logos/Screenshot%20(49).png)

## Project Structure
The project structure consists of the following files:

### Document Finder Project
- `config.py`: This python file implements the env variables for API coniguration
- `extract_metadata.py`: This python file is for extraction of metadata
- `gemini_llm.py`: This module is responsible for initializing LLM, Embedding and Prompts
- `google_drive_reader.py`: This python module implements the access of files from the Google Drive Folder
- `instance_flag.py`: Store the instances of file id_ of new and old documents for checking which documents are uploaded recently
- `main.py`: This a python file for frontend of the Intelligent Document Finder using LlamaIndex
- `rag_query.py`: This python module performs query generation
- `store_vector_index.py`: This python module performs the function of storing the vectors along with the implementation of TitleExtractor
- `requirements.txt`: 

### Login SignUP JWT Authentication
**The File for the authentication system are present under the Authentication Folder**

- `auth_bearer.py` : Python file to authenticate the token generated after login. 
- `database.py` : Python file to configure the database connection to store user information.
- `models.py` : Python file that contains the database schemas of each table
- `schemas.py` : Python file that contains each schema of every operation like user registration details, user login and password details, and JWT tokens.
- `stream.py` : Python file for frontend implementation using streamlit
- `utils.py` : Python utility function for hashing password, verifying password, and generating access tokens.

## API Endpoints
- SignUp
    - **Method**: `POST`
    - **URL**: `/register`
    - **Parameters**: `user: schemas.UserCreate` for sending the user details and `session: Session = Depends(get_session)` for sending the database session
    - Output: For successful registration of users -  `user created successfully` is returned. Along with it Access Token is generated.  If email id already exists then `Email already registered` is returned.
    - **Description**: Takes up user details and database session as input and stores the details to the database, generates the access token and provides an output if the user is registered.
- Login
    - **Method**: `POST`
    - **URL**: `/login`
    - **Parameters**: `request: schemas.Logindetails` for sending the user login details as email id and password and `db: Session = Depends(get_session)` for connecting to the database session
    - **Output**: For successful login of users -  Login Successful is returned. If email id already exists then exception Incorrect mail id or incorrect password exception is raised
    - **Description**: Takes up user login details and database session as input and stores the details to the database and provides login successful message

- Set Link
    - **Method**: `POST`
    - **URL**: `/setlink`
    - **Parameters**: `link` for accessing the google drive folder along with it proper authentication is required using JWT Tokens
    - **Output**: After data is loaded `Docs successfully loaded and Indexing done successfully`
    - **Description**: Loads the data from the google drive folder and indexes it.

- Get the response from llm
    - **Method**: `POST`
    - **URL**: `/getquery`
    - **Parameters**: `question` for accessing the question and returning the response and the link will be accessed only if  along with it proper authentication is required using JWT Tokens
    - **Output**: The query will be searched and returned in the response.
    - **Description**: Accepts the query, searches the vector database using LLM and then provides the response.

## Installation and Executation
### Clone the Project Repository
Clone the repository or download the project files. Navigate to the project directory by using:
    
```bash
git clone https://github.com/souravbiswas19/Intelligent-Document-Finder-with-LlamaIndex.git
```

Go inside the 'Intelligent-Document-Finder-with-LlamaIndex' directory.
```bash
cd Intelligent-Document-Finder-with-LlamaIndex
```

### Setup Python Virtual Environment
To set up the project environment, follow these steps:

1. Ensure you have Python 3.11.8 installed. This project has been run on `Python 3.11.8`. Download the python 3.11.8 from here: [Python 3.11](https://www.python.org/downloads/release/python-3118/)

Direct download link of Python 3.11.8: [Click to download from here](https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe)

2. Create a virtual environment using `venv`.

    ```bash
    python -m venv <virtual-environment-name>
    ```

3. Actiavte the virtual environment using:
    
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

4.  Install the dependencies listed in requirements.txt using pip:

    ```bash
    pip install -r requirements.txt
    ```

5. Setting up the `.env` file is provided in the `.env.examples` file in the Project directory. Assign your GOOGLE_API_KEY save the `.env.examples` file as `.env` file only. If you don't have a GOOGLE_API_KEY generate one from here [Google API Key Documentation](#google-cloud-integration)

    ```bash
    GOOGLE_API_KEY = "<YOUR GOOGLE API KEY>"
    ```
    
    **How can we get a FOLDER_ID?**

    Open the Google Drive Folder you want, copy the url. The URL should look like this: `https://drive.google.com/drive/folders/<FOLDER_ID>`.
    
    **Make sure to keep the share mode of the folder as `Anyone with the link`.**

6. Setting up the `Authentication/.env` file is provided in the `Authentication/.env.examples` file in the Project directory. 
    ```bash
    ALGORITHM = HS256
    JWT_SECRET_KEY = 
    DATABASE_URL = "postgresql://<USERNAME>:<PASSWORD>@localhost/<DB_NAME>"
    ```
    Generate the `JWT_SECRET_KEY` with the `secrets` library of python for that type in git bash
    
    ```bash 
    python
    >> import secrets
    >> secrets.token_hex(32)
    ```
    This will generate a 32bits secret key. Save the key in the `Authentication/.env` file.

    Keep the `ALGORITHM` as `HS256` only.

    Provide the `username`, `password` and `database name` in the database url.

    Open PGAdmin and create the database with your specfied database name.

7. Create a credentials.json from Google Cloud Console by creating a Service Account as mentioned in [Google Drive Integration](#google-cloud-credentials-for-google-drive-integration-with-llama-index)

8. To run the Intelligent Document Finder system along with Signup and Login functionalities using JWT Authentication, execute the following command in the Git bash/Command Prompt/Powershell by activating the environment as mentioned above:

    ```bash
    uvicorn api:app --reload
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
