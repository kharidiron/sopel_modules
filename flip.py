# coding=utf8
"""
flip.py - Because flipping things is fun!
Copyright 2016, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

An module for the Phenny/Willie/Sopel IRC Bots.
"""

from __future__ import unicode_literals, absolute_import, print_function, division
import sys
import upsidedown

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr


@commands('flip')
def flip(bot, trigger):
    """Flips things... because that is the whole point."""
    if not trigger.group(2):
        bot.say('What should I flip? o.o')
        return
    target = trigger.group(2)
    try:
        if target == 'table':
            return bot.say(u'(╯°□°）╯︵ ┻━┻')
        if target == 'table over':
            return bot.say(u'┬──┬ ノ(゜-゜ノ)')
        elif target == 'tables':
            return bot.say(u'┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻')
        elif target == 'out':
            return bot.say(u'ಠ﹏ಠ')
        elif target == 'bird':
            return bot.say(u't(°□ °t)')
        elif target == 'person':
            return bot.say(u'(╯°Д°）╯︵ /(.□ . \)')
        elif target == 'russia':
            bot.reply('In Soviet Russia, table flip you!')
            return bot.say(u'┬─┬ ︵  ( \o°o)\\')
        else:
            return bot.say(upsidedown.transform(target))
    except ValueError:
        return bot.reply(u'I can\'t flip that. -_-;')

if __name__ == '__main__':
    pass

