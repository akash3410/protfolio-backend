from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactMessageForm()
            messages.success(request, "Your message has been sent. A response will be sent your email. Thank you!")
            return redirect('/#contact')
        else:
            messages.error(request, "Please correct the message below!")
    else:
        form = ContactMessageForm()

    context = {
        'form': form
    }

    return render(request, 'myapp/index.html', context)