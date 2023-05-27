
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


// filter by category

const categories = document.querySelectorAll('.filter-category');
const search     = document.querySelector('#guide-search-input');

function filterByCategory(){
	search.value = this.innerHTML
	var value = this.innerHTML.toLowerCase();
    $("#container-of-guides *").filter(function() {
      if (this.classList.contains('guide-container')){
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      }
    });
}

for (category of categories){
	category.addEventListener('click',filterByCategory);
}


// clear search
const clear_search = document.querySelector('#clear-search');
const guide_containers = document.querySelectorAll('.guide-container');

function clearSearch(){
	search.value = '';
	for (guide of guide_containers){
		 guide.style.display = 'block';
	}
}
if(guide_containers.length != 0){
  clear_search.addEventListener('click',clearSearch);
}


// Search for tools
$(document).ready(function(){
  $("#guide-search-input").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#container-of-tools *").filter(function() {
      if (this.classList.contains('tool-card')){
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      }
    });
  });
});

const tool_container = document.querySelectorAll('.tool-card');

function clearSearchTools(){
  search.value = '';
  for (tool of tool_container){
     tool.style.display = 'block';
  }
}

if (tool_container.length != 0){
  clear_search.addEventListener('click',clearSearchTools);
}

// Search for Items
$(document).ready(function(){
  $("#guide-search-input").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#items-container *").filter(function() {
      if (this.classList.contains('item-card')){
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      }
    });
  });
});


const item_container = document.querySelectorAll('.item-card');

function clearSearchItems(){
  search.value = '';
  for (item of item_container){
     item.style.display = 'block';
  }
}

if (item_container.length != 0){
  clear_search.addEventListener('click',clearSearchItems);
}
