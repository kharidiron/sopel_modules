"""
flip.py - Because flipping things is fun!
Copyright 2016, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

A module for the Sopel IRC Bots.
"""

from sopel.module import commands, example
import upsidedown


@commands("flip")
@example('.flip')
@example('.flip table[s]')
@example('.flip table ove')
@example('.flip person')
@example('.flip <nick>')
def flip(bot, trigger):
    """Flips things... because that is the whole point."""
    if not trigger.group(2):
        bot.say("What should I flip? o.o")
        return

    target = " ".join(trigger.group().split()[1:])
    try:
        if target == "table":
            return bot.say(u"(╯°□°）╯︵ ┻━┻")
        elif target == "table over":
            return bot.say(u"┬──┬ ノ(゜-゜ノ)")
        elif target == "tables":
            return bot.say(u"┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")
        elif target == "out":
            return bot.say(u"ಠ﹏ಠ")
        elif target == "bird":
            return bot.say(u"t(°□ °t)")
        elif target == "person":
            return bot.say(u"(╯°Д°）╯︵ /(.□ . \)")
        elif target == "russia":
            bot.reply("In Soviet Russia, table flip you!")
            return bot.say(u"┬─┬ ︵  ( \o°o)\\")
        else:
            return bot.say(upsidedown.transform(target))
    except ValueError:
        return bot.reply(u"I can\'t flip that. -_-;")


if __name__ == "__main__":
    pass
