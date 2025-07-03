from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here. #! models are used in models and saving data this includes things such as name, age, email, etc
class React(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    emailAddress = models.EmailField(max_length=40)