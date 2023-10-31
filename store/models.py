from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=30)
    store_slug = models.SlugField(max_length=15, unique=True, db_index=True)
    address = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
