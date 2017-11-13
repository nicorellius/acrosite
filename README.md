<!---
markdown syntax: http://daringfireball.net/projects/markdown/syntax
-->

# Acrostic Tees
#### Created on October 2, 2014

Nick has a T-shirt he wears every Thursday, which features something called an 'Acrostic':

So    
Happy    
It's    
Thursday

An acrostic is a poem or other form of writing in which the first letter, syllable or word of each line, paragraph or other recurring feature in the text spells out a word or a message.  In this case, the first letter of each word spells a message.

This project is about programmatically generating such clever acrostics, which could be then be put on tee shirts, coffee mugs, and other merchandise.

## The (acro)stack

Please note that these instructions are from the perspective of a Linux development environment. Installing, running and maintaining a stack like this on Windows requires a bit more finesse. See the blog entry below for Windows.

Also, since we are going with Python 3.2, there are several things to keep in mind. The MySQL/Python connector, `mysql-python`, for example, is no longer supported.

Read up on Python standards: <a href="http://legacy.python.org/dev/peps/pep-0008/" target="_blank">http://legacy.python.org/dev/peps/pep-0008/</a>

See this great presentation about unicode: <a href="http://nedbatchelder.com/text/unipain.html" target="_blank">Unicode and Python Pain</a>

Regarding IDEs, I found a neat markdown plugin for Komodo that enables me to view the markdown files in the IDE. This might be useful for your IDE/dev setup, and I'm sure most IDEs have something like this.

The essential components of the development stack are as follows (SQLite will be used until we need to scale, at which point PostgreSQL):

Python 3.2, 3.3 or 3.4 <a href="https://www.python.org" target="_blank">https://www.python.org</a>    
Django 1.7 <a href="https://www.djangoproject.com/" target="_blank">https://www.djangoproject.com/</a>    
SQLite3 3.7.9 <a href="http://www.sqlite.org/" target="_blank">http://www.sqlite.org/</a>    
PostgreSQL 8/9 <a href="http://www.postgresql.org/" target="_blank">http://www.postgresql.org/</a>    
Apache 2.2 (2.2 and above) <a href="http://httpd.apache.org/" target="_blank">http://httpd.apache.org/</a>    
PHP 5.4 (5.4.20 or above) <a href="http://php.net/">http://php.net/</a> (may not need this but installation a LAMP or LAMP stack is very easy - <a href="https://bitnami.com/stacks" target="_blank">https://bitnami.com/stacks</a>)    
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

##Installation

For more details, check out these posts (they needs some cleaning up since they were written a while ago):

Linux:    
<a href="http://pdxpixel.com/blog/setting-up-django-on-ubuntu-with-virtualenv-and-mod_wsgi/" target="_blank">http://pdxpixel.com/blog/setting-up-django-on-ubuntu-with-virtualenv-and-mod_wsgi/</a>

Mac OSX Mavericks:  
[Quick Setup](http://www.merplerps.com/configuring-imac-mavericks-develop-django/)  
Here's some [stuff](http://blog.kristian.io/post/46338461184/how-i-develop-django-projects/) that might be useful.  

Windows:    
<a href="http://pdxpixel.com/blog/setting-up-python-and-virtualenv-windows-cygwin/" target="_blank">http://pdxpixel.com/blog/setting-up-python-and-virtualenv-windows-cygwin/</a>

**Briefly**

Note that setting up file structure is a developer-centric activity. I usually use something like this (Linux):

    Django projects         /home/<user>/dev/django/projects/<project_repo_name>/<project_name>
    Virtual environments    /home/<user>/dev/virtenvs/<project_name>
    Private/secret bits     /home/<user>/dev/prv/<project_name>
    
Here is a more detailed repository structure for this Django project:

    repository_name/
        . . .
        
        docs/
        resouces/
        .gitignore 
        README.md
        TODO.md
        AUTHORS.md
        requirements/
            base.txt
            local.txt
            . . .
        
        django_project_name
            . . .
            
            django_site_configuration_name
                db.sqlite3
                urls.py
                wsgi.py
                settings
                    base.py
                    local.py
                    . . .
                    
            static
                css
                images
                js
            media
            templates
                base.html
                app_name
                    app_name_descriptor.html
                . . .
                
            manage.py


- Clone the repository
- Pull changes and update
- The next two options (installing LAPP or Apache are optional if setting up local development environment)
- 1) Install LAPP (I find using s stack like this easy to set up and run, since I alredy have PHP/MySQL/PostgreSQL sites using it): <a href="https://bitnami.com/stacks" target="_blank">https://bitnami.com/stacks</a>
- 2) If you don't use LAPP, install Apache: `sudo apt-get install apache2`
- Install `virtualenv` (on Linux, use `virtualenvwrapper`) and create a virtual environment with command: `mkvirtualenv acrosite`
- Check pip (will be installed with creation of your first virtual environment)
- Install all requirements with command: `pip install -r requirements.txt`
- Set up Django and database (SQLite for now - see docs for more details)
- Set up SMTP email credentials, database credentials and secret key files in `prv` directory on development/production file system. This can be done several different ways. For my uses, I go with something like: `/home/<user>/dev/prv/<project_name>`
- Start Django (and LAMP optionally) with startup script. If you use `./manage.py runserver` be sure to include the settings for your local environment (eg, for nick): `./manage.py runserver --settings=acros.settings.nick`

##Settings notes

The preferred method for settings is to use per-dev settings files and check those into source control. In our case, we add `local.py` back to the repo, because it contains critical local settings (db, email settings, etc...), shared among all our local environments, and then we add to the repo these files: `settings/nick.py`, `settings/phil.py`, `settings/jimar.py`. These files will contain pointers to private bits and secrets existing on our file systems in different locations. According to the authors of Two Scoops of Django (<a href="http://twoscoopspress.org/products/two-scoops-of-django-1-5" target="_blank">1.5</a> and <a href="http://twoscoopspress.org/products/two-scoops-of-django-1-6" target="_blank">1.6</a>), keeping all the settings files in the repo is good practice. Another useful feature of using per-dev settings is that each dev might want a secific tool in their INSTALLED_APPS and so this would be something he could add to his `<dev_name>.py` file.

Cool resource: <a href="https://code.djangoproject.com/wiki/SplitSettings" target="_blank">https://code.djangoproject.com/wiki/SplitSettings</a>

##Development environment

In order to use `django-admin.py` for your administrative tasks, you must first adjust your virtual environment's `bin/activate` script to set a couple environmental variables (this is an example of Nick's local environment):

`vim /home/nick/dev/virtenvs/acros/bin/activate`

At the top of the file, add these lines:

    # export Django settings for this virtual environment
    export DJANGO_SETTINGS_MODULE='acros.settings.nick'
    
    # export new PYTHONPATH for this virtual environment
    export PYTHONPATH=$PYTHONPATH:/home/nick/dev/django/projects/acrosite/acros
    
Then, when in the working directory, you can issue commands like this:

    django-admin runserver
    django-admin.py runserver
    ./manage.py runserver

##Unit Testing  
[Here's](http://docs.python-guide.org/en/latest/writing/tests/) some useful bits about testing.  

##Libraries 
We can use [nltk](http://www.nltk.org/) for doing fancy things and generating useful data sets -- analyzing corpora for sentiment, parts of speech, tokenizing, etc. This was added to the `requirements.txt` file.

##Tips and Tricks  
This section is to collect tips and tricks we've learned so far. 

**Installing a Fresh Database**

For example, when applying new migrations or to start from scratch to get your database up and running these steps will help:

1. Delete your database file
2. Delete all your `migrations` folders.
3. Then run these commands:

        ./manage.py syncdb   # accept the creation of the admin, and follow instructions
        ./manage.py makemigrations generator
        ./manage.py makemigrations accounts
        ./manage.py migrate
        ./manage.py runserver
        
4. Launch the application and create your first acrostic. This will take a couple minutes while the database is populated with words.
5. Then log in to [http://localhost:8000/admin/](http://localhost:8000/admin/) and use credentials you created above and check out the database.
