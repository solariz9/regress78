from django.db import models
from commons.core import UploadTo
from blog.managers import ListManager
from blog.models import (
    Author,
    Tag,
)


class Records(models.Model):

    published_items = ListManager()

    record_url = models.CharField(max_length=1024,
                                  null=False,
                                  verbose_name="ссылка на запись")
    title = models.CharField(max_length=1024,
                             verbose_name="название")

    published = models.BooleanField(default=False,
                                    verbose_name="активен")
    date_published = models.DateTimeField(auto_now=True)

    record_date = models.DateTimeField(default="2017-01-01", verbose_name="дата эфира")

    pic = models.ImageField(
        'обложка',
        upload_to=UploadTo('records'),
        null=True,
        blank=True
    )
    dj = models.ManyToManyField(Author,
                                verbose_name="DJ",
                                default=None)

    tag = models.ManyToManyField(Tag,
                                 verbose_name="теги")

    class Meta:
        verbose_name = "Запись эфира"
        verbose_name_plural = "Записи эфиров"
