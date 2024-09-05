<div align="center">
   <img src="https://github.com/user-attachments/assets/f4311d59-2dce-4542-b1e7-3973db6b9a5c" alt="fastapi-blueprint-logo" />
</div>

<br />

## Features

- **`FastAPI`**: High-performance web framework for building APIs with Python.
- **`SQLAlchemy`**: ORM tool following version 2 conventions for efficient database operations.
- **`Alembic`**: For handling database migrations.
- **`PostgreSQL`**: Robust and scalable database system.
- **`Docker`**: Containerization for consistent development and deployment environments.
- **`Unit Testing with Pytest`**: Ensures code quality and reliability.
- **`User Authentication with JWT`**: Secure user authentication and authorization.
- **`Modular Structure`**: Organized project structure for maintainability and scalability.

<br />

## Project Structure

The project is organized into a modular structure to promote scalability and maintainability. Below is an overview of the directory structure:

```bash
.
├── app
│   ├── api
│   │   ├── auth.py
│   │   └── user.py
│   ├── core
│   │   ├── config.py
│   │   └── setup.py
│   ├── db
│   │   ├── base.py
│   │   └── session.py
│   ├── models
│   │   └── user.py
│   ├── schemas
│   │   ├── auth.py
│   │   └── user.py
│   ├── services
│   │   ├── auth.py
│   │   └── user.py
│   └── main.py
├── alembic
│   ├── versions
│   └── env.py
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_user.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

```

<br />

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-stack.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd fastapi-stack
   ```

3. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

4. **Apply database migrations:**
   ```bash
   docker-compose exec web alembic upgrade head
   ```

## Usage

- **Run the application:**

  ```bash
  docker-compose up
  ```

- **Access the API documentation:**
  Open your browser and navigate to `http://localhost:8000/docs` for the Swagger UI or `http://localhost:8000/redoc` for ReDoc.

## Running Tests

To run the unit tests, use the following command:

```bash
docker-compose exec web pytest
```

## Configuration

Configuration settings are managed via environment variables. You can customize the configuration by editing the `.env` file.

## Contributing

If you have suggestions or improvements, please open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
