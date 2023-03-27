from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Lecture(models.Model):
    title = models.CharField(max_length=2048)
    text = RichTextUploadingField()
    youtube = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.title


class ControlQuestion(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, verbose_name="Leksiya")
    question = models.CharField(max_length=4096, verbose_name="nazorat savoli")


class Resource(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=2048)
    image = models.ImageField(upload_to="resource")
