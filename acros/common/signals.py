"""
file        :   signals.py
date        :   2014-0619
module      :   common
classes     :   
description :   signals
"""

import django.dispatch

# file has been uploaded
upload_file_completed = django.dispatch.Signal(providing_args=["request"])

# ecrostic not found message
ecrostic_not_found = django.dispatch.Signal(providing_args=["request"])