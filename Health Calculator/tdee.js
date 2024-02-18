

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
  const activityLevel = parseFloat(document.getElementById('activity-level').value);

  let bmr;
  if (gender === "male") {
    bmr = 10 * weight + 6.25 * height - 5 * age + 5;
  } else if (gender === "female") {
    bmr = 10 * weight + 6.25 * height - 5 * age - 161;
  }

  // Calculate TDEE based on activity level
  const tdee = bmr * activityLevel;

  // Format the output with one decimal place
  const roundedTdee = tdee.toFixed(1);

  // Generate descriptive result message
  let message;
  if (tdee < 1600) {
    message = "Your TDEE is relatively low. Consider increasing your activity level or calorie intake if you feel sluggish.";
  } else if (tdee >= 1600 && tdee < 2400) {
    message = "Your TDEE is within a moderate range. Adjust your calorie intake as needed based on your goals.";
  } else if (tdee >= 2400 && tdee < 3000) {
    message = "Your TDEE is relatively high. Maintain your activity level or reduce calorie intake if aiming for weight loss.";
  } else {
    message = "Your TDEE is very high. Consult a healthcare professional for personalized guidance.";
  }

  // Display the final result
  resultP.textContent = `Your estimated TDEE: ${roundedTdee} calories per day. ${message}`;
});
