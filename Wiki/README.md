## Django Wiki: Encyclopedia Project

This Markdown file outlines the core functionality of the Django-based encyclopedia project.

### Project Overview

- **Purpose:** Create a user-friendly online encyclopedia where users can browse, search, create, and edit entries.
- **Technologies:** Django web framework, Markdown for content formatting.

### Functionality Breakdown

**1. Views and Templates:**

- `index.html`: Displays a list of all encyclopedia entries.
- `entry.html`: Renders the content of a specific entry in HTML format (using Markdown conversion).
- `error.html`: Handles error scenarios like non-existent entries or invalid search queries.
- `create.html`: Provides a form for creating new encyclopedia entries.
- `edit.html`: Allows users to edit existing entries.
- `search.html`: Presents search results based on user queries.

**2. View Functions:**

- `index(request)`: Retrieves and displays all entries from the `util` module.
- `markdown_to_html(title)`: Converts Markdown content to HTML for display.
- `entry_page(request, title)`: Fetches the content of a specific entry and renders it.
- `search(request)`: Handles user search queries, redirecting to entries or displaying search results.
- `new_entry(request)`: Renders the form for creating new entries.
- `save_entry(request)`: Processes form submissions to create new entries or update existing ones.
- `edit_entry(request, title)`: Handles both GET (displaying edit page) and POST (saving edits) requests.
- `random(request)`: Selects a random entry and displays its content.

**3. `util` Module :**

- Provides functions for managing encyclopedia entries, such as:
  - `list_entries()`: Returns a list of all entry titles.
  - `get_entry(title)`: Retrieves the content of a specific entry by title.
  - `save_entry(title, content)`: Saves a new entry or updates an existing one.
  
**4. Markdown Support:**

- The `markdown2` library is used to convert Markdown content stored in entries to HTML for display on the web pages.

**5. User Interactions:**

- Users can browse the list of entries on the index page.
- Clicking on an entry title takes users to the corresponding entry page to view its content.
- A search bar enables users to find entries containing specific keywords.
- Users can create new entries using the provided form.
- Existing entries can be edited through the edit page.
- Clicking the "Random Page" link redirects users to a randomly chosen entry.

**6. Error Handling:**

- Non-existent entries and invalid search queries result in appropriate error messages being displayed.
- The `edit_entry` view function handles unexpected request meth
