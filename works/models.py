from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class WorksCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'work category'
        verbose_name_plural = 'works category'


class WorksModel(models.Model):
    category = models.ManyToManyField(WorksCategoryModel)
    title = models.CharField(max_length=255)
    body = RichTextUploadingField
    created_at = models.DateTimeField(auto_now_add=True)
    works_image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'
