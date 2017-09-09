from django.db import models

class User(models.Model):
    facebook_id = models.BigIntegerField(primary_key=True)
    # friends = models.ManyToManyField()
    name = models.CharField(max_length=100)
    pic = models.CharField(max_length=500)
    high_score = models.IntegerField()

    def __str__(self):
        return str(self.facebook_id) + ' - ' + self.name