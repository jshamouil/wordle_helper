const letterFields = document.querySelectorAll('.letter-field');
const resultsTableBody = document.querySelector('.results-table tbody');
const clearButton = document.querySelector('.clear-button');
const colorInputs = document.querySelectorAll('.color-field');
let colorData = []; // Array to store color data


// Event listener for input fields
letterFields.forEach((field, index) => {
  field.addEventListener('input', (e) => {
    const inputValue = e.target.value.toUpperCase();
    e.target.value = inputValue; // Ensure the input value is in uppercase
    letterFields[index + 1]?.focus(); // Move focus to the next input field if available
  });

  field.addEventListener('keydown', (e) => {
    if (e.key === 'Backspace' && e.target.value === '') {
      letterFields[index - 1]?.focus(); // Move focus to the previous input field if available
    }
  });

  field.addEventListener('click', (e) => {
    const colors = ['grey', 'yellow', 'green'];
    const currentColor = e.target.dataset.color || 'grey';
    const nextColor = colors[(colors.indexOf(currentColor) + 1) % colors.length];
    e.target.dataset.color = nextColor;
    e.target.style.backgroundColor = nextColor;
    const color = e.target.dataset.color;
    if (color) {
      e.target.classList.toggle(color);
      colorInputs[index].value = e.target.classList.contains(color) ? color : '';
    }
    console.log(e.target.id.concat("-color"))
    const colorBox = e.target.id.concat("-color")
    document.getElementById(colorBox).value = nextColor;
  });


});
