from django.db import models
from django.urls import reverse
import datetime
import os
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from ckeditor_uploader.fields import RichTextUploadingField

STATIC_UPLOAD_PRODUCT_URL = 'static/upload/product/'

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

def upload_product_image(instance, filename):

    ext = filename.split('.')[-1]
    name = (instance.name).replace(" ", "_")
    filename = "%s_%s.%s" % (instance.slug, instance.id, ext)
    today = datetime.datetime.now()
    today_path = today.strftime("%Y/%m/%d")
    fullname = os.path.join(STATIC_UPLOAD_PRODUCT_URL + today_path + '/', filename)
    return fullname

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    description = RichTextUploadingField(null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_product_image , blank=True)

    class Meta:
        ordering = ('-name', )
        index_together = (('id', 'slug'),)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="%s" height="70px"/>' % (self.image.url))
    image_tag.short_description = ''
    image_tag.allow_tags = True

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

def product_image_slider(instance, filename):
    time = datetime.datetime.now().timestamp()
    folder_name = str(instance.product.id)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (time, ext)
    fullname = os.path.join(STATIC_UPLOAD_PRODUCT_URL + folder_name + '/', filename)
    return fullname

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_slider, null=True)

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Products Image')

    def image_tag(self):
        return format_html('<img src="%s" width="200px"/>' % (self.image.url))
    image_tag.short_description = ''
    image_tag.allow_tags = True
