from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', blank=True)
    pass

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=200)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2, default=starting_bid)
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) 
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Listing: {self.title} by {self.seller.username}"

    def get_absolute_url(self):
        return reverse("listing_detail", kwargs={"listing_id": self.id})


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid of ${self.amount} on {self.listing.title} by {self.user.username}"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.listing.title}"
    


class Watchlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlisted_items')  # Links to User model
  listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  # Links to Listing model
  
  def __str__(self):
    return f"Watchlist item: {self.user.username} - {self.listing.title}"
  

