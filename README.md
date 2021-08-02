![Lint](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-lint.yml/badge.svg)
![Build and Test](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-test.yml/badge.svg)
![Upload Package](https://github.com/JeanPinzon/py-easy-rest-mongo-motor-repo/actions/workflows/python-publish.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/py-easy-rest-mongo-motor-repo.svg)](https://badge.fury.io/py/py-easy-rest-mongo-motor-repo)

# py-easy-rest-mongo-motor-repo

Cache lib to use with [py-easy-rest](https://github.com/JeanPinzon/py-easy-rest)


## Getting Started

### How to install

`pip install py-easy-rest py-easy-rest-mongo-motor-repo`


### Integrating with your [py-easy-rest](https://github.com/JeanPinzon/py-easy-rest) app


### Mongo Repository

```python
#main.py
from motor.motor_asyncio import AsyncIOMotorClient

from py_easy_rest.server import App
from py_easy_rest_mongo_motor_repo.mongo_motor_repo import MongoRepo


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

repo = MongoRepo()

pyrApp = App(config, repo=repo)

@pyrApp.app.listener('before_server_start')
def init(app, loop):
    mongo_db_instance = AsyncIOMotorClient("mongodb://localhost:27017/db")
    db = mongo_db_instance.get_default_database()
    collection = db["default"]
    repo.set_db_collection(collection)


pyrApp.app.run(
    host='0.0.0.0',
    port=8000,
    debug=True,
    auto_reload=True,
)
```