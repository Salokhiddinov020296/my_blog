import datetime
import os.path
import random
from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


def upload_to_blogs(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = "{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
        datetime.datetime.now(),
        random.randint(100000, 999999),
        ext
    )
    return "{:%Y}/{:%m}/{}".format(
        datetime.datetime.now(),
        datetime.datetime.now(),
        filename
    )


class CategoryModel(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogsModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_to_blogs)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def save(self, *args, **kwargs):
        if self.image:
            try:
                image_file = BytesIO(self.image.read())
                image = Image.open(image_file)
                image.thumbnail((500, 500), Image.ANTIALIAS)
                image_file = BytesIO()
                image.save(image_file, 'JPG')
                self.image = File(image_file, name=self.image.name + '.jpg')
            except:
                pass
        return super().save(*args, **kwargs)
