Features
========

Features are loaded by passing their names to
:func:`chickennuggets.load.load` along with your bot instance. ::

    import chickennuggets
    from discord.ext import commands

    bot = commands.Bot(command_prefix='!')
    chickennuggets.load(bot, ['help', 'errors'])

API
---

.. automodule:: chickennuggets.load
  :members:
  :undoc-members:
