

//SELECTORS and VARIABLES
const prevBtn = document.querySelector('#prev-btn');
const nextBtn = document.querySelector('#next-btn');
var position = 0;
const inputs  = document.querySelectorAll('.step');
const title = document.querySelector('.title');
const container = document.querySelector('#container-of-all');



// FUNCTIONS
function getParents(element){
    var els = [];
    while (element) {
      if(element.tagName == undefined){
        break;
      }
      els.push(element);
      element = element.parentNode;
  }
  return els;
}


function animatePrevious(){
  container.classList.add('animate__fadeOutLeft');

  container.addEventListener('animationend',function(){
    container.classList.remove('animate__fadeOutLeft')
    container.classList.add('animate__fadeInRight');
      container.addEventListener('animationend',function(){
      container.classList.remove('animate__fadeInRight');
    });
  });
}


function animateNext(){
  container.classList.add('animate__fadeOutRight');
  
  container.addEventListener('animationend',function(){
    container.classList.remove('animate__fadeOutRight');
    container.classList.add('animate__fadeInLeft');
      container.addEventListener('animationend',function(){
      container.classList.remove('animate__fadeInLeft');
    });
  });
};


function changeInterfacePrevious(){
  let questions = document.querySelectorAll('.step.disabled');
  let active    = document.querySelector('.active');


  // Disabling what was the active question
  active.classList.toggle('active');
  active.classList.toggle('disabled');

  // Abling the next disabled question
  question = questions[position-1];
  question.classList.toggle('active');
  question.classList.toggle('disabled');

  position-=1;

}


function changingInterfaceNext(){
  let questions = document.querySelectorAll('.step.disabled');
  console.log(questions)
  let active    = document.querySelector('.active');
  // Disabling what was the active question
  active.classList.toggle('active');
  active.classList.toggle('disabled');

  

  // inabling the next disabled question
  question = questions[position];

  question.classList.toggle('active');
  question.classList.toggle('disabled');

  position+=1;
  console.log(questions,position,active)

}


function nextQuestion(){
  if (position != inputs.length ){
    prevBtn.classList.remove('disabled');
    animateNext()
    setTimeout(changingInterfaceNext,'650');

    // If its the the last step apply disabled class on the next button
    let questions = document.querySelectorAll('.step.disabled');
    if (position == questions.length -1){
      nextBtn.classList.add('disabled')
    }

  }
}


function prevQuestion(){
  if (position ==1){
    prevBtn.classList.add('disabled');
  }
  if (position != 0){
    animatePrevious()
    setTimeout(changeInterfacePrevious,'650');
  }
  // Changing the Next Button
  if((nextBtn.classList).contains('disabled')){
    nextBtn.classList.remove('disabled');
  }
}


// EVENTS
nextBtn.addEventListener('click',nextQuestion);
prevBtn.addEventListener('click',prevQuestion);
