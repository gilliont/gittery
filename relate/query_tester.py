
import os, sys 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print("-------------------------")
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
						'tango_with_django_project.settings')


import django
django.setup()
from relate.models import Program, Price, Order

# class Program(models.Model):
#     name = models.CharField(max_length=20)

# class Price(models.Model):
#     program = models.ForeignKey(Program)

# class Order(models.Model):
#     state = models.CharField(max_length=20)
#     items = models.ManyToManyField(Price)


def tester():
	o = Order.objects.filter(state='received')
	print("+ Order.objects.filter(state='received'): {}".format(o))
	print(o.query)
	o = Order.objects.filter(state='received').first()
	print('+ o: {}'.format(o))
	p_name = [price.program.name for price in o.items.all()]
	print('+ o: {}'.format(o))
	print('+ p_name: {}'.format(p_name))
	list1 = o.items.values_list('program__name')
	print('+ list1: {}'.format(list1))
	print(list1.query)

	o = Order.objects.filter(state='completed',).prefetch_related('items__program',)
	print('+ Order.objects.filter(state="completed",).prefetch_related("items__program",): {}'.format(o))
	print(o.query)
	o = Order.objects.filter(state='completed',).prefetch_related('items__program',).first()
	list2 = [price.program.name for price in o.items.all()]
	list2 = o.items.values_list('program__name')
	print('+ list2: {}'.format(list2))
	print(list2.query)

if __name__ == '__main__':
	tester()