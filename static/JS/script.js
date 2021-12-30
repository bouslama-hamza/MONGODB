window.onscroll = function() {myFunction()};
var header = document.getElementById("myHeader");
var sticky = header.offsetTop;
var nav_bar_1 = document.querySelector("#nav_bar_1")
var nav_bar_2 = document.querySelector("#nav_bar_2")
var nav_bar_3 = document.querySelector("#nav_bar_3")
var nav_bar_4 = document.querySelector("#nav_bar_4")

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    nav_bar_1.style.color = 'black'
    nav_bar_2.style.color = 'black'
    nav_bar_3.style.color = 'black'
    nav_bar_4.style.color = 'black'
  } else {
    header.classList.remove("sticky");
    nav_bar_1.style.color = 'white'
    nav_bar_2.style.color = 'white'
    nav_bar_3.style.color = 'white'
    nav_bar_4.style.color = 'white'
  }
}
var slides = document.querySelectorAll('.slide');
var btns = document.querySelectorAll('.btn');
let currentSlide = 1;

let change = document.getElementById("change")

setInterval(() => {
  x = Math.floor((Math.random()*5)+1)
  change.src = `../static/images/service/${x}.jpg`
}, 3000);
