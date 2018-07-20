"""
cake.py - Because cake is not a lie!
Copyright 2016, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

A module for the Sopel IRC Bots.
"""

from sopel.module import commands, example


@commands('cake')
@example('.cake')
@example('.cake <nick>')
def cake(bot, trigger):
    """Give someone some cake."""
    if not trigger.group(2):
        bot.action(f"gives {trigger.nick} a slice of cake and a tall glass of milk. \U0001F382")
        return

    bot.action(f"gives {trigger.group(2)} a slice of cake and a tall glass of milk... courtesy of {trigger.nick}! "
               f"\U0001F382")


if __name__ == '__main__':
    pass
