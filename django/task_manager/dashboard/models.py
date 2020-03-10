from django.db import models
from django import urls

from django.conf import settings


class Project(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=1000
    )
    created_at = models.DateField(
        auto_now=True,
        null=True
    )
    logo = models.FileField(null=True, upload_to='logos')

    users = models.ManyToManyField('auth.User')

    def get_absolute_url(self):
        return urls.reverse('projects-detail', args=[str(self.id)])


class Issue(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=2000
    )
    created_at = models.DateTimeField(
        auto_created=True
    )
    reported = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='reporters',
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='assigns'
    )
    deadline = models.DateField(
        null=False,
        blank=False
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True
    )
