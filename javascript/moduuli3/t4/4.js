'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let i of students) {
  let ul = document.getElementById('target');
  let op = document.createElement('option');
  let name = document.createTextNode(i.name)
  op.appendChild(name);
  op.value = i.id;
  ul.appendChild(op);
}

