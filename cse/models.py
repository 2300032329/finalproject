from django.db import models

class ContactUs(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True)
    comments = models.CharField(max_length=255)

    class Meta:
        db_table = "contactus"
