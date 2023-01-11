let p = document.querySelector('p');
let img = document.querySelector('img')
p.addEventListener('mouseover', function (evt) {
    img.src = "img/picB.jpg"
});

p.addEventListener('mouseout', function (evt) {
    img.src = "img/picA.jpg"
});

