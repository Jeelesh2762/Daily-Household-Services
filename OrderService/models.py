from django.db import models
from registration.models import Customer, ServiceProvider


class OrderService(models.Model):
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field="username")
    s_id = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, to_field="username")
    order_status = models.CharField(max_length=10)
    city = models.CharField(max_length=50, null=True)
    mobile_no = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "OrderService"
