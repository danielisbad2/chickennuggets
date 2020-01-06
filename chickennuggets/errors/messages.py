from discord.ext import commands


COMMAND_ERROR_MESSAGES = {
    commands.CommandNotFound: {
        'title': 'Command Not Found',
        'description': 'That command doesn\'t exist'
    },
    commands.DisabledCommand: {
        'title': 'Command Disabled',
        'description': 'That command is disabled'
    },
    commands.CommandOnCooldown: {
        'title': 'Command on Cooldown',
        'description': 'That command is on cooldown, please wait'
    },
    commands.NotOwner: {
        'title': 'Not Owner',
        'description': 'You\'re not the boss of me!'
    },
    commands.PrivateMessageOnly: {
        'title': 'Wrong Context',
        'description': 'This command can only be used in private messages'
    },
    commands.NoPrivateMessage: {
        'title': 'Wrong Context',
        'description': 'This command can only be used on servers'
    },
    commands.MissingPermissions: {
        'title': 'Missing Permissions',
        'description': 'You don\'t have the permissions required to run this command'
    },
    commands.BotMissingPermissions: {
        'title': 'Bot Missing Permissions',
        'description': 'Sorry, I don\'t have the necessary permissions to do that'
    },
    commands.MissingRole: {
        'title': 'Missing Role',
        'description': 'You don\'t have a role required to run that'
    },
    commands.MissingAnyRole: {
        'title': 'Missing Role',
        'description': 'You don\'t have a role required to run that'
    },
    commands.BotMissingRole: {
        'title': 'Bot Missing Role',
        'description': 'I don\'t have a role required to run that'
    },
    commands.BotMissingAnyRole: {
        'title': 'Bot Missing Role',
        'description': 'I don\'t have a role required to run that'
    },
    commands.NSFWChannelRequired: {
        'title': 'NSFW Required',
        'description': 'That can only be used in an NSFW channel'
    },
    commands.CheckFailure: {
        'title': 'Check Failure',
        'description': 'You cannot use this command'
    },
    commands.MissingRequiredArgument: {
        'title': 'Missing Required Argument',
        'description': 'You need to spcify all the required paramenter for this command to function'
    },
    commands.TooManyArguments: {
        'title': 'Too Many Arguments',
        'description': 'You gave too much information to this command'
    },
    commands.BadArgument: {
        'title': 'Bad Argument',
        'description': 'One or more arguments were passed incorrectly'
    },
    commands.BadUnionArgument: {
        'title': 'Bad Union Argument',
        'description': 'One or more arguments were passed incorrectly'
    },
    commands.UnexpectedQuoteError: {
        'title': 'Argument Parsing Error',
        'description': 'Unexpected quote'
    },
    commands.InvalidEndOfQuotedStringError: {
        'title': 'Argument Parsing Error',
        'description': 'Expecting a space after the end of a string'
    },
    commands.ExpectedClosingQuoteError: {
        'title': 'Argument Parsing Error',
        'description': 'Expected a closing quote'
    },
    commands.ArgumentParsingError: {
        'title': 'Argument Parsing Error',
        'description': 'You have formatted this command\'s parameters incorrectly'
    },
    commands.UserInputError: {
        'title': 'User Input Error',
        'description': 'You have given some incorrect input'
    },
}


# Import discord-flags only if available
try:
    from discord.ext import flags
except ImportError:
    pass
else:
    # The flags module is installed!
    COMMAND_ERROR_MESSAGES[flags._parser.ArgumentParsingError] = {
        'title': 'Flag Parsing Error',
        'description': 'There is an error in the flags passed to this command'
    }
