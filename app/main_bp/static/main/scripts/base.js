$(document).ready(function () {
$('.navbar-light .dmenu').hover(function () {
        $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
    }, function () {
        $(this).find('.sm-menu').first().stop(true, true).slideUp(105);
        var all_shown = document.querySelectorAll('.show');
        for (const elem of all_shown){
			elem.classList.remove('show');
		}
    });
});


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


// search for guides
$(document).ready(function(){
  $("#guide-search-input").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#container-of-guides *").filter(function() {
      if (this.classList.contains('guide-container')){
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      }
    });
  });
});

function onAnimationEnd(){
  var sidebar = document.querySelector('#sidebar');
  var toggler = document.querySelector('.fa-toolbox');
  sidebar.classList.toggle('disabled');
  toggler.classList.toggle('disabled');
  sidebar.classList.remove('animate__slideOutLeft');
  console.log(toggler)
}

// toggle of sidebar
function toggleSideBar(){
  var sidebar = document.querySelector('#sidebar');
  var toggler = document.querySelector('.fa-toolbox');

  // if sidebar.classlist.contains(animate__slideOutLeft) then remove that classlist and add the other one.
  if (sidebar.classList.contains('disabled')){
    sidebar.classList.add('animate__slideInLeft');
    sidebar.removeEventListener('animationend',onAnimationEnd)
    sidebar.classList.toggle('disabled');
    toggler.classList.toggle('disabled');


  }
  else {
    sidebar.classList.remove('animate__slideInLeft');
    sidebar.classList.add('animate__slideOutLeft');
    sidebar.addEventListener('animationend',onAnimationEnd)
  }
}



var sidebar_togglers = document.querySelectorAll('.sidebar-drop-toggler')

for (toggler of sidebar_togglers){
  toggler.addEventListener('click',toggleSideBar);
}
