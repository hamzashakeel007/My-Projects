from django import forms
from .models import Listing, Bid, Comment, Category

class ListingForm(forms.ModelForm):
    category = forms.CharField(label="Category", required=False)

    def clean_category(self):
        data = self.cleaned_data['category']
        if data:
            try:
                # Check for existing category
                category = Category.objects.get(name=data)
                return category
            except Category.DoesNotExist:
                # Create a new category if it doesn't exist
                new_category = Category.objects.create(name=data)
                return new_category
        else:
            return None  # Allow leaving category blank
        
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
