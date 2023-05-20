

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
        alert = document.querySelector('#alert');
        if (alert != null){
          alert.remove();
        }

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
    alert = document.querySelector('#alert');
    if (alert != null){
      alert.remove();
    }
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
  return true;
};


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

    var title = document.querySelector('.title')

    title.after(parentDiv)
  }else{
    return false;
  }
};

//create button for each of the tools that adds them to a list that will be sent with the post request.
// EVENTS
nextBtn.addEventListener('click',nextQuestion);
prevBtn.addEventListener('click',prevQuestion);



// Search of tools

// Selecting
const search_submit_button = document.querySelector('#button-addon3');
const search         = document.querySelector('#search');
const tool_cards           = document.querySelectorAll('.tool-container');
const tool_names           = document.querySelectorAll('.tool-name');
const reset_button         = document.querySelector('#reset_button');
const add_buttons          = document.querySelectorAll('.add_button');
const tools_form_input     = document.querySelector('#tools_input');
var tools_to_submit        = [];
const plus = 'https://img.icons8.com/ios/50/add--v1.png';
const minus = 'https://img.icons8.com/ios/50/minus.png';


// Functions
function getSearchInfo(){
    return search.value.toLowerCase();
}

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

function filterTools(){
  user_input = getSearchInfo();
  if(user_input === ''){
    return false;
  };

  // Get Matches
  matches = [];
  for (var tool of tool_names){
    tool_text = tool.innerHTML
    if (tool_text.toLowerCase() === user_input){
      matches.push(tool);
    }
  }

  // If no results, dont disable anything and just alert
  if (matches.length === 0){
    alert('No matches were found for what you searched!');
    search.value = '';
    return false;
  }

  // Disable all that dont match
  for (var tool of tool_names){
    if(!matches.includes(tool)){
      itsParents = getParents(tool);
      for (var parent of itsParents){
        if(parent.classList.contains('tool-container')){
          parent.classList.add('disabled');
        }
      }
    }
  }
}

function unFilterTools(){
  for(var tool of tool_cards){
    tool.classList.remove('disabled');
  }
}

function getToolId(tool){
  console.log('getid',tool.children[1].innerHTML);
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

// Assinging events
search_submit_button.addEventListener('click',filterTools);
reset_button.addEventListener('click',unFilterTools);

for(var button of add_buttons){
  button.addEventListener('click',addOrRemoveTool);
}


