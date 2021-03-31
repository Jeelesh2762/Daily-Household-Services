# from django.db import models
# from service.models import Category


# class Customer(models.Model):
#     username = models.CharField(max_length=100,unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=10)
#     email = models.EmailField()
#     password = models.CharField(max_length=10)
#     user_type = models.CharField(max_length=5, default="cust")

#     class Meta:
#         db_table = 'Customer'


# class ServiceProvider(models.Model):
#     username = models.CharField(max_length=100,unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     mobile_no = models.CharField(max_length=10)
#     email = models.EmailField()
#     password = models.CharField(max_length=10)
#     service_rate = models.IntegerField(default=0)
#     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     s_license = models.CharField(max_length=50, default=1)
#     profile_description = models.CharField(max_length=255, default=1)
#     user_type = models.CharField(max_length=5, default="sp")

#     class Meta:
#         db_table = 'ServiceProvider'
from django.db import models
from service.models import Category


class Customer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    user_type = models.CharField(max_length=5, default="cust")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Customer'


class ServiceProvider(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    service_rate = models.IntegerField(default=0)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    s_license = models.CharField(max_length=50, default=1)
    profile_description = models.CharField(max_length=255, default=1)
    user_type = models.CharField(max_length=5, default="sp")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'ServiceProvider'
