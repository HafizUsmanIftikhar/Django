import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()

# faker pop script

import random
from firstapp.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for entry
        top = add_topic()

        # create fake data for that entry 
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new web page entry
        web_page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record for web page
        acc_rec = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating script...')
    populate(20)
    print('Populating complete.')

#Note that the `topics` list should be defined with lowercase names to match the `top_name` field in the `Topic` model. Also, the `Webpage` and `AccessRecord` models should be imported from `models.py` in the `firstapp` directory.
