from django.shortcuts import render, redirect
from markdown2 import Markdown
from django.contrib import messages
from django.http import HttpResponseBadRequest
from random import choice
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
       "entries": util.list_entries()
       })


def markdown_to_html(title):
    content = util.get_entry(title)
    md = Markdown()
    if content is None:
        return None
    else:
        return md.convert(content)


def entry_page(request, title):
  entry_content = markdown_to_html(title)
  if entry_content is None:
    return render(request, "encyclopedia/error.html")
  else:
     return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "content" : entry_content
        })


def search(request):
#   Handles search queries, redirects to entry or search results
  if request.method == "POST":
    query = request.POST['q'].lower()
    matching_entries = [entry.lower() for entry in util.list_entries() if query in entry.lower()]
    if len(matching_entries) == 1:
      return redirect("entry_page", title=matching_entries[0])
    elif matching_entries:
      # Multiple entries with query as substring
      return render(request, "encyclopedia/search.html", {
        "entries": matching_entries,
        "query": query
      })
    else:
      # No entries found
      return render(request, "encyclopedia/error.html", {
        "message": f"No entries found containing '{query}'."
      })
  else:
    # Not a POST request, so probably GET (shouldn't happen for search)
    return render(request, "encyclopedia/error.html", {
      "message": "Invalid search request."
    })
  

def new_entry(request):
  # Renders the 'create.html' template for creating a new entry
  return render(request, "encyclopedia/create.html")


def save_entry(request):
#   Handles form submission for creating a new entry
  if request.method == "POST":
    title = request.POST["title"]
    content = request.POST["content"]
    
    # Check if entry already exists
    if util.get_entry(title) is not None:
      messages.error(request, f"Error: Encyclopedia entry '{title}' already exists!")
      return render(request, "encyclopedia/create.html")  # Re-render form with error message
    else:
      # Save the new entry using util.save_entry(title, content)
      util.save_entry(title, content)
      return redirect("entry_page", title=title)  # Redirect to new entry page
    
  else:
    return redirect("index")


def edit_entry(request, title):
    # Renders the edit page for a specific entry, pre-populated with existing content.
    # Also handles POST requests with edited content for saving.
    if request.method == "GET":
        entry_content = markdown_to_html(title)
        if entry_content is None:
           return render(request, "encyclopedia/error.html")
        else:
            return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry_content
            })
    elif request.method == "POST":
        # Handle editing and saving the content here\
        content = request.POST["content"]
        # Save the edited content using util.save_entry (might require modifications)
        util.save_entry(title, content)  # Adjust arguments/functionality if needed
        return redirect("entry_page", title=title)  # Redirect back to the entry page
        
    else:
        return HttpResponseBadRequest("Invalid request method")  # Handle unexpected methods


def random(request):
   entries = util.list_entries()
   random_entry = choice(entries) if entries else None  # Choose random entry (or None if empty)
   content = markdown_to_html(random_entry)
   return render(request, "encyclopedia/entry.html", {
    "title": entries,
    "content": content
  })