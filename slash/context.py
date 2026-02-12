class SlashContext:
    def __init__(self, client, command, args, invoker, channel):
        self.client = client
        self.command = command
        self.args = args
        self.invoker = invoker
        self.channel = channel

    async def respond(self, content, ephemeral=None):
        payload = {
            "cmd": "slash_response",
            "response": content,
            "invoker": self.invoker,
            "channel": self.channel,
            "ephemeral": ephemeral if ephemeral is not None else self.command.ephemeral
        }

        await self.client.gateway.send(payload)
