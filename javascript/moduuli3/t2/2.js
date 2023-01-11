

//appendchild
 const div = document.querySelector('#target');

    const t = document.createTextNode('First item');  // create text node
    const p = document.createElement('li');
    p.appendChild(t);
    div.appendChild(p);


    const r = document.createTextNode('Second item');  // create text node
    const y = document.createElement('li');
    y.classList.add("my-item")
    y.appendChild(r);
    div.appendChild(y);


    const j = document.createTextNode('Third item');  // create text node
    const g = document.createElement('li');
    g.appendChild(j);
    div.appendChild(g);







