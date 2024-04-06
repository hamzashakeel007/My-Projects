from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Listing, Watchlist, Category
from .forms import ListingForm, BidForm, CommentForm
from .models import User
from django.db.models import F


def index(request):
    # Filter active listings
    active_listings = Listing.objects.filter(active=True)

    context = {'active_listings': active_listings}
    return render(request, 'auctions/index.html', context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)  # Don't save yet to assign seller
            new_listing.seller = request.user  # Assign current user as seller
            new_listing.current_price = form.cleaned_data['starting_bid']
            new_listing.title= form.cleaned_data['title']
            new_listing.description= form.cleaned_data['description']
            new_listing.category= form.cleaned_data['category']
            new_listing.image_url= form.cleaned_data['image_url']
            new_listing.save()
            return redirect('listing_detail', listing_id=new_listing.id) # Redirect to desired page after successful creation
    else:
        form = ListingForm()

    context = {"form": form}
    return render(request, "auctions/create_listing.html", context)
  

@login_required
def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    bids = listing.bids.all().order_by('-placed_at')
    comments = listing.comments.all().order_by('-created_at')
    highest_bid = bids.first()

    if highest_bid:
        highest_bidder_username = highest_bid.user.username  # Access username of user who placed highest bid
    else:
        highest_bidder_username = None
    
    # Handle different POST requests based on user actions
    if request.method == 'POST':
        close_listing(request, listing_id)
        place_bid(request, listing_id)
        add_comment(request, listing_id)

    image_url = listing.image_url  
    # Prepare context for the template
    bid_form = BidForm()
    comment_form = CommentForm()

    return render(request, 'auctions/listing_detail.html', {
        'listing': listing,
        'bids': bids,
        'comments': comments,
        'bid_form': bid_form,
        'comment_form': comment_form,
        'highest_bidder_username': highest_bidder_username,
        'image_url': image_url 
    })


@login_required
def close_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if listing.seller == request.user and listing.active:
        listing.active = False
        listing.save()
        return redirect('index')
    else:
        return HttpResponse("You cannot close this listing.")
    

@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == 'POST':
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            new_bid = bid_form.save(commit=False)
            new_bid.user = request.user
            new_bid.listing = listing
            if new_bid.amount > listing.current_price:
                new_bid.save()
                listing.current_price = new_bid.amount
                listing.save()
                return redirect('listing_detail', listing_id=listing.id)
            else:
                # Handle error: bid is lower than current price
                # listing.bids.all().order_by('-placed_at') -> Order bids in descending / the last highest bid
                return render(request, 'auctions/listing_detail.html', {
                    'listing': listing, 
                    'bids': listing.bids.all().order_by('-placed_at'), 
                    'comments': listing.comments.all().order_by('-created_at'), 
                    'bid_error': 'Bid must be higher than current price.',
                    })
        
    return redirect('listing_detail', listing_id=listing_id)  # Redirect on GET requests or invalid forms


@login_required
def add_comment(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.listing = listing
            new_comment.save()
            return redirect('listing_detail', listing_id=listing.id)
    return redirect('listing_detail', listing_id=listing_id)  # Redirect on GET requests or invalid forms


@login_required
def watchlist(request):
    if request.method == 'POST':
        try:
            listing_id = request.POST.get('listing_id')  # hidden field with listing ID
            listing = Listing.objects.get(pk=listing_id)
            if not Watchlist.objects.filter(user=request.user, listing=listing).exists():
                Watchlist.objects.create(user=request.user, listing=listing)
                messages.add_message(request, messages.SUCCESS, f"{listing.title} Listing added to watchlist.")

            else:
                messages.add_message(request, messages.INFO, f"{listing.title} Listing already exists in your watchlist.")
            return redirect('watchlist')  # Redirect back to listing detail
        except (Listing.DoesNotExist, ValueError):
            pass  # Handle potential errors (optional)

    # Retrieve and display the watchlist if not a POST request
    user_watchlist = Watchlist.objects.filter(user=request.user)
    listings = Listing.objects.filter(pk__in=[watchlist.listing.id for watchlist in user_watchlist])
    context = {'listings': listings}
    return render(request, 'auctions/watchlist.html', context)

    
@login_required
def remove_from_watchlist(request, listing_id):
  if request.method == 'POST':
    listing = Listing.objects.get(pk=listing_id)
    watchlist_item = Watchlist.objects.get(user=request.user, listing_id=listing_id)
    watchlist_item.delete()
    messages.add_message(request, messages.SUCCESS, f"{listing.title} Listing successfully removed from watchlist.")
    
    return redirect('watchlist')  # Redirect back to watchlist
  
  else:
    return redirect('watchlist')  # Handle non-POST requests 
  

@login_required
def my_listings(request):
    user_listings = request.user.listings.all()  # Get current user's listings
    context = {'listings': user_listings}
    return render(request, 'auctions/my_listings.html', context)


@login_required
def categories(request):
    categories = Category.objects.annotate( c=F('name')).values('name').distinct()

    context = {
        'categories': categories,
    }
    return render(request, 'auctions/categories.html', context)


@login_required
def category_listings(request, category):
    category = Category.objects.get(name=category)
    active_listings = Listing.objects.filter(active=True, category=category)

    context = {
        'category': category,
        'listings': active_listings,
    }
    return render(request, 'auctions/category_listings.html', context)
