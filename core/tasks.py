import os, sys 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print('+ BASE_DIR: {}'.format(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page

def populate_database():

	python_pages = [
	{"title": "Official Python Tutorial",
	"url":"http://docs.python.org/2/tutorial/"},
	{"title":"How to Think like a Computer Scientist",
	"url":"http://www.greenteapress.com/thinkpython/"},
	{"title":"Learn Python in 10 Minutes",
	"url":"http://www.korokithakis.net/tutorials/python/"} ]

	django_pages = [
	{"title":"Official Django Tutorial",
	"url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
	{"title":"Django Rocks",
	"url":"http://www.djangorocks.com/"},
	{"title":"How to Tango with Django",
	"url":"http://www.tangowithdjango.com/"} ]

	other_pages = [
	{"title":"Bottle",
	"url":"http://bottlepy.org/docs/dev/"},
	{"title":"Flask",
	"url":"http://flask.pocoo.org"} ]

	category = {"Python": {"pages": python_pages},
	"Django": {"pages": django_pages},
	"Other Frameworks": {"pages": other_pages} }

	# Get data from dictionaries and create objects in the database
	for categ, categ_data in category.iteritems():
		c = add_category(categ)
		for p in categ_data["pages"]:
			p = add_page(c, p["title"], p["url"])

	# Print out the Categories we have just added.
	for category in Category.objects.all():
		for page in Page.objects.filter(category=category):
			print("{0} : {1}".format(category, page))



def add_page(category, title, url):
	p = Page.objects.get_or_create(category = category, title = title)[0]
	p.url = url,
	p.views = len(title)
	p.save()
	return p

def add_category(name):
	c = Category.objects.get_or_create(name = name)[0]
	c.save()
	return c

if __name__ == '__main__':
	populate_database()