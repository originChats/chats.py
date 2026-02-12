import asyncio
from gateway import Gateway
from slash.registry import SlashRegistry

class Client:
    def __init__(self, user=None, password=None):
        self.user = user
        self.password = password

        self.gateway = Gateway(self)
        self.slash = SlashRegistry(self)

        self._events = {}

    def event(self, coro):
        self._events[coro.__name__] = coro
        return coro

    def slash_command(self, **kwargs):
        return self.slash.command(**kwargs)

    async def _dispatch(self, payload):
        cmd = payload.get("cmd")

        if cmd == "ready":
            await self.on_ready(payload)
        
        if cmd == "slash_call":
            await self.slash.handle_call(payload)

        elif cmd in self._events:
            await self._events[cmd](payload)
            
        print(payload)

    async def on_ready(self, payload):
        await self.slash.register_all()

        if "on_ready" in self._events:
            await self._events["on_ready"]()

    async def start(self, websocket_url):
        await self.gateway.connect(websocket_url)

    def run(self, websocket_url):
        asyncio.run(self.start(websocket_url))
