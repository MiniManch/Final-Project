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
