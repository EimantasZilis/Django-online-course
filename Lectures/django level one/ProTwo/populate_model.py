import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import Users

fakegen = Faker()

def add_user(id):
    email = fakegen.email()
    name, *midnames, surname = fakegen.name().split()
    user = Users.objects.get_or_create(uid=id, first_name=name,
                                       last_name=surname, email=email)
    user[0].save()

def populate(n=5):
    for x in range(n):
        add_user(x)

if __name__ == '__main__':
    print("Populating scripts!")
    populate(80)
    print(" >> Complete ")
