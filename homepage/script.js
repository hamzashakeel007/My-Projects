

const form = document.getElementById("myForm");
const response = document.getElementById("response");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent default form submission

  const message = document.getElementById("message").value;
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  // Do something with the data, e.g., send it to a server
  console.log("Message:", message);
  console.log("Name:", name);
  console.log("Email:", email);

  response.textContent = "Message and contact information submitted successfully!";
  form.reset(); // Clear the form fields
});
