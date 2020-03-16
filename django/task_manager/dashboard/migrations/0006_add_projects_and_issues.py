from dashboard import models
from django.utils import timezone
from django.db import migrations
from django.conf import settings
import csv
import os


def add_projects(apps, schema_editor):
    path = os.path.join(settings.BASE_DIR, 'dashboard', 'migrations', 'data', 'add_projects.csv')
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            models.Project.objects.create(
                name=line['name'],
                description=line['description'],
            )


def add_issues(apps, schema_editor):
    path = os.path.join(settings.BASE_DIR, 'dashboard', 'migrations', 'data', 'add_issues.csv')
    with open(path) as file:
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            models.Issue.objects.create(
                created_at=timezone.now(),
                name=line['name'],
                description=line['description'],
                deadline=line['deadline'],
                executor_id=line['executor_id'],
                reported_id=line['reported_id'],
            )


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0005_add_users_to_groups'),
    ]

    operations = [
        migrations.RunPython(add_projects, migrations.RunPython.noop),
        migrations.RunPython(add_issues, migrations.RunPython.noop)
    ]
