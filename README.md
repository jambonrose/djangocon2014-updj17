# Upgrading Django (to 1.7)

This repository contains the code used in my DjangoCon 2014 presentation. All other materials may be accessed [here](http://afrg.co/updj17/).

**NB**: To ease setup of this demonstration, the Django Secret Key has not been removed from the `settings.py` file. This site should therefore never be used for production purposes.

## Organization

This repository contains two branches: `updj16` and `updj17`.

The first branch contains the project built in Django 1.6.

The second branch contains the code built in Django 1.7.

## Installation and Setup

The following assumes that Python (2.7 or 3.2+), pip, and virtualenvwrapper, are installed. For instruction, please refer to my Django installation guide.

To download the repository and move into the directory:

    $ git clone git@github.com:jambonrose/djangocon2014-updj17.git
    $ cd djangocon2014-updj17

Using a virtual environment is highly recommended. Below, I title the virtual environment `updj17`.

    $ mkvirtualenv updj17
    $ pip install -r requirements.txt

To switch to the first branch, I recommended you create a separate virtual environment, as the requirements are different.

    $ git co updj16
    $ mkvirtualenv updj16
    $ pip install -r requirements.txt

To switch back to the second, default branch, use the following (assuming the creation of the `updj17` virtual environment, as detailed above).

    $ git co updj17
    $ workon updj17

The site is not meant to be run. It is programmed without URL Configuration patterns or views. Instead, the code is intended to let you play with migrations in Django 1.6 with South, and Django 1.7 with native migrations. Please refer to the presentation slides or article for instructions on how to do so.
