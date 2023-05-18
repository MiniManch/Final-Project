

//SELECTORS and VARIABLES
const form    = document.querySelector('#regForm');
const name = document.querySelector('#name');
const usage = document.querySelector('#usage');
const submit = document.querySelector('#submit');
const image  = document.querySelector('#image');
const prevBtn = document.querySelector('#prev-btn');
const nextBtn = document.querySelector('#next-btn');
var position = 0;
const inputs  = document.querySelectorAll('#container>input');
const progress = document.querySelector('#progress-bar');

// FUNCTIONS
function nextQuestion(){
  if ((position+1) != inputs.length){
    let questions = document.querySelectorAll('input.disabled,div.disabled');
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

        progress.style.width = (position * 50) / questions.length + '%';
        console.log(progress);
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
    let questions = document.querySelectorAll('input.disabled,div.disabled');
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
  let active    = document.querySelector('.active');

  if(active.type == 'file'){
    var validFileExtensions = ["jpg", "jpeg", "png"];    

    filename = active.value ;
    if (filename.length > 0){
      extensionName = filename.split('.');
      extensionName = extensionName[extensionName.length - 1];
      if (!validFileExtensions.includes(extensionName)){
        alert('File type must be jpg,jpeg or png, please upload a different file.')
        return false;
      }
    }
  }

  else if(active.type == 'text'){
    text = active.value;
    active.value = text.replace( '/[^\x20-\x7E]+/g', '' );
    if (active.value.length == 0){
      alert('This is a mandatory field.')
      return false;
    }
    
  } 
  
  return true;
}

// EVENTS
nextBtn.addEventListener('click',nextQuestion);
prevBtn.addEventListener('click',prevQuestion);





// create step checker variable DONE
// if were on step one no back button.
// if were on last step no next button but submit button DONE

// create data validator function
// create next question function DONE
// create previous question function DONE
// create shaker just like they did it was awesome probably should just copy that
// create progress bar
