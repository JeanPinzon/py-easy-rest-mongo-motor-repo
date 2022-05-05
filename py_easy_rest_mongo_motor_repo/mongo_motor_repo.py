import json

from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


json_dumps = JSONEncoder().encode


class MongoRepo():

    def __init__(self):
        self.connection = None

    def set_db_connection(self, connection):
        self.connection = connection

    async def get(self, slug, id):
        document = await self.connection[slug].find_one({'_id': ObjectId(id)})
        return json.loads(json_dumps(document))

    async def list(self, slug, page, size):
        page = page or 0
        size = size or 30

        cursor = self.connection[slug].find().skip(page * size).limit(size)

        result = await cursor.to_list(length=size)

        return {
            "result": json.loads(json_dumps(result)),
            "page": page,
            "size": size,
        }

    async def create(self, slug, data, id=None):
        if id is not None:
            data['_id'] = ObjectId(id)

        result = await self.connection[slug].insert_one(data)

        return str(result.inserted_id)

    async def replace(self, slug, id, data):
        await self.connection[slug].replace_one({'_id': ObjectId(id)}, data)

    async def delete(self, slug, id):
        await self.connection[slug].delete_one({'_id': ObjectId(id)})
