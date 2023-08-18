# xrpl-swap Backend

This backend API is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python 3. Additionally, the backend interacts with the XRP Ledger through the [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/) library, a pure Python implementation of the XRP Ledger.

## Requirements

- [Python 3.11+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Setting Up for Development

1. Ensure Python 3.11 or higher is installed on your system:

   ```bash
   python3 --version
   ```

2. Clone this repository to your local machine.

3. Using the terminal, navigate to the project's root directory.

4. Install the required dependencies using `poetry`:
   ```bash
   poetry install
   ```

## Running the Server Locally

While in the project's root directory, initiate the virtual environment and run the server using `poetry` with the following command:

```bash
poetry run python -m main
```

The server will start in development mode with hot-reloading enabled. You should see an output indicating the server is running on `http://127.0.0.1:8000/`.

For interactive API documentation, open your web browser and navigate to `http://127.0.0.1:8000/docs`. Alternatively, use API clients like Postman to send requests to your application.

## Testing

From the project's root directory, run the tests using:

```bash
poetry run pytest
```

Make sure all tests pass before committing or opening a pull request.

## Deployment

<!-- Add description how to deploy to the server -->

## API Endpoints

The FastAPI server offers several endpoints, including:

1. `api/account`

2. `api/swap`

For a comprehensive list of endpoints and their documentation, please refer to FastAPI's interactive API documentation located at `http://<your-server-url>/docs`.

## Contributing

If you wish to contribute to this project, kindly go through our [CONTRIBUTING.md](CONTRIBUTING.md) guidelines. We value each contribution and request you to adhere to the coding conventions and guidelines for all pull requests and issues.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0). This means you are free to copy and redistribute the material in any medium or format, but you must give appropriate credit, cannot use the material for commercial purposes, and cannot create derivative works based on it.

For more details, please see the [LICENSE.md](LICENSE.md) file or visit the [official license page](https://creativecommons.org/licenses/by-nc-nd/4.0/).
