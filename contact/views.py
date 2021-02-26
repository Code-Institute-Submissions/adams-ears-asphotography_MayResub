from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage

from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            full_name = request.POST.get('full_name', '')
            email = request.POST.get('email', '')
            phone_number = request.POST.get('phone_number', '')
            service = request.POST.get('service', '')
            enquiries = request.POST.get('enquiries', '')
            form.save()

            template = get_template('contact_template.txt')
            context = {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'service': service,
                'enquiries': enquiries
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "https://8000-gold-planarian-sb90yf7a.ws-eu03.gitpod.io/" + '',
                ['adamsearsphotography@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('home')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })

