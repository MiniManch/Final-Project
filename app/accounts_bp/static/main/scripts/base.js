


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
    }
  }

  // remove the event listeners of mouse out, but if you hover over 2 stars and its 3 stars clicked on i
}

for (star of stars){
  star.addEventListener('mouseover',changeColorRating);
  star.addEventListener('mouseout',removeColorRating);
  star.addEventListener('click',selectRating)

}


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
  console.log(this.children[1].tagName)
  if (this.children[1].tagName == 'I'){
    this.children[1] .classList.toggle('fa-bounce');
  }
}

for (icon of icons){
  icon.addEventListener('mouseover',toggleBounce);
  icon.addEventListener('mouseout',toggleBounce);

}

// Animate How botton border on homepage

var how = document.querySelector('#how');
var how_span = document.querySelector('how-span');

function addEffectToHow(){
  how_span.classList.add('animate__zoomIn');
  
  how_span.addEventListener('animationend',function(){
    how_span.classList.remove('animate__zoomIn');
    how_span.classList.add('how');
  });
}

function removeEffectToHow(){
  how_span.classList.add('animate__zoomOut');
  
  how_span.addEventListener('animationend',function(){
    how_span.classList.remove('animate__zoomOut');
    how_span.classList.remove('how');
  });
}

how.addEventListener("mouseover",addEffectToHow);
how.addEventListener('mouseout',removeEffectToHow);