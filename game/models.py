from django.db import models


# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name
    

class Game(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=50, null=True)
    game_pic = models.ImageField(blank=True, null=True)
    release_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    