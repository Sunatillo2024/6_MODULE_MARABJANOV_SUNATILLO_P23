from django.db.models import Model, CharField, ForeignKey, ImageField, CASCADE
from django.forms import IntegerField, FloatField


class Category(Model):
    name = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=50, )
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category', CASCADE, related_name='categories')
    price = FloatField()
    quantity = IntegerField()
    def __str__(self):
        return self.name

class Profile(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    image = ImageField(upload_to='profiles/')
    email = CharField(max_length=50)
    phone = CharField(max_length=50)
    mobile_phone = CharField(max_length=50)
    password = CharField(max_length=50)



