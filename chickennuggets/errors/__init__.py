import logging

import discord

from chickennuggets.errors.messages import COMMAND_ERROR_MESSAGES
from chickennuggets.errors.unhandled import process_unknown_error
from chickennuggets.footer import set_footer


WARNING_COLOR = discord.Color.from_rgb(255, 255, 0)

logger = logging.getLogger(__name__)


async def send_error_message(ctx, message):
    """Send the given error message in an embed and return the sent message."""

    embed = discord.Embed(
        color=WARNING_COLOR,
        **message # Unpack message as kwargs
    )
    set_footer(embed, ctx.bot.user)
    return await ctx.send(embed=embed)

async def on_command_error(ctx, error):
    """
    Handle command errors.

    Will send a relevant error message if one is found, otherwise will forward
    the exception to the bot owner.
    """

    logger.info('Processing command error')

    # Check if this is a known error
    for known_error, message in zip(
        COMMAND_ERROR_MESSAGES.keys(),
        COMMAND_ERROR_MESSAGES.values()):

        if isinstance(error, known_error):
            # We found a compatible error message
            logger.info('Matched %s', known_error)
            # Send it to the user
            await send_error_message(ctx, message)
            return

    # It is not
    await process_unknown_error(ctx, error)


def setup(bot):
    bot.add_listener(on_command_error)
