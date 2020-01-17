import logging


logger = logging.getLogger(__name__)

# Map feature names to extension import paths
COGS = {
    'errors': 'chickennuggets.errors',
    'help': 'chickennuggets.help',
}


class FeatureNotFoundException(Exception):
    pass


def load(bot, features):
    """
    Load the listed features into the bot.

    :param bot: Bot to load into
    :param cogs: List of cogs/features to load
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
