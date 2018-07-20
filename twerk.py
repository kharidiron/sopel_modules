"""
twerk.py - Because we all need to get some twerk done!
Copyright 2017, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

A module for the Sopel IRC Bots.
"""

from datetime import datetime, timedelta

from sopel.module import commands


def _initialize(bot):
    if not bot.memory.contains("twerk_count"):
        bot.memory["twerk_count"] = 0
    if not bot.memory.contains("twerk_limit"):
        bot.memory["twerk_limit"] = datetime.now()


def _check(bot):
    if bot.memory["twerk_limit"] < datetime.now():
        bot.memory["twerk_count"] = 0

    if bot.memory["twerk_count"] == 0:
        bot.memory["twerk_limit"] = datetime.now() + timedelta(minutes=10)
    elif bot.memory["twerk_count"] >= 10 and datetime.now() < bot.memory["twerk_limit"]:
        return False
    return True


@commands("twerk")
def twerk(bot, trigger):
    """Instructs the Sopel bot to 'twerk it."""
    _initialize(bot)

    if not _check(bot):
        print("twerk-bot is over twerked.")
        return bot.reply("Sorry, I'm out of twerk. Let me recharge... -_-; ")

    if not trigger.group(2):
        bot.memory["twerk_count"] += 1
        return bot.action("twerks.")
    target = " ".join(trigger.group().split()[1:])
    try:
        if target == "harder":
            bot.memory["twerk_count"] += 1
            return bot.action("twerks harder.")
        elif target == "even harder":
            bot.memory["twerk_count"] += 1
            return bot.action("is a veritable twerk-nado!")
        else:
            bot.memory["twerk_count"] += 1
            return bot.action(f"twerks it '{target}' style (what does that even mean?!)")
    except ValueError:
        return bot.reply("I don't twerk that way. -_-; ")


if __name__ == "__main__":
    pass
