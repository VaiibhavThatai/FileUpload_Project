# File Upload and Display Metadata
This project aims to provide a user-friendly interface to upload files and retrieve detailed metadata information about those files.

![image](https://github.com/VaiibhavThatai/FileUpload_Project/assets/85902487/aed62fc5-a22f-4481-a968-87c0488436db)


### Installation and Setup

1. Clone the repository `git clone https://github.com/VaiibhavThatai/FileUpload_Project.git`
2. Download Docker Desktop for your operating system from the official website: [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)


### Build Docker Image
To run Flask application using Docker, run the following commands
1. Open terminal/command prompt/ Git Bash.
2. Navigate to your project directory where the Dockerfile is located.
```python
cd /path/to/your/project
```
3. Give execute permissions to the script using the following command:
```python
chmod +x run_container.sh
```
4. Run the bash script:
```python
./run_container.sh
```


### Accessing the Application
Once the Docker container is up and running, we can access the Flask application in a web browser.
1. Open preferred web browser.
2. Enter the following URL: `http://localhost:5000`


### Cleaning Up
To stop the running Docker container and remove the image, you can use the following steps:

1. In the terminal where the container is running, press `Ctrl+C` to stop the container.
2. Run the following command to remove the Docker image:
```python
docker image rm fileupload-app
```


### Note
If you encounter any issues during the installation or running of the Docker container, refer to the official Docker documentation or the error messages for troubleshooting assistance.


### API Definition
1. GET:
    1. Description: Retrieve information about the uploaded files.
    2. Response:
        1. Status Code: 200
        2. Content: List of uploaded files with their metadata.

2. POST:
    1. Description: Upload one or multiple files to the server.
    2. Request:
        1. Method: POST
        2. Body: Form data with the files to be uploaded.
    3. Response:
        1. Status Code: 201 (Success) or 500 (Error).
        2. Content: JSON indicating success or error message.


### GET vs POST

1. GET Requests
    1. Purpose: Used to retrieve information from the server.
    2. Data: Data is sent as part of the URL query parameters.
    3. Caching: Responses can be cached by browsers.
    4. Security: Data is visible in the URL (not suitable for sensitive information).
    5. Idempotent: Repeated identical requests will produce the same response (no side effects).

2. POST Requests
    1. Purpose: Used to retrieve information from the server.
    2. Data: Data is sent as part of the URL query parameters.
    3. Caching: Responses can be cached by browsers.
    4. Security: Data is visible in the URL (not suitable for sensitive information).
    5. Idempotent: Repeated identical requests will produce the same response (no side effects).


#### Project Deployed Link: http://vaiibhav.codes/ 
