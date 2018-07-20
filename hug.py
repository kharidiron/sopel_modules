"""
hug.py - Because we all need a hug!
Copyright 2018, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

A module for the Sopel IRC Bots.
"""

from random import choice

from sopel.module import commands, example


verb = ["hugs", "hugs", "hugs", "squishes", "tacklehugs", "glomps",
        "embraces", "squeezes"]
flavor = ["tightly", "gently", "in the most lewd way possible", "wholesomely",
          "lovingly", "cutely", "nicely", "warmly", "and gropes their butt",
          "extra tightly", "reassuringly", "from behind"]


@commands('hug')
@example('.hug')
@example('.hug <username>')
def hug(bot, trigger):
    """Give someone a hug... or something more."""
    hugged = trigger.group(3) if trigger.group(3) else "no one in particular"

    bot.say(f"{trigger.nick} {choice(verb)} {hugged} {choice(flavor)}.")


if __name__ == "__main__":
    pass
