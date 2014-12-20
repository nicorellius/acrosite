<!---
markdown syntax: http://daringfireball.net/projects/markdown/syntax
-->

# Acrostic Tees Style Guide
#### Created on December 10, 2014

Read up on Python standards: <a href="http://legacy.python.org/dev/peps/pep-0008/" target="_blank">http://legacy.python.org/dev/peps/pep-0008/</a>

See this great presentation about unicode: <a href="http://nedbatchelder.com/text/unipain.html" target="_blank">Unicode and Python Pain</a>

**Project Specific Styles**

Where possible, it is recommended to use the pop-0008 style guide for writing Python. However, in this project, here are a few extra adviseries:

- use two (2) lines between functions and classes.
- put python imports at top, followed by Django, followed by project-specific imports, each separated by one (1) line. For example, this might look like this:

        import os
    
        from django.conf import settings
    
        from apps.generator.views import GenerateAcrosticFormView
        
- for string formatting, use `format()` rather than `%` or `+` concatenation (see below for when to use `+`, see <a href="http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format" target="_blank">this post</a>:

        print("The {0} eats the {1}.".format('dog', 'cat'))
        
- for string concatenation, use `+` for joining two (2) strings. If more than two (2), use `join()`, see <a href="http://stackoverflow.com/questions/2133571/most-pythonic-way-to-concatenate-strings" target="_blank">this post</a>:

        string = substring + '\n'
        string = ''.join([self.name, '\n', self.part_of_speech, '\n', 'tags:\n'])
        
- use single quotes for characters and small strings that don't make up intelligible sentences. Use double quotes for strings that should read like sentences, eg, error messages, alerts to user, etc. See <a href="http://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python" target="_blank">this post</a>.:

        component_words = self.horizontal_words.split(';')
        print("DEBUG: error rendering view.")
        
- use augmented assignment statements where possible:

        sequence = sequence + 1  # not good
        sequence += 1  # good
        
- comments should be double spaced after end of code line and have one space between pound sign and comment:

        print("fatal error: please try again!")  # error message