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
│  ├── 📦 pyproject.toml
│  ├── 🔒 uv.lock
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

5. **That's it! now you can find your API docs here [localhost:8000/docs](http://0.0.0.0:8000/docs)**

### Local development (without Docker)

Dependencies are managed with [uv](https://docs.astral.sh/uv/). From the `backend` folder:

```bash
uv sync                      # install runtime + dev dependencies into .venv
uv run pytest -n 6 --cov=.   # run the tests
uv run fastapi dev main.py   # run the app (needs the database running)
```

Add a dependency with `uv add <package>` (or `uv add --dev <package>` for dev tools); this updates `pyproject.toml` and `uv.lock`, which should both be committed.

<br />

### Note
- For security reasons, we have not included any method to create a superuser via the API. To create the first superuser, please follow these steps:
1. Create a normal user using the `create/` API endpoint.
2. Access the database using Docker by running:
```bash
docker exec -it fastapi_blueprint_db psql -U root -d fastapi_blueprint_db
```
3. Run the following SQL command to update the user role:
```sql
UPDATE users SET role='ADMIN' WHERE username='your_username_here';
```
4. Exit the database by running `\q`.
- Once these steps are completed, you are ready to proceed with managing your application.


<br />

## Extending the App
Say, for example, you want to use this template for a shop and add functionality for managing items. You can do this by following these steps:

1. **Create a new folder for the items functionality inside api folder `api/items` organize the folder as follow:**
```bash

└── 📁 items
     ├── 📄 __init__.py 
     ├── 📄 crud.py           
     ├── 📄 models.py         
     ├── 📄 schemas.py        
     └── 📄 item_routes.py  

```

2. **Write your database models:**
In the `models.py` file within the `items` folder, define your database models for the items functionality.

3. **Add model imports to Alembic for migrations:**
After writing your models, open the `migrations/env.py` file and add the following line under the user model import to ensure Alembic recognizes your items models:
```python

"""
Import all models here to ensure they are included in the migration
"""
from api.user import models  # noqa
from api.items import models # noqa  <-------- this line 

target_metadata = Base.metadata

```

4. **Run the migration:**
Make sure your container is running, then apply the migrations by running:
```bash
alembic revision --autogenerate -m "Add items models"
alembic upgrade head 
```

5. **You're ready to go!**
Now you can start working on your new items functionality or any other feature for your app!


<br />

## Contributing

If you have suggestions or improvements, please open an issue or submit a pull request. Contributions are welcome!

<br />

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
