from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    # slug = AutoSlugField(unique=True, populate_from='title')
    slug = models.SlugField(max_length=255, blank= True, null= True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     self.slug = uuslug(self.slug, instance=self)
    #     super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.IntegerField()
    call_back = models.SlugField(max_length=255, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.call_back = slugify(self.title)
        super().save(*args, **kwargs)