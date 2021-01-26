from django.db import models

class cloth(models.Model):

    name = models.CharField(max_length=250)
    data_of_purchase = models.DateField()
    brand_of_clothes = models.CharField(max_length=250)
    Cient = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    Name = models.CharField(max_length=250)
    Surname = models.CharField(max_length=250)
    addres = models.DateField()
    data_of_purchase = models.DateTimeField()
    user = models.ForeignKey('cloth',  on_delete=models.CASCADE)



    def __str__(self):
        return self.Name
