import logging


logger = logging.getLogger(__name__)

# Map feature names to extension import paths
COGS = {
    'errors': 'chickennuggets.errors',
    'help': 'chickennuggets.help',
}


class FeatureNotFoundException(Exception):
    """
    Exception raised when an invalid feature name is given to :func:`load`.
    """

    pass


def load(bot: 'discord.ext.commands.Bot', features: list):
    """
    Load a set of chickennuggets features into your bot.

    Args:
       bot: Bot to load extensions into
       features: List of cog names to load
    """

    for feature in features:
        try:
            # Get the import path of the cog
            path = COGS[feature]
        except KeyError:
            # Cog not found
            raise FeatureNotFoundException(
                f'"{feature}" is not an existing feature or cog'
            )

        # Load the cog
        logger.info('Loading %s (%s)', feature, path)
        bot.load_extension(path)

    logger.info('Load completed')
