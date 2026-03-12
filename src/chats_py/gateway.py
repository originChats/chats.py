import hashlib
import json

import requests
import websockets


class Gateway:
    def __init__(self, client):
        self.client = client
        self.ws = None
        self.validator_key = ""

    async def connect(self, websocket_url):
        self.ws = await websockets.connect(websocket_url)

        async for message in self.ws:
            data = json.loads(message)

            if data.get("cmd") == "handshake":
                await self.handle_handshake(data)

            await self.client._dispatch(data)

    async def login(self):
        user_info = requests.get(
            "https://api.rotur.dev/get_user"
            f"?username={self.client.user}"
            f"&password={hashlib.md5(self.client.password.encode()).hexdigest()}"
        )
        if user_info.status_code != 200:
            raise Exception("Failed to authenticate with the gateway")

        user_key = user_info.json().get("key")
        validator = requests.get(
            "https://api.rotur.dev/generate_validator"
            f"?key={self.validator_key}&auth={user_key}"
        )
        if validator.status_code != 200:
            raise Exception("Failed to generate validator for gateway authentication")

        payload = {
            "cmd": "auth",
            "validator": validator.json().get("validator"),
        }
        await self.send(payload)

    async def send(self, data):
        if self.ws:
            await self.ws.send(json.dumps(data))

    async def handle_handshake(self, data):
        val = data.get("val", {})

        self.server_info = val.get("server")
        self.limits = val.get("limits")
        self.version = val.get("version")
        self.validator_key = val.get("validator_key")

        await self.login()
