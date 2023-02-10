from django.db import models

class User(models.Model):
    phone_number = models.CharField(max_length=13)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=20)


    def __str__(self):
        return self.chat_id

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=255)


    def __str__(self):
        return self.user.first_name