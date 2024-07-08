from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Note

@receiver(post_save,sender=Note)
def create_slug(sender,instance:Note,created,*args, **kwargs):
    if created:
        instance.slug = instance.who+'-'+instance.title+'-'+str(instance.id)
        instance.save()