# from twpn.views import bhaktapur
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

districts = (
    ('Kathmandu', 'Kathmandu'),
    ('Lalitpur', 'Lalitpur'),
    ('Bhaktapur', 'Bhaktapur')
)

# Create your models here.
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=100)
    vendor_district = models.CharField(max_length=15, choices=districts)
    vendor_email = models.EmailField(max_length=250)
    vendor_contact = models.BigIntegerField()
    vendor_desc = models.CharField(max_length=150)
    vendor_user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.vendor_name

    def get_absolute_url(self):
        # return reverse('dashboard', args=(str(self.id)))
        return reverse('dashboard')

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=250)
    user_serviceDate = models.DateField()
    review = models.CharField(max_length=1000)
    def __str__(self):
        return self.user_name + ' to ' + self.vendor_name

class Images(models.Model):
    vendor_id = models.ForeignKey(Vendor, null= True, on_delete=models.SET_NULL)
    image_id = models.AutoField(primary_key=True)
    image_descName = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images/")
    def __str__(self):
        return self.image_descName

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    service_name = models.CharField(max_length=100)
    service_price = models.FloatField()
    service_desc = models.CharField(max_length=250)
    def __str__(self):
        return self.service_name + ' ' + str(self.vendor_id)

    def get_absolute_url(self):
        # return reverse('dashboard', args=(str(self.id)))
        return reverse('dashboard')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()
    email = models.EmailField(max_length=250)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name


class MembershipForm(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    bname = models.CharField(max_length=50)
    weburl = models.URLField()
    email = models.EmailField(max_length=250)
    contact = models.BigIntegerField()
    district = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    msg = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Membership Request from ' + self.bname

class QuoteRequest(models.Model):
    vendor_id = models.PositiveSmallIntegerField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    contact = models.BigIntegerField()
    msg = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Quote requested by ' + self.fname + ' for ' + str(self.vendor_id)