from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Member(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(default='')

    def __str__(self):
        return self.user.username

    def avatar(self):
        api = "http://api.adorable.io/avatars/96/{}@adorable.io.png"
        return api.format(self)

    def thumbnail(self):
        api = "http://api.adorable.io/avatars/32/{}@adorable.io.png"
        return api.format(self)


@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
