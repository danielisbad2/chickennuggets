def set_footer(embed, client_user=None):
    """
    Set a "Powered by Chicken Nuggets" footer on the given embed.

    :param embed: Embed to add the footer to
    :param client_user: ClientUser whose avatar will be added to the footer
    """

    if client_user is None:
        embed.set_footer(
            text='Powered by Chicken Nuggets'
        )
    else:
        embed.set_footer(
            text='Powered by Chicken Nuggets',
            icon_url=client_user.avatar_url
        )
