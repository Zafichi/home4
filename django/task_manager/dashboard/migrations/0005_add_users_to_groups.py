from django.contrib.auth.models import Group, User
from django.db import migrations


def add_users_to_groups(apps, schema_editor):
    gr_of_man = Group.objects.get(name='Manager')
    gr_of_dev = Group.objects.get(name='Developer')
    users = User.objects.exclude(id=1)
    for u in range(1, len(users)):
        user = User.objects.get(id=u)
        if user.is_staff:
            user.groups.add(gr_of_man)
        else:
            user.groups.add(gr_of_dev)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0004_add_users'),
    ]

    operations = [
        migrations.RunPython(add_users_to_groups, migrations.RunPython.noop)
    ]
