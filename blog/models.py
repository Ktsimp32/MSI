from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    FName = models.CharField(max_length=40, verbose_name="First Name:")
    LName = models.CharField(max_length=40, verbose_name="Last Name:")
    DoB = models.DateField(max_length=8, verbose_name="Date of Birth mm/dd/yy:")
    Gender = models.CharField(max_length=6, verbose_name="Gender Male/Female:")
    Email = models.EmailField(verbose_name="Email:")
    City = models.CharField(max_length=100, verbose_name="City:")
    State = models.CharField(max_length=2, verbose_name="State Abbreviation:")
    Zipcode = models.CharField(max_length=5, verbose_name="Zipcode:")
    StreetAddress = models.CharField(max_length=100, verbose_name="Street Address:")
    PhoneNumber = models.CharField(max_length=14, verbose_name="Phone Number:")

    def __str__(self):
        return self.FName, self.LName

