"""
passthrough.py - Because sometimes things do work right the first time!
Copyright 2018, Kharidiron [kharidiron@gmail.com]"
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

A module for the Sopel IRC Bots.
"""

import re

from sopel.module import rule, commands
from sopel.tools import get_command_regexp

import flip
import cake
import hug
import twerk


class Trigger:
    def __init__(self, old_trigger, new_nick, match):
        self.user = old_trigger.user
        self.nick = new_nick
        self.event = old_trigger.event
        self.group = match.group
        self.groups = match.groups
        self.groupdict = match.groupdict


@rule('\[.*\] \<(.*)\> (\..*)')
def passthrough(bot, trigger):
    # Grab the discord user and what they said
    user = trigger.group(1)
    text = trigger.group(2)

    # Split out the command part of the text
    cmd = text.split()[0][1:]

    # Re-use the Sopel regexp on the text passed
    prefix = bot.config.core.prefix
    regexp = get_command_regexp(prefix, cmd)
    re_match = regexp.match(text)

    # Create a trigger class mirroring what we need from the offical one
    my_trigger = Trigger(trigger, user, re_match)

    # Only works on my commands (currently hard-coded.)
    if cmd == 'flip':
        flip.flip(bot, my_trigger)
    elif cmd == 'twerk':
        twerk.twerk(bot, my_trigger)
    elif cmd == 'hug':
        hug.hug(bot, my_trigger)
    elif cmd == 'cake':
        cake.cake(bot, my_trigger)
    else:
        pass


if __name__ == "__main__":
    pass
