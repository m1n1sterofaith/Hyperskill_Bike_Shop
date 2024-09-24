from django.contrib import admin
from shop.models import Frame
from shop.models import Seat
from shop.models import Tire
from shop.models import Basket
from shop.models import Bike
from shop.models import Order

admin.site.register(Frame)
admin.site.register(Seat)
admin.site.register(Tire)
admin.site.register(Basket)
admin.site.register(Bike)
admin.site.register(Order)

