# django-pages
Pages, categories, tags for django.

# Install
* Add ```'apps.pages',``` to ```INSTALLED_APPS ```
* Add ```'apps.pages.middleware.PageMiddleware',``` to end of ```MIDDLEWARE_CLASSES```
* Add ```url(r'^', include('apps.pages.urls')),``` to end of urls.py 
* manage.py syncdb
## Notise
If you want to use multilanguage you must instal ```django-modeltranslation```, define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.

# To Do
* Check flatpages view!
* New templates
* Custom templates
* Translate image field?

* New views
* New **news** urls
	/news/some-thing-heppen/
	/news/page-1/
		http://ux.stackexchange.com/questions/16045/pagination-urls
		http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html
	/news/2013/
	/news/2013/01/
	/news/2013/01/23/
