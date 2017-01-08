# coding=utf8
"""
twerk.py - Because we all need to get some twerk done!
Copyright 2017, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

An module for the Phenny/Willie/Sopel IRC Bots.
"""

import sys
from datetime import datetime, timedelta

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr

def _initialize(bot):
    if not bot.memory.contains("twerk_counter"):
        bot.memory["twerk_counter"] = 0
    if not bot.memory.contains("twerk_limiter"):
        bot.memory["twerk_limiter"] = datetime.now()

def _check(bot):
    if bot.memory["twerk_limiter"] < datetime.now():
        bot.memory["twerk_counter"] = 0

    if bot.memory["twerk_counter"] == 0:
        bot.memory["twerk_limiter"] = datetime.now() + timedelta(minutes = 10)
    elif bot.memory["twerk_counter"] >= 10 and datetime.now() < bot.memory["twerk_limiter"]:
        return False
    return True

@commands("twerk")
def twerk(bot, trigger):
    """Instructs the sopel bot to 'twerk it."""
    _initialize(bot)

    if not _check(bot):
        print("twerk-bot is over twerked.")
        return bot.reply("Sorry, I'm out of twerk. Let me recharge... -_-; ")

    if not trigger.group(2):
        bot.memory["twerk_counter"] += 1
        return bot.action("twerks.")
    target = " ".join(trigger.group().split()[1:])
    try:
        if target == "harder":
            bot.memory["twerk_counter"] += 1
            return bot.action("twerks harder.")
        if target == "even harder":
            bot.memory["twerk_counter"] += 1
            return bot.action("is a veritable twerk-nado!")
        else:
            bot.memory["twerk_counter"] += 1
            return bot.action("twerks it '{}' style (what does that even mean?!)".format(target))
    except ValueError:
        return bot.reply(u"I can't twerk like that. -_-; ")

if __name__ == "__main__":
    pass

