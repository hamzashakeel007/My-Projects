const button1 = document.getElementById('button1');
const button2 = document.getElementById('button2');

button1.addEventListener('click', () => {
  button1.classList.add('active');
  button2.classList.remove('active');
});

button2.addEventListener('click', () => {
  button2.classList.add('active');
  button1.classList.remove('active');
});
