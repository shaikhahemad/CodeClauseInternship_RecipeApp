
console.log("main.js loaded")
$(document).ready(function () {
  $('.menubar').hide()
  $('.menu-toggle').click(function(){
    $('.menubar').toggle()
  });
  var recipes = ['fa-solid fa-bowl-food','fa-solid fa-pizza-slice', 'fa-solid fa-burger']
  var ingredients = ['fa-solid fa-pepper-hot', 'fa-solid fa-lemon', 'fa-solid fa-egg', 'fa-solid fa-carrot', 'fa-solid fa-cheese'];
            var index = 0;

            setInterval(function() {
                $('#ingre').removeClass(ingredients[index]);
                index = (index + 1) % ingredients.length;
                $('#ingre').addClass(ingredients[index]);
            }, 2000);
        setInterval(function() {
                $('#recipe').removeClass(recipes[index]);
                index = (index + 1) % recipes.length;
                $('#recipe').addClass(recipes[index]);
            }, 1500);
});
const scroll = new LocomotiveScroll({
    el: document.querySelector('body'),
    smooth: true
});