from .command import SlashCommand
from .context import SlashContext

class SlashRegistry:
    def __init__(self, client):
        self.client = client
        self.commands = {}

    def command(self, **kwargs):
        def decorator(func):
            cmd = SlashCommand(callback=func, **kwargs)
            self.commands[cmd.name] = cmd
            return func
        return decorator

    async def register_all(self):
        payload = {
            "cmd": "slash_register",
            "commands": [cmd.to_dict() for cmd in self.commands.values()]
        }
        print('registering commands:', payload)
        await self.client.gateway.send(payload)

    async def handle_call(self, payload):
        name = payload["val"]["command"]
        args = payload["val"]["args"]

        command = self.commands.get(name)
        if not command:
            return

        ctx = SlashContext(
            client=self.client,
            command=command,
            args=args,
            invoker=payload.get("invoker"),
            channel=payload.get("channel")
        )

        await command.callback(ctx)
