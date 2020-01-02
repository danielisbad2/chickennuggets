# Chicken Nuggets

A utility library for Discord.py.

## Install

```
pip3 install chickennuggets
```

## Features

### Help Command

An embed-based improvement to the default discord.py help command, showing all
the same information.

```python3
bot.load_extension('chickennuggets.help')
```

### Error Handler

Handles user-input-related command errors as well as forwarding unexpected
exceptions to the bot author in a DM.

```python3
bot.load_extension('chickennuggets.errors')
```
