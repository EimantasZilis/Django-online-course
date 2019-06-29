import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from faker import Faker
from first_app.models import AccessRecord, Webpage, Topic

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topic.save()
    return topic

def populate(N=5):
    for entry in range(N):
        # Create fake data
        fk_url = fakegen.url()
        fk_date = fakegen.date()
        fk_name = fakegen.company()
        top = add_topic()

        # Create new web page entry and fake access record for it
        webpg = Webpage.objects.get_or_create(topic=top, url=fk_url, name=fk_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fk_date)[0]

if __name__ == '__main__':
    print("Populating scripts!")
    populate(90)
    print(" >> Complete ")
