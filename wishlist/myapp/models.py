from django.db import models

NULLABLE = {'null': True, 'blank': True}


class MyWishList(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена", **NULLABLE)
    url = models.URLField(verbose_name="Ссылка", **NULLABLE)
    description = models.TextField(verbose_name="Примечание", **NULLABLE)

    def __str__(self):
        return self.name
