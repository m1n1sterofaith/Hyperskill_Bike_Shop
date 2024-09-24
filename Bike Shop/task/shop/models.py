from django.db import models

class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"

class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"

class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type}"

class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return "basket"

class Bike(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    has_basket = models.BooleanField(default=False, null=False)

    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    bike = models.ForeignKey(Bike,default=None, on_delete=models.CASCADE)

    statuses = [
        ('P', 'pending'),
        ('R', 'ready')
    ]
    status = models.CharField(choices=statuses, max_length=1)


