from django.shortcuts import render, redirect
from django.contrib import messages
from .models import subscriber

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed!')
        else:
            subscriber = subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')