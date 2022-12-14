from django.db import models


class ProductsModel(models.Model):
    title = models.CharField(max_length=200)
    article = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey('ProductStatusModel', on_delete=models.SET_NULL, null=True)
    path = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.title


class ProductStatusModel(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
