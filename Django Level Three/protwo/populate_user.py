import os

# configure settings for this project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings') # setup as default
import django
django.setup() # allow as to papulate database

from apptwo.models import users
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for i in range(N):
        fakename=fakegen.name().split()
        f_name=fakename[0]
        l_name=fakename[1]
        fake_email=fakegen.email()

        # new entry in our acual database

        user=users.objects.get_or_create(first_name=f_name,last_name=l_name,email=fake_email)[0]

if __name__== '__main__':
    print('populating data')
    populate(20)
    print('complete populate')



