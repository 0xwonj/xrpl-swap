# xrpl-swap Backend

This backend API is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python 3. Additionally, the backend interacts with the XRP Ledger through the [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/) library, a pure Python implementation of the XRP Ledger.

## Requirements

-   Python 3.11+

## Setting Up for Development

1. Ensure Python 3.11 or higher is installed on your system:

    ```bash
    python3 --version
    ```

2. Clone this repository to your local machine.

3. Using the terminal, navigate to the project's root directory.

4. This project uses `poetry` for dependency management. If you don't have `poetry` installed, you can install it with:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

5. Install the required dependencies using `poetry`:
    ```bash
    poetry install
    ```

## Running the Server Locally

While in the project's root directory, run the server with the following command:

```bash
python -m main
```

The server will start in development mode with hot-reloading enabled. You should see an output indicating the server is running on `http://127.0.0.1:8000/`.

For interactive API documentation, open your web browser and navigate to `http://127.0.0.1:8000/docs`. Alternatively, use API clients like Postman to send requests to your application.

## Testing

From the project's root directory, run the tests using:

```bash
pytest
```

Make sure all tests pass before committing or pushing any new code.

## Deployment

## API Endpoints

The FastAPI server offers several endpoints, including:

1. `api/account`

2. `api/swap`

For a comprehensive list of endpoints and their documentation, please refer to FastAPI's interactive API documentation located at `http://<your-server-url>/docs`.

## Contributing

If you wish to contribute to this project, kindly go through our contributing guidelines. We value each contribution and request you to adhere to the coding conventions and guidelines for all pull requests and issues.

## License
