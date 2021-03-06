#!/usr/bin/env python
"""

Copyright (c) 2008  Dustin Sallings <dustin@spy.net>
"""

import os
import sys

from twisted.internet import reactor, protocol, defer, task

from twittytwister import twitter

def cb(answer):
    def f(x):
        print answer
    return f

twitter.Twitter(sys.argv[1], sys.argv[2]).verify_credentials().addCallback(
    cb("worked")).addErrback(cb("didn't work")).addBoth(
    lambda x: reactor.stop())

reactor.run()
