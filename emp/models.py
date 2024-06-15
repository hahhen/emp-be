from django.db import models
class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    variant = models.TextField(blank=True, null=True)  # This field type is a guess.
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)  # This field type is a guess.
    slug = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
