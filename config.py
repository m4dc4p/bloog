import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# If we're debugging, turn the cache off, etc.
# Set to true if we want to have our webapp print stack traces, etc
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
logging.info("Starting application in DEBUG mode: %s", DEBUG)

# Don't change default_blog or default_page to prevent conflicts when merging #  Bloog source code updates.
# Do change blog or page dictionaries at the bottom of this config module.


default_blog = {
    "bloog_version": "0.8",
    "html_type": "text/html",
    "charset": "utf-8",
    "title": "Bloog",
    "author": "Bill Katz",
    # This must be the email address of a registered administrator for the
    # application due to mail api restrictions.
    "email": "you@foo.com",
    "description": "A RESTful Blog/Homepage for Google AppEngine.",
    "root_url": "http://bloog.billkatz.com",
    "master_atom_url": "/feeds/atom.xml",
    # By default, visitors can comment on article for this many days.
    # This can be overridden by setting article.allow_comments
    "days_can_comment": 60,
    # You can override this default for each page through a handler's call to
    #  view.ViewPage(cache_time=...)
    "cache_time": 0 if DEBUG else 3600,

    # Use the default YUI-based theme.
    # If another string is used besides 'default', calls to static files and
    #  use of template files in /views will go to directory by that name.
    "theme": "default",

    # If you want to use legacy ID mapping for your former blog platform,
    # define it here and insert the necessary mapping code in the
    # legacy_id_mapping() function in ArticleHandler (blog.py).
    # Currently only "Drupal" is supported.
    "legacy_blog_software": None
    #"legacy_blog_software": "Drupal"
}

default_page = {
    "title": default_blog["title"],
    "articles_per_page": 5,
    "navlinks": [
        { "title": "Articles", "description": "Bits of Info",
          "url": "/articles"},
        { "title": "Contact", "description": "Send me a note",
          "url": "/contact"},
    ],
    "featuredMyPages": {
        "title": "Bloog Development",
        "description": "Get involved",
        "entries": [
            { "title": "Source Code",
              "url": "http://github.com/DocSavage/bloog",
              "description": "GitHub repository" },
            { "title": "Tarball",
              "url": "http://github.com/DocSavage/bloog/tarball/master",
              "description": "Most recent snapshot" },
            { "title": "Group",
              "url": "http://groups.google.com/group/bloog/topics",
              "description": "Developer discussion" },
            { "title": "Author's Bloog",
              "url": "http://www.billkatz.com",
              "description": "What's brewing" },
            { "title": "Architecture Diagram",
              "url": "/static/images/architecture2.png",
              "description": "RESTful Bloog" }
        ]
    },
    "featuredOthersPages": {
        "title": "Google App Engine",
        "description": "Developer Resources",
        "entries": [
            { "title": "Google App Engine",
              "url": "http://code.google.com/appengine/",
              "description": "The mothership" },
            { "title": "AppEngine Group",
              "url": "http://groups.google.com/group/google-appengine",
              "description": "Google Group for App Engine developers" },
            { "title": "GAE SWF Project",
              "url": "http://gaeswf.appspot.com/",
              "description": "Flash and Flex on Google AppEngine" },
            { "title": "Dev Console",
              "url": "http://localhost:8080/_ah/admin/datastore",
              "description":
                "Your datastore viewer and console if running locally" }
        ]
    },
}

# Customize the following two dictionaries to tailor this Bloog to your taste.
# The view will preferentially use 'blog' and 'page' dictionaries.

codeslower_blog = {
    "bloog_version": "0.8",
    "html_type": "text/html",
    "charset": "iso-8859-1",
    "title": "codeslower.com",
    "author": "Justin Bailey",
    # This must be the email address of a registered administrator for the
    # application due to mail api restrictions.
    "email": "jgbailey+blog@codeslower.com",
    "description": "Savor Your Code.",
    "root_url": "http://blog.codeslower.com",
    "master_atom_url": "/feeds/atom.xml",
    "days_can_comment": 60,
    "cache_time": 0 if DEBUG else 3600,
    "theme": "default",
    "legacy_blog_software": None
}

codeslower_page = {"title": codeslower_blog["title"],
    "navlinks": [{ "title": "Contact"
                  , "description": "Send me a note"
                  , "url": "mailto:" + codeslower_blog['email'] },],
    # Currently tags are hardwired to prevent datastore access.
    # Might shift to lookup + cache.
    "articles_per_page": 5,
    "tags": [],
    "featuredMyPages": {    },
    "featuredOthersPages": {    },
}

BLOG = codeslower_blog
PAGE = codeslower_page
