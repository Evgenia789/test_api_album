
# test_api_album

Catalog of artists and their albums with songs


## Technology stack

- Python3.7
- Django REST Framework
- SQLite
- docker-compose
- git

## How to launch a project by Docker

Clone the repository and go to it on the command line

```bash
    git clone https://github.com/Evgenia789/test_api_album.git
    cd test_api_album
```

Create and activate a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate
```

In the project directory, create a .env file in which you write the following environment variables. (SECRET_KEY need to take from settings.py)

```python
DEBUGE=TRUE
SECRET_KEY=<SECRET_KEY>
```

Run the [docker compose build](https://docs.docker.com/engine/reference/commandline/compose_build/) command

```bash
 docker-compose -f docker-compose.yaml build
```

Run the [docker compose up](https://docs.docker.com/engine/reference/commandline/compose_up/) command

```bash
docker-compose -f docker-compose.yaml up
```

To stop and remove containers, run the [docker compose down](https://docs.docker.com/engine/reference/commandline/compose_down/) command

```bash
docker-compose down
```

---

You can try to access the Django admin at

```bash
http://127.0.0.1:8000/admin
```

You can try to access Swagger at

```bash
127.0.0.1:8000/swagger/
```
