from django.db import models

from apps.members.models import Member
from core.models import TimeStampedModel


class StoryCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.name


class Story(TimeStampedModel):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    category = models.ForeignKey(StoryCategory)
    author = models.ForeignKey(Member)

    def __unicode__(self):
        return self.title
