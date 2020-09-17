from django.db import models

# Create your models here.


class Staff(models.Model):
    full_name = models.TextField(max_length=500)
    birth_day = models.DateTimeField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    current_address = models.TextField(max_length=500, blank=True, null=True)
    photo = models.TextField(max_length=500, blank=True, null=True)
    id_number = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=50, blank=True, null=True)
    email = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "staff"


class Store(models.Model):
    company = models.TextField(max_length=500)
    store_name = models.TextField(max_length=500)
    address = models.TextField(max_length=500, blank=True, null=True)
    presenter = models.OneToOneField(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = "store"
