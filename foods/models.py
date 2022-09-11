from django.db import models

class Restaurant(models.Model) :
    safe_id = models.IntegerField(null=True)
    region = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    land_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length = 30,null=True)
    res_number = models.CharField(max_length=15)
    xpos = models.FloatField()
    ypos = models.FloatField()

    def __str__(self) :
        return (f"{self.id}번 : {self.title}")
    
class check(models.Model) :
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    