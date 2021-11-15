import random
import string
import functools
import time
import mysql.connector
import argparse
import sys
from halo import Halo


def percentage_calculator(part, whole):
    return int(round(100 * float(part) / float(whole)))


def rand_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))





