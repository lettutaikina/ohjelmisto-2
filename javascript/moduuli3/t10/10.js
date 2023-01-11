
const fname = document.querySelector('input[name=firstname]');
const lname = document.querySelector('input[name=lastname]');
const p = document.querySelector('p');

const button = document.getElementById('source');

button.addEventListener('click', function(evt) {
    evt.preventDefault();
    p.innerText = `Your name is ${fname.value} ${lname.value}`;
});