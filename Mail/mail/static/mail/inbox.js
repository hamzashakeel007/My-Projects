document.addEventListener('DOMContentLoaded', function() {
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');

});


function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').addEventListener('submit', (event) => {
    event.preventDefault();
     // Extract data from form fields
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    // Prepare request body
    const data = JSON.stringify({ recipients, subject, body });
  
    fetch('/emails', {
      method: 'POST',
      body: data,
    })
      .then(response => response.json())
      .then(result => {
        if (result.message === "Email sent successfully.") {
          alert("Email sent successfully!");
          load_mailbox('sent'); // Load sent mailbox after successful send
        } else {
          console.error('Error sending email:', result.error);
          alert("Error sending email: " + result.error); // Display error details in the alert
        }
      });
  });
}


function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      const emailContainer = document.getElementById('emails-view');

      // Document click listener to hide email view on any click (except email elements)
      document.addEventListener('click', (event) => {
        const emailDiv = event.target.closest('.email');
        if (!emailDiv) {
          document.querySelector('#email-view').style.display = 'none';
        }
      });

      // Render each email
      emails.forEach(email => {
        const emailDiv = document.createElement('div');
        emailDiv.classList.add('email');
        emailDiv.style.border = '1px solid black';  // Add border
        emailDiv.style.padding = '10px';  // Add padding for better readability
        emailDiv.innerHTML = `
          <b style="margin-right: 20px;"> ${email.sender} </b>    ${email.subject} 
          <span style="color: rgba(0, 0, 0, 0.5); float: right;"> ${email.timestamp} </span>
        `;
        
        emailDiv.addEventListener('click', () => {
          load_email(email.id);  // Call new function to load individual email
        });
        emailDiv.style.backgroundColor = email.read ? 'white' : 'gray';
        emailContainer.append(emailDiv);
      });

    });


}


function load_email(email_id) {
  fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email=> {
      // Show email view and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#email-view').style.display = 'block';


      // Mark email as read
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({ read: true }),
      });

      // Display email content
      document.querySelector('#email-view').innerHTML = `
        <b>From:</b> ${email.sender}
        <br>
        <b>To:</b> ${email.recipients.join(', ')}  <br>
        <b>Subject:</b> ${email.subject}
        <br>
        <b>Timestamp:</b> ${email.timestamp}
        <br>
        <hr>
        <p>${email.body}</p>
      `;
      const archiveButton = document.createElement('button');
      archiveButton.textContent = email.archived ? 'Unarchive' : 'Archive';

      archiveButton.addEventListener('click', () => {
        const newArchivedValue = !email.archived;
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({ archived: newArchivedValue }),
        })
        .then(() => {
          load_mailbox('inbox');  // Reload inbox and clear email view
        });
      });
      
      document.querySelector('#email-view').append(archiveButton);


      const replyButton = document.createElement('button');
      replyButton.textContent = 'Reply';

      replyButton.addEventListener('click', () => {
        compose_email();
        const recipient = email.sender; 
        const subject = email.subject.startsWith('Re: ') ? email.subject : `Re: ${email.subject}`;
        const body = `On ${email.timestamp.toLocaleString()}, ${email.sender} wrote: "${email.body}"\nYour reply: `;

        // Redirect to compose view with pre-filled data in form using innerHTML
        const composeView = document.querySelector('#compose-view');
        composeView.style.display = 'block'; // Show compose view

        const recipientInput = composeView.querySelector('#compose-recipients');
        recipientInput.value = recipient;

        const subjectInput = composeView.querySelector('#compose-subject');
        subjectInput.value = subject;

        const bodyTextarea = composeView.querySelector('#compose-body');
        bodyTextarea.value = body;
      });

      document.querySelector('#email-view').append(replyButton);


    });


}


