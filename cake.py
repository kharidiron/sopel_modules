# coding=utf8
"""
cake.py - Because cake is not a lie!
Copyright 2016, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

An module for the Phenny/Willie/Sopel IRC Bots.
"""

from __future__ import unicode_literals, absolute_import, print_function, division
import sys

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr


@commands('cake')
def cake(bot, trigger):
    """Give someone some cake"""
    if not trigger.group(2):
        bot.action(u'gives {} a slice of cake and a tall glass of milk.'
                    '\U0001F382'.format(trigger.nick))
        return

    target = trigger.group(2)
    bot.action(u'gives {} a slice of cake and a tall glass of milk... '
                'courtesy of {}! \U0001F382'.format(target, trigger.nick))
    return 

if __name__ == '__main__':
    pass

