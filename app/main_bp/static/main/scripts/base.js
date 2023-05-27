


const stars = document.querySelectorAll('.no-color');


function changeColorRating(){
  stars_array = Array.from(stars)
  for (let x = 0; x-1 < stars_array.indexOf(this); x++){
    stars_array[x].classList.add('rating-color');
  }
}

function removeColorRating(){
  for(star of stars){
    if(star.classList.contains('star-clicked-on')){
      continue;
    }else{
      star.classList.remove('rating-color');
    }
  }
}


function selectRating(){
  var stars_array = Array.from(stars);
  var index = stars_array.indexOf(this);
  for (star of stars){
    star.removeEventListener('mouseout',removeColorRating);
    star.classList.remove('star-clicked-on');
    star.classList.remove('rating-color');


    if (stars_array.indexOf(star) > index){
      star.addEventListener('mouseout',removeColorRating);
    }
    else{
      star.classList.add('rating-color');
      star.classList.add('star-clicked-on');
    }
    var ratings_input = document.querySelector('#rating-input');
    var clicked_on_stars = Array.from(document.querySelectorAll('.star-clicked-on'));
    if (ratings_input!= null){
      ratings_input.value = clicked_on_stars.length
      console.log(ratings_input.value)
    }
  }

  // remove the event listeners of mouse out, but if you hover over 2 stars and its 3 stars clicked on i
}

for (star of stars){
  console.log(stars)
  star.addEventListener('mouseover',changeColorRating);
  star.addEventListener('mouseout',removeColorRating);
  star.addEventListener('click',selectRating)

}


// Sidebar open and close

function onAnimationEnd(){
  var sidebar = document.querySelector('#sidebar');
  var toggler = document.querySelector('.fa-toolbox');
  toggler.classList.toggle('disabled');
  sidebar.classList.toggle('disabled');
  sidebar.classList.remove('animate__slideOutLeft');
}

function toggleSideBar(){
  var sidebar = document.querySelector('#sidebar');
  var toggler = document.querySelector('.fa-toolbox');

  // if sidebar.classlist.contains(animate__slideOutLeft) then remove that classlist and add the other one.
  if (sidebar.classList.contains('disabled')){
    sidebar.classList.add('animate__slideInLeft');
    sidebar.classList.toggle('disabled');
    toggler.classList.toggle('disabled');


  }
  else {
    sidebar.classList.remove('animate__slideInLeft');
    sidebar.classList.add('animate__slideOutLeft');
    setTimeout(onAnimationEnd,'700');
  }
}


var sidebar_togglers = document.querySelectorAll('.sidebar-drop-toggler')

for (toggler of sidebar_togglers){
  toggler.addEventListener('click',toggleSideBar);
}

// animate icons inside navbar
var icons = document.querySelectorAll('.nav-link.link-dark');

function toggleBounce(){ 
  if (this.children[1].tagName == 'I'){
    this.children[1] .classList.toggle('fa-bounce');
  }
}

for (icon of icons){
  icon.addEventListener('mouseover',toggleBounce);
  icon.addEventListener('mouseout',toggleBounce);

}


// Change sidebar toggler color after scroll only on index page
var sidebar_toggler = document.querySelector('.sidebar-drop-toggler')
var path = window.location.pathname;

function changeTogglerColor(){
  console.log(sidebar_toggler.classList.contains('changed-navbar-toggler') && $(window).scrollTop() > screen.height);
  if (path == '/'){
    if(sidebar_toggler.classList.contains('changed-navbar-toggler') && $(window).scrollTop() < screen.height-10){
      sidebar_toggler.classList.toggle('changed-navbar-toggler');
    }
    else if (!sidebar_toggler.classList.contains('changed-navbar-toggler') && $(window).scrollTop() > screen.height){
      sidebar_toggler.classList.toggle('changed-navbar-toggler');
    }
  }
}

window.onscroll = function() {changeTogglerColor()};


// Hover Store on homepage
var store_jumbo = document.querySelector('#homepage-store-jumbo');

function addAnimationToStore(){
  this.classList.add('animate__heartBeat');
  
}

function removeAnimationToStore(){
  this.classList.remove('animate__heartBeat');
}

if (store_jumbo != null){
  store_jumbo.addEventListener('mouseover',addAnimationToStore);
  store_jumbo.addEventListener('mouseout',removeAnimationToStore);
}
