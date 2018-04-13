
import os, sys 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print('+ BASE_DIR: {}'.format(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'tango_with_django_project.settings')


import django
django.setup()
from relate.models import Program, Price, Order

def populate_relate_tables():

	sample_program = [
	{"name": "Learn Django"},
	{"name": "AWS"},
	{"name": "Machine Learning"},
	]

	sample_price = [
	{"price": 134},
	{"price": 246},
	{"price": 312},
	]

	sample_order = [
	{"state": "shipped"},
	{"state": "received"},
	{"state": "paid"},
	]

	for prog in sample_program:
		for state in sample_order:
			program_instance = add_program(prog["name"])
			price_instance = add_price(program_instance)
			order_instance = add_order(price_instance, state)
		


def add_price(program_instance):
	pr = Price.objects.create(program=program_instance)
	return pr
def add_program(name):
	pa = Program.objects.get_or_create(name=name)[0]
	return pa

def add_order(price_instance, state):
	order = Order.objects.create(items=price_instance, state=state)
	return order

if __name__ == '__main__':
	populate_relate_tables()