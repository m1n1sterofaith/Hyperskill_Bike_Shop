from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from shop.models import Bike, Order, Basket
from shop.forms import OrderForm

def bikes_view(request):
    template = 'bikes.html'
    bikes = Bike.objects.all()
    context = {'bikes': bikes}
    return render(request, template, context=context)

class OrderCreateView(View):
    def get(self, request, pk, *args, **kwargs):
        bike = get_object_or_404(Bike, id=pk)
        order_form = None
        can_order = bike.frame.quantity > 0 and bike.tire.quantity > 0 and bike.seat.quantity > 0

        if can_order:
            order_form = OrderForm()

        return render(request, 'bikedetails.html',
                      {'bike': bike, 'can_order': can_order, 'order_form': order_form})

    def post(self, request, pk, *args, **kwargs):
        bike = get_object_or_404(Bike, id=pk)
        form = OrderForm(request.POST)
        basket = Basket
        if form.is_valid():
            order = form.save(commit=False)
            order.bike = bike
            order.save()
            bike.seat.quantity -= 1
            bike.frame.quantity -= 1
            bike.tire.quantity -= 2
            bike.save()
            bike.seat.save()
            bike.tire.save()
            bike.frame.save()
            if bike.has_basket:
                basket = get_object_or_404(Basket)
                basket.quantity -= 1
                basket.save()
            return redirect(reverse('order_success', args=[order.id]))
        return render(request, 'bikedetails.html', {'form': form})

def order_success_view(request, order_number):
    return render(request, 'order.html', {'order_number': order_number})