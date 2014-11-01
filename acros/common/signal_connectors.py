"""
file        :   signal_connectors.py
date        :   2014-0619
module      :   common
classes     :   
desription  :   holds receivers for system signals
"""

import logging
from time import strftime

from django.core.mail import mail_admins
from django.core.signals import request_finished
from django.dispatch import receiver

from django.template.loader import render_to_string
from django.template import Template, Context, RequestContext

from django.contrib import messages
from django.contrib.auth.signals import user_logged_out

from registration.signals import user_registered, user_activated

from common.signals import upload_file_completed


# get an instance of a logger
logger = logging.getLogger(__name__)

@receiver(user_registered, dispatch_uid="common.signal_connectors.user_registered_handler")
def user_registered_handler(sender, user, request, **kwargs):
    
    # log info message based on logger settings
    logger.info('{0}'.format(user) +
        ' registered successfully at aerial solutions: ' +
        strftime("%A, %B %d, %Y, %H:%M"))
    
    subject = 'aerial solutions user registration message'
    template = Template('{{ user }} has registered at aerial solutions: {% now "l, F j, Y H:i" %}')
    context = Context({ 'user': user })
    message = template.render(context)
    from_email = 'info@cistechconsulting.com'
    #to = 'nicorellius@gmail.com'
    
    # send email to admins, if user has been registered
    mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
    
    # log info message based on logger settings
    logger.info('registration email sent to administrators: ' + strftime("%A, %B %d, %Y, %H:%M"))
    
@receiver(user_activated, dispatch_uid="common.signal_connectors.user_activated_handler")
def user_activated_handler(sender, user, request, **kwargs):
    
    # log info message based on logger settings
    logger.info('{0}'.format(user) +
        ' activated an account successfully at aerial solutions: ' +
        strftime("%A, %B %d, %Y, %H:%M"))
    
    subject = 'aerial solutions user activation message'
    template = Template('{{ user }} has activated an account at aerial solutions: {% now "l, F j, Y H:i" %}')
    context = Context({ 'user': user })
    message = template.render(context)
    from_email = 'info@cistechconsulting.com'
    #to = 'nicorellius@gmail.com'
    
    # send email to admins, if user has been activated
    mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
    
    # log info message based on logger settings
    logger.info('activation email sent to administrators: ' + strftime("%A, %B %d, %Y, %H:%M"))