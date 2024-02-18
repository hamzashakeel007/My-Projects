
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

  let bmi;
  if (gender === "male") {
    bmi = weight / (height / 100) ** 2;
  } else if (gender === "female") {
    bmi = 0.9 * weight / (height / 100) ** 2; // Gender-specific formula for females
  }

  let interpretation;
  if (bmi < 18.5) {
    interpretation = 'Underweight';
  } else if (bmi >= 18.5 && bmi < 25) {
    interpretation = 'Healthy weight';
  } else if (bmi >= 25 && bmi < 30) {
    interpretation = 'Overweight';
  } else {
    interpretation = 'Obese';
  }

  resultP.textContent = `Your BMI is: ${bmi.toFixed(2)}. Interpretation: ${interpretation}`;
});
