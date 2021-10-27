from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = "categories"

class SubCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)
    class Meta:
        db_table = "subcategories"


class Main(models.Model):
    product        = models.ForeignKey("Product", on_delete=models.CASCADE)
    title          = models.CharField(max_length=50)
    description    = models.CharField(max_length=50)
    main_image_url = models.CharField(max_length=100)
    class Meta:
        db_table = "mains"

class Service(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = "services"

class ProductService(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    class Meta:
        db_table = "productservices"

class Product(models.Model):
    sub_category          = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    title                 = models.CharField(max_length=50)
    detail_title          = models.CharField(max_length=50)
    price                 = models.DecimalField(max_digits=18, decimal_places=0)
    description           = models.TextField()
    services              = models.ManyToManyField("Service",       through="ProductService")
    specifications        = models.ManyToManyField("Specification", through="ProductSpecification")
    color                 = models.ManyToManyField('Color', through="ProductImage")
    class Meta:
        db_table = "products"

class Color(models.Model):
    name               = models.CharField(max_length=50)
    class Meta:
        db_table = "colors"

class ProductImage(models.Model):
    image_url      = models.CharField(max_length=200)
    product        = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_images")
    color          = models.ForeignKey("Color", on_delete=models.CASCADE)
    class Meta:
        db_table = "productimages"

class ProductSpecification(models.Model):
    product           = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    specifications    = models.ForeignKey("Specification", on_delete=models.CASCADE, null=True)
    data = models.JSONField()
    class Meta:
        db_table = "productspecifications"

class Specification(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "specifications"


class Inspiration(models.Model):
    product          = models.OneToOneField("Product", on_delete=models.CASCADE)
    title            = models.JSONField()
    description      = models.JSONField()
    video_url        = models.JSONField()
    slide_image_url  = models.JSONField()
    class Meta:
        db_table = "inspirations"

class Feature(models.Model):
    product      = models.OneToOneField("Product", on_delete=models.CASCADE)
    image_url    = models.JSONField()
    description  = models.JSONField()
    title        = models.JSONField()
    subtitle     = models.JSONField()
    class Meta:
        db_table = "features"