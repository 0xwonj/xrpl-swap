# xrpl-swap Backend

This backend API is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python 3. Additionally, the backend interacts with the XRP Ledger through the [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/) library, a pure Python implementation of the XRP Ledger.

## Prerequisites

- [Docker](https://www.docker.com/)
- Docker Compose

## Project Structure

This backend solution is categorized into three major components:

1. [**FastAPI**](app) (API Endpoint Exposures)
2. [**ETL**](etl) (Data Extraction, Transformation, and Loading)
3. [**Redis**](database) (In-memory data structure store)

## Development Setup

1. Clone the repository to your local machine.

2. Navigate to the project's root directory using the terminal.

3. Make sure to set up the `.env` file using the provided [`.env-template`](.env-template) before proceeding further.

## Running the Application using Docker

1. To initiate the application, use the following Docker command:

   ```bash
   docker compose up --build -d
   ```

2. Once executed, the application will run on `http://0.0.0.0:8000/`.

3. To shut down the application and its services:

   ```bash
   docker compose down
   ```

## API Endpoints

A complete list of endpoints and their descriptions can be found in the FastAPI's interactive API documentation ([swagger](https://swagger.io/)) at `http://<your-server-url>/docs`.

## Contributing

If you wish to contribute to this project, kindly go through our [CONTRIBUTING.md](CONTRIBUTING.md) guidelines. We value each contribution and request you to adhere to the coding conventions and guidelines for all pull requests and issues.

## License

This project adheres to the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0). You're permitted to copy and distribute the material across various mediums. However, appropriate credit is essential, and commercial usage or derivative works creation isn't allowed.

For a comprehensive understanding, refer to the [LICENSE.md](LICENSE.md) documentation or the [official license page](https://creativecommons.org/licenses/by-nc-nd/4.0/).
