from django.db import models

class User(models.Model):
    email                 = models.EmailField(max_length=254)
    password              = models.CharField(max_length=100)
    first_name            = models.CharField(max_length=50)
    last_name             = models.CharField(max_length=50)
    preferred_language    = models.CharField(max_length=50, null=True)
    receive_communication = models.BooleanField(null=True)
    
    class Meta:
        db_table = 'users'
