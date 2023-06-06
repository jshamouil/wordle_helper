const letterFields = document.querySelectorAll('.letter-field');

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
  });

});
