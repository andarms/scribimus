from django.db import models

from core.models import TimeStampedModel


class StoryCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.name


class Story(TimeStampedModel):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    category = models.ForeignKey(StoryCategory)
