from django.db      import models

from user.models    import User
from bangoraf.utils import TimeStampModel
from product.models import Product

class Payment(TimeStampModel):
    order          = models.OneToOneField("Order", on_delete=models.CASCADE)
    card           = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    ammount        = models.IntegerField()

    class Meta:
        db_table = 'payments'

class Order(TimeStampModel):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    status     = models.ForeignKey("Status", on_delete=models.CASCADE)
    address    = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'orders'

class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'

class Cart(models.Model):
    order         = models.ForeignKey("Order", on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    count         = models.IntegerField(default=1)
    gift_wrapping = models.BooleanField()

    class Meta:
        db_table = 'carts'

class GiftWrapping(models.Model):
    EDITION_GOLD    = 'Gold'
    EDITION_SILVER  = 'Silver'

    EDITION_CHOICES = [
		(EDITION_GOLD, 'Gold'),
        (EDITION_SILVER, 'Silver')
    ]
    edition     = models.CharField(max_length=6, choices=EDITION_CHOICES, default=EDITION_GOLD)
    description = models.TextField()
    cart        = models.ForeignKey("Cart", on_delete=models.CASCADE,related_name="cart")

    class Meta:
        db_table = 'giftwrappings'

class Address(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'address'