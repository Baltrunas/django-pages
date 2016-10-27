# django-pages
Pages, categories, tags for django.

# Requirements
django-seo
django-helpful

# Install
* Add ```'apps.pages',``` to ```INSTALLED_APPS ```
* Add ```'apps.pages.middleware.PageMiddleware',``` to end of ```MIDDLEWARE_CLASSES```
* Add ```url(r'^', include('apps.pages.urls')),``` to end of urls.py
* python manage.py migrate pages

## Notise
If you want to use multilanguage you must instal ```django-modeltranslation```, define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.

# To Do
* Check flatpages view!
* New templates
* Custom templates
* Translate image field?

# Need?
* New views
* New **news** urls
	/news/some-thing-heppen/
	/news/page-1/
		http://ux.stackexchange.com/questions/16045/pagination-urls
		http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html
	/news/2013/
	/news/2013/01/
	/news/2013/01/23/




Express Pages

без карты, без социальных сетей

seo
	on-page
	off-page
google local

web projects
	бизнес программы

support (django)

portfolio (case)

страница программы СТО



Продукты \ Сервисы
	Diesel UP

Продвижение
	Так и сяк

Сайты

Для бизнеса

Разработка сайтов

Разработка приложений


Главная
	Продвижение
	Сайты
	Проекты для бизнеса

	Портфолио
	Контакты