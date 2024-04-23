# Mail 

This single-page web application implements an email service, featuring:

* Inbox view displaying email summaries
* Individual email view
* Compose view for creating new emails (with pre-filling functionality for reply)
* Visual distinction between read and unread emails

## Features

* Leverages HTML, CSS, and JavaScript for a dynamic user interface.
* Utilizes a project-specific API for email data interaction.
* Provides functionalities for viewing, composing, and replying to emails.

## Setup

**Prerequisites:**

* A web server (e.g., Python's built-in `http.server` module)
* A project-specific API for handling email data

1. Clone this repository.
2. Install any required dependencies (if applicable).
3. Configure and run your project-specific API.
4. Start the web server and navigate to the project's root directory in your browser.

## Usage

* The application provides buttons for navigating between Inbox, Compose, Sent, and Archived views.
* Clicking on an email in the Inbox view displays its details.
* The Compose view allows you to create new emails.

**Note:**

* Reply functionality leverages pre-filling the recipient, subject, and body fields in the compose view but might require additional logic in your project's API for handling reply actions.


## Technology Stack

* Django
* HTML
* CSS
* JavaScript

## Contribution

Feel free to fork this repository and contribute improvements or additional features!
