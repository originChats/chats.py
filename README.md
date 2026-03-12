# chats.py

A Python wrapper for writing bots for originchats.mistium.com.

## Install

For local development:

```bash
python -m pip install -e .
```

Published/install name:

```bash
pip install chats.py
```

## Usage

1. Copy `.env.example` to `.env`.
2. Fill in the required bot credentials.
3. Run one of the examples:

```bash
python examples/addBot.py
```

Example imports use the package directly:

```python
from chats_py import Client, Option
```
