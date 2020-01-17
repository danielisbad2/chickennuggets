# Chicken Nuggets

A utility library for Discord.py.

## Install

```
pip3 install chickennuggets
```

## Features

| Feature  | Description                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------|
| `help`   | An embed-based alternative to the default help command.                                                     |
| `errors` | Responds to all command errors with a helpful message, and forwards unhandled exceptions to the bot author. |

## Loading Features

Features can be loaded by calling `chickennuggets.load` with your Discord
bot instance and a list of keys, corresponding to the feature names in the
table above.

```python3
import chickennuggets
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
chickennuggets.load(bot, ['help', 'errors'])
```
