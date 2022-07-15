
// js code to toggle table dark and light mode
var mode = document.querySelector('.dark-light');
mode.addEventListener('click', table);
function table() {
	let x = document.getElementById('body').className;
	if (x == 'dark') {
		document.getElementById('table').className += ' table-dark';
	}else{
		document.getElementById('table').className = 'table table-sm table-striped';
	}
}
// js code to keep user selected mode even page refresh or file reopen
if(document.getElementById('body').className == 'dark'){
	localStorage.setItem('table', 'table table-sm table-striped table-dark');
	document.getElementById('table').className = localStorage.getItem('table');
}

