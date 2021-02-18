from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm


def contact(request):
    form = ContactForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Form sent successfully')

    else:
        messages.error(request, 'Form failed to send.'
                       'Please ensure the form is valid.')

    return render(request, 'contact/contact.html', {'form': form})
