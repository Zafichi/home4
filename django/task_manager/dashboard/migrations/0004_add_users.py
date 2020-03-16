from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.db import migrations
import csv
from django.conf import settings
import os


def add_users(apps, schema_editor):
    path = os.path.join(settings.BASE_DIR, 'dashboard', 'migrations', 'data', 'add_users.csv')
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            User.objects.create(
                password=make_password(line['password']),
                username=line['username'],
                email=line['email'],
                is_staff=bool(line['is_staff'],))
        # gr_of_man = Group.objects.get(name='Manager')
        # gr_of_dev = Group.objects.get(name='Developer')
        # users = User.objects.exclude(id=1)
        # for u in range(1, len(users)):
        #     user = User.objects.get(id=u)
        #     if user.is_staff:
        #         user.groups.add(gr_of_man)
        #     else:
        #         user.groups.add(gr_of_dev)


# def add_users(apps, schema_editor):
#     path = os.path.join(settings.BASE_DIR, 'dashboard', 'migrations', 'data', 'add_managers.csv')
#     _create_users(path, 'Manager', apps)
#     path = os.path.join(settings.BASE_DIR, 'dashboard', 'migrations', 'data', 'add_developers.csv')
#     _create_users(path, 'Developer', apps)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0003_add_permissions'),
    ]

    operations = [
        migrations.RunPython(add_users, migrations.RunPython.noop)
    ]
