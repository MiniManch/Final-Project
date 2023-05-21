

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

// FUNCTIONS
function nextQuestion(){
  if (position != inputs.length){
    // let questions = document.querySelectorAll('input.disabled,select.disabled');
    let questions = document.querySelectorAll('.form-input.disabled');
    let active    = document.querySelector('.active');

    // Here should be a data checker, if empty/data doesn't fit
    if (dataValidator()){
        prevBtn.classList.remove('disabled');

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

        console.log(container.style.width);

      }
    // If its the submit then display-none on the next button
    if (submit.classList.contains('active')){
      nextBtn.classList.add('disabled');
    };
  }
}


function prevQuestion(){
  if (position ==1){
    prevBtn.classList.add('disabled');
  }
  if (position != 0){
    let questions = document.querySelectorAll('.form-input.disabled');
    let active    = document.querySelector('.active');

    // Here should be a data checker, if empty/data doesn't fit

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
  // Changing the Next Button
  if((nextBtn.classList).contains('disabled')){
    nextBtn.classList.remove('disabled');
  }
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

// EVENTS
nextBtn.addEventListener('click',nextQuestion);
prevBtn.addEventListener('click',prevQuestion);

