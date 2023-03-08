#!/usr/bin/env python

import datetime
import math
import random
import time


@staticmethod
def readFileFrom(path=None):
    if None != path:
        return open(path, 'r').readlines()


def generate_token():
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    return f"z{math.floor(random.random() * random.random() * unix_timestamp)}"


def starter(TIMING):
    lines = readFileFrom("ascii.starter")
    print("".join(lines))
    time.sleep(TIMING)
