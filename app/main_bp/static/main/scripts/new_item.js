
//SELECTORS and VARIABLES
const form    = document.querySelector('#regForm');
const subject = document.querySelector('#subject');
const description = document.querySelector('#description');
const submit = document.querySelector('#submit');
const image  = document.querySelector('#image');
const prevBtn = document.querySelector('#prev-btn');
const nextBtn = document.querySelector('#next-btn');
var position = 0;
const inputs  = document.querySelectorAll('.form-control');
const progress = document.querySelector('#progress-bar');
const title = document.querySelector('.title');
const nav = document.querySelector('nav');
const container = document.querySelector('#container-of-all');
var guide_form_input     = document.querySelector('#guide_input');



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


function dataValidator(){
  let active    = document.querySelector('.active').children[1];

  if(active.type == 'file'){
    var validFileExtensions = ["jpg", "jpeg", "png"];    

    filename = active.value ;
    if (filename.length > 0){
      extensionName = filename.split('.');
      extensionName = extensionName[extensionName.length - 1];
      if (!validFileExtensions.includes(extensionName)){
        console.log(extensionName);
        alertMessage('File type must be jpg,jpeg or png, please upload a different file.')
        return false;
      }
    }
  }
  else if(active.type == 'text'){
    text = active.value;
    active.value = text.replace( '/[^\x20-\x7E]+/g', '' );
    if (active.value.length == 0){
      alertMessage('This is a mandatory field.')
      return false;
    }
  } 
  else if(active.id == 'category'){
    if (active.value == '-Category-'){
      alertMessage('This is a mandatory field.')
      return false;
    }
  }
  else if(active.id == 'search-and-filter'){
    if(guide_form_input.value == ''){
      alertMessage('This is a mandatory field.')
      return false;
    }
  }
  return true;
}


function alertMessage(message){
  alert = document.querySelector('#alert');

  if (alert == null){
    parentDiv = document.createElement('div');
    parentDiv.id = 'alert';

    parentDiv.className = ('alert alert-warning alert-dismissible fade show');
    parentDiv.setAttribute('role','alert')

    text = document.createTextNode(message);

    button = document.createElement('button');
    button.classList.add('btn-close');
    button.setAttribute('data-bs-dismiss','alert');
    button.setAttribute('aria-label','Close');

    parentDiv.appendChild(text);
    parentDiv.appendChild(button);


    title.after(parentDiv)
  }else{
    return false;
  }
};


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
  let questions = document.querySelectorAll('.form-input.disabled');
  let active    = document.querySelector('.active');


  // Disabling what was the active question
  active.classList.toggle('active');
  active.classList.toggle('disabled');

  // Abling the next disabled question
  question = questions[position-1];
  question.classList.toggle('active');
  question.classList.toggle('disabled');

  position-=1;
  progress.style.width = (position * 50) / questions.length + '%';
}


function changingInterfaceNext(){
  let questions = document.querySelectorAll('.form-input.disabled');
  let active    = document.querySelector('.active');
  // Disabling what was the active question
  active.classList.toggle('active');
  active.classList.toggle('disabled');

  // Here should be a checker if its submit button there shouldn't be a next button

  // inabling the next disabled question
  question = questions[position];

  question.classList.toggle('active');
  question.classList.toggle('disabled');

  position+=1;

  progress.style.width = (position * 50) / questions.length + 5 + '%';
}


function nextQuestion(){
  if (position != inputs.length && dataValidator() ){
    prevBtn.classList.remove('disabled');
    animateNext()
    setTimeout(changingInterfaceNext,'650');

    // If its the submit then display-none on the next button
    imageParents = getParents(image)
    for (parent of imageParents){
      if (parent.classList.contains('active')){
      nextBtn.classList.add('disabled');

      }
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



// Select guides in New Item
var add_buttons          = document.querySelectorAll('.add_button');
var guide_form_input     = document.querySelector('#guide_input');
var plus = 'https://img.icons8.com/ios/50/add--v1.png';
var minus = 'https://img.icons8.com/ios/50/minus.png';
var guide_cards = document.querySelectorAll('.blog-card');

function getGuideId(guide){
  return guide.children[1].innerHTML;
}

function addOrRemoveGuide(){
  parents = getParents(this);
  for(var parent of parents){
    if(parent.classList.contains('blog-card')){
      parent.classList.toggle('guide_added');
      if (this.children[0].src == plus){
        this.children[0].setAttribute('src',minus);
        guide_form_input.value = getGuideId(this).toString();

        for (guide of guide_cards){
          if(!guide.classList.contains('guide_added')){
            guide.classList.add('disabled-guide');         
          }
        }
      }
      else if(this.children[0].src == minus){
        guide_form_input.value = '';
        this.children[0].setAttribute('src',plus);

        for (guide of guide_cards){
          if(guide.classList.contains('disabled-guide')){
              guide.classList.remove('disabled-guide');         
          }
        }
      }
    }
  }
}

for(var button of add_buttons){
  button.addEventListener('click',addOrRemoveGuide);
}
