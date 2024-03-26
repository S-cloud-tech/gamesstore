from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=200, blank=False, null=True)
    genre = models.CharField(max_length=50, blank=False, null=True)
    game_pic = models.ImageField(blank=True, null=True, upload_to="img/%y")
    release_date = models.DateField( blank=False,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.title
<<<<<<< HEAD
    
=======
    
# class User(models.Model):
#     name = models.CharField(max_length=32, null=True)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
>>>>>>> 35719fdd13481954c13b5cbf9d564d27e27b852f
