from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices
from .models import Listing


def index(request):
    listings = Listing.objects.order_by ('-list_data').filter (is_published=True)
    paginator = Paginator (listings, 6)
    page = request.GET.get ('page')
    paged_listings = paginator.get_page (page)
    context = {
        'listings': paged_listings
    }
    return render (request, 'listings/listings.html', context)


def listing(request, listing_id):

    listing = get_object_or_404 (Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render (request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by ('list_data')
    # keywords
    if 'keywords' in request.GET:
        if keywords := request.GET['keywords']:
            queryset_list = queryset_list.filter (description__icontains = keywords)

    # city
    if 'city' in request.GET:
        if city := request.GET['city']:
            queryset_list = queryset_list.filter (city__iexact=city)

    # State
    if 'state' in request.GET:
        if state := request.GET['state']:
            queryset_list = queryset_list.filter (state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        if bedrooms := request.GET['bedrooms']:
            queryset_list = queryset_list.filter (bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        if price := request.GET['price']:
            queryset_list = queryset_list.filter (price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render (request, 'listings/search.html', context)
