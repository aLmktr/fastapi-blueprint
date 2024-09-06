<div align="center">
   <img src="https://github.com/user-attachments/assets/f4311d59-2dce-4542-b1e7-3973db6b9a5c" alt="fastapi-blueprint-logo" />
</div>
<br />
 <p align="center">
    <em>FastAPI template with JWT auth, PostgreSQL, and Docker Compose for rapid API development.</em>
 </p>
 
<br />

## Features

- **FastAPI**: A high-performance web framework for building APIs with Python.
- **SQLAlchemy**: An ORM tool. Following SQLAlchemy's version 2 approach for defining models
- **Alembic**: Manages database migrations.
- **PostgreSQL**: A robust and scalable database system.
- **Docker**: Provides containerization for consistent development and deployment environments.
- **Unit Testing with Pytest**: Ensures code quality and reliability through effective testing.
- **User Authentication with JWT**: Implements secure user authentication and authorization.
- **Modular Structure**: Organizes the project for maintainability and scalability.

<br />

## Project Structure

The project is organized into a modular structure to promote scalability and maintainability.

```bash

📁 .
├── 📁 backend
│  ├── 📁 api
│  │  ├── 📁 auth
│  │  │  └── 📄 auth_routes.py
│  │  ├── 📁 core
│  │  │  ├── 📄 config.py
│  │  │  ├── 📄 database.py
│  │  │  └── 📄 security.py
│  │  └── 📁 user
│  │     ├── 📄 crud.py
│  │     ├── 📄 models.py
│  │     ├── 📄 schemas.py
│  │     └── 📄 user_routes.py
│  ├── ⚙️ alembic.ini
│  ├── 🐳 Dockerfile
│  ├── 📄 main.py
│  ├── 📁 migrations
│  ├── 📦 requirements.txt
│  └── 📁 tests
│     ├── 📄 conftest.py
│     ├── 📁 user
│     │  ├── 📄 test_crud.py
│     │  └── 📄 test_routes.py
│     └── 📁 utils
├── 🐳 compose.yaml
└── 📑 README.md

```


<br />


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aLmktr/fastapi-blueprint.git
   ```

2. **Step into the project:**

   ```bash
   cd fastapi-blueprint 
   ```

3. **Update the `.env.test` file by setting the DB_PASS and SECRET_KEY (using hashes is recommended). Then, rename the file to `.env`**


4. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

5. **That's ! now you can find your API docs here [localhost:8000/docs](http://0.0.0.0:8000/docs)**

<br />

## Usage

- **Run the application:**

  ```bash
  docker-compose up
  ```

- **Access the API documentation:**
  Open your browser and navigate to `http://localhost:8000/docs` for the Swagger UI or `http://localhost:8000/redoc` for ReDoc.

<br />

## Contributing

If you have suggestions or improvements, please open an issue or submit a pull request. Contributions are welcome!

<br />

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
