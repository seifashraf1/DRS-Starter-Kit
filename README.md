# Deploy a DRS Starter Kit

## 1. Set Up Environment
- Install Docker Desktop
- Install Python 3.x

## 2. Install requirements
```
cd DRS_Starter_Kit
```
```
pip3 install -r requirements.txt
```

## 3: Delete any databases and temporary files
```
rm -f resources/drs/db/drs.db tmp/drs_dataset.ndjson
```

## 4. Deploy DRS Starter Kit using docker-compose
```
docker-compose up -d
```
You should now have DRS Starter Kit running on port 5000


## 5. Confirm that the DRS Starter Kit is running on port 5000 
**HTTP METHOD:**
```
GET
```
**REQUEST URL:**
```
http://localhost:5000/ga4gh/drs/v1/service-info
```
**Expected Response Status Code:** 200
**Expected Response Content Type:** JSON

## 6. Populate data into DRS
```
python3 resources/drs/db-scripts/populate-drs.py
```

## 7. Confirm that the data is populated
**HTTP METHOD:**
```
GET
```
**REQUEST URL:**
```
http://localhost:5000/ga4gh/drs/v1/objects/8e18bfb64168994489bc9e7fda0acd4f
```
**Expected Response Status Code:** 200

## NOTE: 
when you are done using the DRS Starter Kit, to bring down the docker containers use the following commands
```
cd DRS_Starter_Kit
```
```
docker-compose down
```
## Running The App:
There are two testing modules I implemented, unit testing, and manual testing: <br>
**Manual Testing:** 
```
./resources/drs/run_tests.py
```
![image](https://user-images.githubusercontent.com/63073172/231483753-3f3588ef-2a2f-40e1-8928-f41dc0ddad94.png)

**Unit Testing:**
```
./resources/drs/test_endpoints.py
```
![image](https://user-images.githubusercontent.com/63073172/231477500-01f856ab-07c1-4096-bb05-9e5a1c876d7f.png)

## Bundling the application for reuse in another environment:
**Cloud Deployment** <br>
If you intend to deploy the application in a cloud environment, such as AWS, Azure, or Google Cloud, you can package it as a container using Docker. Docker provides a containerization solution that allows you to package the application along with its dependencies, configurations, and runtime environment into a single container image. You can then push the container image to a container registry, such as Docker Hub, and deploy it to any cloud environment that supports Docker containers. <br>

To package the application as a Docker container, you would need to create a Dockerfile that specifies the base image, installs the necessary dependencies, copies the application code, and sets up the runtime environment. Here's an example Dockerfile for the given application: <br>

```
# Dockerfile

# Use an appropriate base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set the entry point for the application
CMD ["python", "app.py"]
```
Build the Docker image using the Dockerfile.
```
docker build -t my-app .
```

Push the Docker image to a container registry, such as Docker Hub.
```
docker push my-app
```

**Deployment on Another Desktop Machine or Alternative Operating System** <br>
If you want to package the application for reuse on another desktop machine, you can create a standalone executable using a tool like PyInstaller or cx_Freeze. These tools allow you to bundle the Python code, dependencies, and runtime into a single executable file that can be run on any compatible desktop machine without requiring any additional installations or dependencies. <br>

To package the application as a standalone executable using PyInstaller, for example, you would need to install PyInstaller using pip, and then use the pyinstaller command to create the executable. Here's an example command: <br>

```
pip install pyinstaller
pyinstaller app.py
```
This will create a standalone executable file for the application in the dist directory, which can be copied and run on any compatible desktop machine.
