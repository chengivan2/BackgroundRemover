from django.db import models

# Create your models here.
class Feedback(models.Model):
    email_address = models.EmailField(max_length = 254)
    feedback_text = models.CharField(max_length=200)
