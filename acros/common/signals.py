"""
file        :   signals.py
date        :   2014-0619
module      :   common
classes     :   
desription  :   signals
"""

import django.dispatch

# file has been uploaded
upload_file_completed = django.dispatch.Signal(providing_args=["request"])