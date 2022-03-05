from django.shortcuts import redirect ,render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car plase wait untel we get back to you')
                return redirect('/cars/'+car_id)

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            car_id=car_id,
            car_title=car_title,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New Car Inquiry',
            f'You have a new inquiry for the {car_title} car. Plase login to your admin panel for more info.',
            'myproject.10526@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly')
        return redirect('')

