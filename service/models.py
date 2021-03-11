from django.db import models


class Category(models.Model):
    Category = models.CharField(max_length=50)

    def __str__(self):
        return self.Category

    class Meta:
        db_table = 'Category'
