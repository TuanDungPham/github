from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.TextField(blank=True)
    category_parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE
        )
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        # ordering = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.TextField()
    icon = models.TextField(blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta():
        db_table = "Brand"

class Detail(models.Model):
    name = models.CharField(max_length=100)
    screen = models.CharField('Màn hình', max_length=100, blank=True)
    operating_system = models.CharField('Hệ điều hành', max_length=100, blank=True)
    rear_camera = models.CharField('Camera sau', max_length=100, blank=True)
    front_camera = models.CharField('Camera trước', max_length=100, blank=True)
    chip = models.CharField('Chip', max_length=50, blank=True)
    RAM = models.CharField('RAM', max_length=100, blank=True)
    memory = models.CharField('Bộ nhớ trong', max_length=200, blank=True)
    sim = models.CharField('SIM', max_length=200, blank=True)
    battery = models.CharField('Pin', max_length=50, blank=True)
    adapter = models.CharField('Sạc', max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Detail"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    detail = models.ForeignKey(Detail,on_delete=models.CASCADE)
    image = models.TextField()
    status = models.BooleanField(default=True) # True là còn, False là hết kinh doanh
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    path = models.TextField()

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "ProductImage"

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "Promotion"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(timezone.now)
    total_amount = models.IntegerField(null=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    status = models.IntegerField(default=0)
    # 0: Đơn hàng tạm/giỏ hàng, chưa thanh toán
    # 1: Hoàn thành, đã thanh toán

    class Meta:
        db_table = "Order"

class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    amount = models.IntegerField()

    class Meta:
        db_table = "OrderDetail"

