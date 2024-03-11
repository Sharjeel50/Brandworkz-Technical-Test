## Weather APP


### Task 1 -

### System requirements -

- Python >= 3.9
- `venv` Package install (`pip install venv`)
- Docker (optional, but recommended)

### Running the application

##### Before starting the application, make sure you add your RAPID_API_KEY in the backend `.env` file! - `/backend/.env` 

The best way to run this application would be to use Docker, using the docker-compose file found at the root of the cloned repository, type `docker-compose up` and this will 
build and start the backend and frontend containers, you will then be able to access the application at `http://localhost:3000/`

The process to build and start the backend and frontend individually is documented below - 

### Backend

To utilise the Weather app API, ensure you have the required dependencies installed and follow these steps:

1. Navigate to backend folder
2. Create a virtual environment using the following command - `python -m venv ./venv`
3. Activate the virtual environment, for MacOS using the command `source venv/bin/activate`, for Windows run `Activate.bat` found under `/venv/Scripts`
4. Install requirements.txt using the following command - `pip install -r requirements.txt`
5. In the terminal, write `uvicorn src.main:app --reload` which will start the FastAPI server
6. Navigate to `http://127.0.0.1:8000/docs/` which is where the endpoints available can be found

### Tests

You can run all unit tests by typing `pytest` in the base directory of the folder, this will test the `cash-flow` endpoint and the `calculate_cash_flow` function

##### Ensure that the virtual environment (venv) is activated after installing the requirements.txt (refer to step 3 under usage). If you attempt to run the test using pytest before activating the virtual environment, you will encounter errors.

### Frontend

Requirements - 
- Node.js and npm

Install and start frontend

1. Navigate to the frontend folder
2. npm install - This will install all dependicies
3. npm run dev - This will start the application, you can then visit the frontend on `http://localhost:3000/`


### Task 2 -

### Weather API Overview - 

An endpoint to receive information about the current weather for a given location, this application is a read heavy system that requires high performance. The diagram below shows the architecture designed to cater for this application.

https://private-user-images.githubusercontent.com/41446219/311890494-71bc4d4c-1627-4b51-893f-adf1b344ee7a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTAxOTg5NzEsIm5iZiI6MTcxMDE5ODY3MSwicGF0aCI6Ii80MTQ0NjIxOS8zMTE4OTA0OTQtNzFiYzRkNGMtMTYyNy00YjUxLTg5M2YtYWRmMWIzNDRlZTdhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAzMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMzExVDIzMTExMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ5MjA3NTQ4OWMxYTI5N2MzMGZlZjAwNDk2ZTc5ZDU4NDMzMWI1ZTkzOThkZWNhMThiNzNkYTRlZWY5MjRlYzAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xtWkG3N4eqyurPv1XWKAFg0lIP_FhQB_m3LgFz6r_Tw

##### Request validation - 

- Check API key present/valid
- Check given lon, lat is correct format/exists on map

##### Responses/Response codes - 

- 200 - Successfully returned weather data
- 401 - Unauthorised
- 422 - Incorrect data passed through required query parameters
- 424 - Dependency error / Internal error to do with hosted DB
- 500 - Internal server error

##### Ideas/remarks on maintaining high performance

API Gateway - 

- Serves as a entry point for the API. It is responsible for handling incoming requests, manages authorisation and routing requests.
- API Gateway is resilient as it is built upon AWS global infrastructure, which is built on AWS regions and availability zones, so scalability and performance are not expected to be problematic.
https://docs.aws.amazon.com/apigateway/latest/developerguide/disaster-recovery-resiliency.html

AWS Lambda 

- The serverless function responsible for processing the request. It contains the business logic for fetching weather data for the specified location. It validates the request parameters, performs authorization using the provided API key, and interacts with the database (Postgres in this case).
- AWS Lambda also provides high performance and scalability, which will be perfect for this API, according to AWS - 
> AWS Lambda provides a serverless compute service that can scale from a single request to hundreds of thousands per second. When designing your application, especially for high load, it helps to understand how Lambda handles scaling and throughput.

https://aws.amazon.com/blogs/compute/understanding-aws-lambda-scaling-and-throughput/

##### Considerations

- Caching - Based on how often the information in the DB is updated, caching would be a big factor to increasing customer satisfaction and decreasing cost as well as response time, `Redis` or `Memcached` can be used for this.

##### Non-functional Requirements - 

- Customer experience/satisfaction - To reduce the number of `500` or bad requests received by the customer, implement retry functionality 
, Check for failed database queries and implement a retry mechanism within the code to ensure a successful 200 response.


- Datadog Logging - Datadog is a cloud-based monitoring and analytics platform that provides real-time insights into the performance and health of applications, infrastructure, and logs.
- Grafana - Grafana is an open-source analytics and monitoring platform that visualizes and explores data, enabling users to create interactive and shareable dashboards for comprehensive insights into various metrics and data sources, this can be used to view application metrics.
