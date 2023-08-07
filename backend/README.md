# Backend Service

Backend service is built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python.

This service also utilizes [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/), a pure Python implementation of the XRP Ledger. xrpl-py allows this backend to interact with the XRP Ledger.

## Requirements

Python 3.10+

## Setting Up for Development

1. Ensure you have Python 3.10+ installed on your system. You can verify this by running `python3 --version` on your command line.

2. Clone the repository onto your local environment.

3. Navigate to the `backend` directory.

4. Install the necessary packages for the project by running:

```bash
pip install -r requirements.txt
```

## Running the Server Locally

Navigate to the `app` directory within `backend` and run the following command:

```bash
uvicorn main:app --reload
```

This command runs the server in development mode, with hot-reloading enabled. You should see output telling you that the server is running and listening for HTTP requests on `http://127.0.0.1:8000/`.

Open up your web browser to this URL to interact with the application via FastAPI's interactive API documentation on `http://127.0.0.1:8000/docs`, or point your API client (like Postman) to this URL to begin sending requests to your application.

## Testing

To run tests, navigate to the `backend` directory and run:

```bash
pytest
```

Ensure any new code is well-tested and all tests pass.

## Deployment

## API Endpoints

Your FastAPI server has the following endpoints:

1. `api/v1/account`

Please refer to the FastAPI interactive API documentation at `http://<your-server-url>/docs`.

## Contributing

Before you contribute, please read through the contributing guidelines. Please adhere to this repository's coding conventions and guidelines for each pull request and issue.

## License
