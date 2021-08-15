from django.db import models
from .utils import GenerateMetaLogic

# Create your models here.
class GenerateMeta(models.Model):
    title = models.CharField(max_length=70, default="")
    description = models.CharField(max_length=160, default="")
    keywords = models.CharField(max_length=500, default=0)
    url = models.URLField(default="")
    publish = models.BooleanField(default=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        title, description, keywords = GenerateMetaLogic(self.url)
        self.title = title
        self.description = description
        self.keywords = keywords
        super().save(*args,**kwargs)
