![Lint](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-lint.yml/badge.svg)
![Build and Test](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-test.yml/badge.svg)
![Upload Package](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-publish.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/py-easy-rest-mongo-motor-repo.svg)](https://badge.fury.io/py/py-easy-rest-mongo-motor-repo)

# py-easy-rest-mongo-motor-repo

Mongo repo to use with [py-easy-rest](https://github.com/JeanPinzon/py-easy-rest)


## Getting Started

### How to install

`pip install py-easy-rest py-easy-rest-mongo-motor-repo`


### Integrating with your [py-easy-rest](https://github.com/JeanPinzon/py-easy-rest) app


### Mongo Repository

```python
#main.py
from motor.motor_asyncio import AsyncIOMotorClient

from py_easy_rest import PYRSanicAppBuilder
from py_easy_rest.service import PYRService
from py_easy_rest_mongo_motor_repo import PYRMongoRepo


config = {
    "name": "Project Name",
    "schemas": [{
        "name": "Mock",
        "slug": "mock",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
        },
        "required": ["name"],
    }]
}

repo = PYRMongoRepo()

service = PYRService(api_config_mock, repo=repo)
sanic_app = PYRSanicAppBuilder.build(api_config_mock, service)

@sanic_app.listener('before_server_start')
def init(app, loop):
    mongo_db_instance = AsyncIOMotorClient("mongodb://localhost:27017/db")
    db = mongo_db_instance.get_default_database()
    repo.set_db_connection(db)


sanic_app.run(
    host='0.0.0.0',
    port=8000,
    debug=True,
    auto_reload=True,
)
```
