from django.db import models

# Create your models here.
class Template(models.Model):
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    instruction = models.TextField(default="Enter needed informations")
    prompt = models.TextField()
    word_doc = models.FileField(upload_to='templates_files/', null=False)

