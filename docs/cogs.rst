Cogs
====

Cogs can be installed by simply loading them as an extension. ::

  bot.load_extension('chickennuggets.help')

A helper function is also provided to load many cogs at once:

.. autofunction:: chickennuggets.load.load

Available Cogs
--------------

==========  ===========
Feature     Description
==========  ===========
`help`      An embed-based alternative to the default help command.
`errors`    Responds to all command errors with a helpful message, and
            forwards unhandled exceptions to the bot author.
==========  ===========
