from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method != 'POST':
        return
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
    if request.user.is_authenticated:
        user_id = request.user.id
        if has_contacted := Contact.objects.all().filter(
            listing_id=listing_id, user_id=user_id
        ):
            messages.error (request, 'You have already made an inquiry for this listing')
            return redirect(f'/listings/{listing_id}')

    contact = Contact (listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                       user_id=user_id)

    contact.save ()

        # Send email
    send_mail(
        'Property Listing Inquiry',
        f'There has been an inquiry for {listing}. Sign into the admin panel for more info',
        'webdevhimanshu@gmail.com',
        [realtor_email, 'coderhimanshugupta@gmail.com'],
        fail_silently=False,
    )


    messages.success (request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect(f'/listings/{listing_id}')
