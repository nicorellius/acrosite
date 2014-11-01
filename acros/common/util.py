"""
file        :   util.py
date        :   2014-0223
module      :   common
classes     :   
desription  :   common uitlity tools and functions
"""
 
import datetime
import random, string
import hashlib


"""
get time in format I like

"""
def get_timestamp():
    
    dt = datetime.datetime.now()
    timestamp = dt.strftime("%Y-%m%d, %X")
    return timestamp


def gen_uid(length):

    concat_string = string.lowercase + string.digits
    
    hashed_string = hashlib.sha1(concat_string)
    
    hashed_id = ''.join(random.sample(concat_string, length))
    
    return hashed_i