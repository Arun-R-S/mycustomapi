import asyncio
import json
from aiohttp import web
from mycustomapi import MyCustomAPI  # Your class
from types import SimpleNamespace

async def run_test():
    # Mock the query parameters
    mock_query = {
        "ip": "192.168.0.54",
        "power": "1"
    }

    # Create a mock request object
    request = SimpleNamespace()
    request.query = mock_query

    api = MyCustomAPI()
    response = await api.get(request)

    # Read the body from the response manually
    body = response.body
    body_text = body.decode("utf-8")
    body_json = json.loads(body_text)

    print("Parsed JSON Response:")
    print(body_json)

asyncio.run(run_test())
