<!---
markdown syntax: http://daringfireball.net/projects/markdown/syntax
-->

# Acrostic Tees
#### Created on October 2, 2014

There is a T-shirt that one of the developers wears every Thursday, which features something called an 'Acrostic':

So    
Happy    
It's    
Thursday

An acrostic is a poem or other form of writing in which the first letter, syllable or word of each line, paragraph or other recurring feature in the text spells out a word or a message.  In this case, the first letter of each word spells a message.

This project is about programmatically generating such clever acrostics, which could be then be put on tee shirts, coffee mugs, and other merchandise.

There is a working version of this here: http://ecrostic.opsys.io/

## The (acro)stack

Python 3.2, 3.3 or 3.4 <a href="https://www.python.org" target="_blank">https://www.python.org</a>    
Django 1.7 <a href="https://www.djangoproject.com/" target="_blank">https://www.djangoproject.com/</a>    
SQLite3 3.7.9 <a href="http://www.sqlite.org/" target="_blank">http://www.sqlite.org/</a>    
PostgreSQL 8/9 <a href="http://www.postgresql.org/" target="_blank">http://www.postgresql.org/</a>    
Apache 2.2 (2.2 and above) <a href="http://httpd.apache.org/" target="_blank">http://httpd.apache.org/</a>    
WSGI 3.4 (mod_wsgi) <a href="http://modwsgi.readthedocs.org/" target="_blank">http://modwsgi.readthedocs.org/</a>    

**Dependencies/requirements**

Check the `requirements.txt` file on the root of this repository for up-to-date dependencies and plugins.

    #requirements.txt for acrosite
    distribute==0.7.3
    Django==1.7
    django_compressor==1.4
    django-localflavor==1.0
    django-session-security==2.2.1
    django-debug-toolbar==1.2.1
    selenium==2.43.0

Also, you will need `virtualenv` for isolating your Python projects:

<a href="http://virtualenv.readthedocs.org" target="_blank">http://virtualenv.readthedocs.org</a>    
<a href="http://virtualenvwrapper.readthedocs.org" target="_blank">http://virtualenvwrapper.readthedocs.org</a>

## Installation

For more details, check out these posts (they needs some cleaning up since they were written a while ago):

Linux:    
<a href="http://pdxpixel.com/blog/setting-up-django-on-ubuntu-with-virtualenv-and-mod_wsgi/" target="_blank">http://pdxpixel.com/blog/setting-up-django-on-ubuntu-with-virtualenv-and-mod_wsgi/</a>

Mac OSX Mavericks:  
[Quick Setup](http://www.merplerps.com/configuring-imac-mavericks-develop-django/)  
Here's some [stuff](http://blog.kristian.io/post/46338461184/how-i-develop-django-projects/) that might be useful.  

Windows:    
<a href="http://pdxpixel.com/blog/setting-up-python-and-virtualenv-windows-cygwin/" target="_blank">http://pdxpixel.com/blog/setting-up-python-and-virtualenv-windows-cygwin/</a>

**Briefly**

- Clone the repository
- Pull changes and update
- Install `virtualenv` (on Linux, use `virtualenvwrapper`) and create a virtual environment with command: `mkvirtualenv acrosite`
- Check pip (will be installed with creation of your first virtual environment)
- Install all requirements with command: `pip install -r requirements.txt`
- Set up Django and database (SQLite for now - see docs for more details)
- Start Django: `django-admin.py runserver --settings=acros.settings.local`
