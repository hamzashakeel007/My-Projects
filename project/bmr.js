
const activeForm = document.getElementById('inputs');
const resultP = document.getElementById('result');

let gender = "male";

function setActive(genderType) {
  gender = genderType;
}

const calculateBtn = document.getElementById('calculate-btn');
calculateBtn.addEventListener('click', () => {
  const weight = parseFloat(document.getElementById('weight').value);
  const height = parseFloat(document.getElementById('height').value);
  const age = parseFloat(document.getElementById('age').value);

  let bmr;
  if (gender === "male") {
    bmr = 10 * weight + 6.25 * height - 5 * age + 5;
  } else if (gender === "female") {
    bmr = 10 * weight + 6.25 * height - 5 * age - 161;
  }

  resultP.textContent = `Your BMR (Mifflin-St Jeor): ${bmr.toFixed(2)} calories per day.`;
});
