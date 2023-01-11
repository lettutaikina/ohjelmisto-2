const button = document.getElementById('start');
button.addEventListener('click', calculate);

function calculate() {
  let num1 = parseFloat(document.getElementById('num1').value);
  let num2 = parseFloat(document.getElementById('num2').value);
  let operation = document.getElementById('operation').value;
  const p = document.getElementById('result');
  switch (operation) {
    case 'add':
      p.innerText = (num1 + num2).toString();
      break;
    case 'sub':
      p.innerText = (num1 - num2).toString();
      break;
    case 'multi':
      p.innerText = (num1 * num2).toString();
      break;
    case 'div':
      p.innerText = (num1 / num2).toString();
      break;
  }
}
