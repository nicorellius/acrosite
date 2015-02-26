"""
file        :   util.py
date        :   2014-0223
module      :   common
classes     :   
description :   common utility tools and functions
"""
 
import datetime
import random
import string
import hashlib

import os

import re
import uuid


# get time in format I like
def get_timestamp():
    """
    method to generate timestamp for use in application

    :return timestamp:
    """
    
    dt = datetime.datetime.now()

    timestamp = dt.strftime("%Y-%m-%d %X")

    return timestamp


def gen_uid(length=10):
    """
    method to generate random uuid of varying length for application

    :param length: length of uid
    :return uid: formatted string
    """
    # python 2.7 version
    # concat_string = string.lowercase + string.digits
    # hashed_string = hashlib.sha1(concat_string)
    # # hashed_id = ''.join(random.sample(concat_string, length))
    # hashed_id = ''.join(random.sample(hashed_string, length))
    # return hashed_id

    # TODO - fund one that works in both v2.x/3.x...
    # python 3.x version
    uid = uuid.uuid4()

    tmp_uid = re.sub('-', '', str(uid))

    uid = ''.join(random.sample(list(tmp_uid), length))

    return uid
