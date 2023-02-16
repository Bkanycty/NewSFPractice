function first_entry_check(){
    let current_url=window.location.search;
    let elem = document.getElementById('notfound');
    current_url == '' ? elem.hidden=true : false;
};
document.addEventListener("DOMContentLoaded", first_entry_check);