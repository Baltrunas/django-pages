# django-pages
Pages, categories, tags for django.

# Install
* Add ```'pages',``` to ```INSTALLED_APPS ```
* Add ```'pages.middleware.PageMiddleware',``` to end of ```MIDDLEWARE_CLASSES```
* Add ```url(r'^', include('pages.urls')),``` to end of urls.py 
* manage.py syncdb
## Notise
If you want to use multilanguage you must instal ```django-modeltranslation```, define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.

# To Do
* New templates
* Custom templates

* New views
* New **news** urls
	/news/some-thing-heppen/
	/news/page-1/
		http://ux.stackexchange.com/questions/16045/pagination-urls
		http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html
	/news/2013/
	/news/2013/01/
	/news/2013/01/23/
