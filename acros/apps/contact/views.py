"""
file        :   views.py
date        :   2013-1220
module      :   contact
classes     :   
desription  :   view for contact us page
"""

import logging
from time import strftime

from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from contact.forms import ContactForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


def contact_us(request):
    
    # if the form has been submitted
    if request.method == 'POST':
        
        # form bound to the POST data
        form = ContactForm(request.POST)
        
        # all validation rules pass
        if form.is_valid():
            
            # process the data in form.cleaned_data
            cd = form.cleaned_data
            
            message = '\nmessage:\n{0}'.format(cd['message'])
            
            body = "you have a message from aerial solutions contact page.\n"
            body += "\n-----\n"
            body += "\nname: {0}\ncompany: {1}\nphone: {2}\n{3}".format(
                cd['name'], cd['company'], cd['phone'], message
            )
            
            # send mail to cleaned data fields
            send_mail(
                cd['subject'],
                body,
                cd.get('sender', 'nicorellius.mail@gmail.com'),
                ['nicorellius@gmail.com'],
            )
            
            logger.info('contact form used to send email to site admins: ' + strftime("%A, %B %d, %Y, %H:%M"))
            
            # redirect after post
            return HttpResponseRedirect('/contact/thanks/')
    
    else:
        # show unbound form
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})