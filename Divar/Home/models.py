from django.db import models
import uuid
from django.contrib.auth.models import User
# from django.conf import settings
class Divar (models.Model):
    category_list = (
    ('TV','Telvision'),('Mobile','Monile'),('Laptop','laptop'),('PC','PC'),('Car','car'),('Camera','Camera'),
    )
    Category = models.CharField(max_length = 100, blank = True, null = True, choices = category_list)

    Picture  =models.ImageField(default = 'default.jpg',blank = True)

    Ad_Titel = models.CharField(max_length = 100, blank = True, null = True)

    Description = models.CharField(max_length = 200, blank = True, null = True)

    city_list = (
    ('Tehran','Tehran'),('Tabriz','Tabriz'),('Mashhad','Mashhad'),('Shiraz','Shiraz'),('Rasht','Rasht'),('Yazd','Yazd'),('Kordestan','Kordestan'),
    )
    City  = models.CharField(max_length = 100, blank = True, null = True, choices = city_list)

    status_list = (
    ('New','New'),('Stock','Stock'),('Broken','Broken'),
    )
    status   = models.CharField(max_length = 100, blank = True, null = True, choices = status_list)

    price    = models.DecimalField(max_digits = 100, decimal_places = 10, default = 'Agreement')

    Phone    = models.IntegerField(blank = True, null=True)

    # Author   = models.CharField (max_length = 100 , blank=True, null=True)

    Author   = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    Date     = models.DateTimeField(auto_now_add=True)

    slug     = models.UUIDField(primary_key=True, default=uuid.uuid4)



    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (self.Category, self.Ad_Titel, self.Description, self.City,
                                            self.status, self.Phone, self.Author, self.Date, self.slug)
