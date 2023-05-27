

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

function ifToolsSetFooter(){
  href = window.location.href
  if (href.includes('new_step')){
      var toolsText = document.querySelector('#form-container>.active>h3');
      var footer    = document.querySelector('footer');
      if (toolsText.innerHTML == 'TOOLS'){
      footer.classList.add('footer-when-tools');
    }else{
      footer.classList.remove('footer-when-tools');
    }
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

  ifToolsSetFooter()

}


function changingInterfaceNext(){
  let questions = document.querySelectorAll('.form-input.disabled');
  let active    = document.querySelector('.active');
  // Disabling what was the active question
  active.classList.toggle('active');
  active.classList.toggle('disabled');

  

  // inabling the next disabled question
  question = questions[position];

  question.classList.toggle('active');
  question.classList.toggle('disabled');

  position+=1;

  progress.style.width = (position * 50) / questions.length + 5 + '%';

  ifToolsSetFooter()
  
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




// Select tools in New step
var add_buttons          = document.querySelectorAll('.add_button');
var tools_form_input     = document.querySelector('#tools_input');
var tools_to_submit        = [];
var plus = 'https://img.icons8.com/ios/50/add--v1.png';
var minus = 'https://img.icons8.com/ios/50/minus.png';


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

function getToolId(tool){
  return tool.children[1].innerHTML;
}

function addOrRemoveTool(){
  parents = getParents(this);
  for(var parent of parents){
    if(parent.classList.contains('blog-card')){
      parent.classList.toggle('tool_added');
      if (this.children[0].src == plus){
        tools_to_submit.push(getToolId(this));  
        this.children[0].setAttribute('src',minus);
        tools_form_input.value = tools_to_submit.toString();
      }else if(this.children[0].src == minus){
        tools_to_submit.pop(getToolId(this));  
        this.children[0].setAttribute('src',plus);
        tools_form_input.value = tools_to_submit.toString();
      }
    }
  }
}

for(var button of add_buttons){
  button.addEventListener('click',addOrRemoveTool);
}

// Search tools in New Step


// search for guides
$(document).ready(function(){
  $("#guide-search-input").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#container-of-tools *").filter(function() {
      if (this.classList.contains('tool-container')){
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      }
    });
  });
});




