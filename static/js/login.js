//my account dropdown
$(document).ready(function(){
    $(".drop").click(function(){
        $(".dropdown").toggle()
    });
});

// side dropdown
$(document).ready(function(){
    $(".side").click(function(){
        $(".side_dropdown").toggle()
    });
});



// autocomplete search

$(document).ready(function() {
    var data = [
        {label: 'art & photography', value: 'art_&_photography'},
        {label: 'Biographies & Memoirs', value: 'Biographies_&_Memoirs'},
        {label: 'Dictionaries & Language', value: 'Dictionaries_&_Language'},
        {label: 'Fiction', value: 'Fiction'},
        {label: 'Society', value: 'Society'},
        {label: 'law', value: 'law'},
        {label: 'medicine', value: 'medicine'},
        {label: 'new arrivals', value: 'new_arrivals'},
        {label: 'box sets', value: 'box_sets'},
        {label: 'best seller', value: 'best_seller'},
        {label: 'fiction books', value: 'fiction_books'},
        {label: 'award winners', value: 'award_winning'},
        {label: 'featured authors', value: 'featured_authors'},
        {label: 'todays deals', value: 'todays_deals'}
    ];
    

    $("input#autocomplete").autocomplete({
        source: data,
        focus: function (event, ui) {
            $(event.target).val(ui.item.label);
            return false;
        },
        select: function (event, ui) {
            $(event.target).val(ui.item.label);
            var url = '/' + ui.item.value.replace(/ /g, '_');
            window.location.href = url;
            return false;
        }
    });
    $("#searchButton").on("click", function() {
        var searchValue = $("#autocomplete").val();
        var url = '/' + searchValue.replace(/ /g, '_');
        window.location.href = url;
    });
});



document.getElementById('usertype').addEventListener('change', function() {
    var userType = this.value;
    var usernameField = document.getElementById('username');
    var passwordField = document.getElementById('password');
    var usernameFieldid = document.getElementById('usernameid');
    var passwordFieldid = document.getElementById('passwordid');

    if (userType === 'Admin') {
        usernameField.style.display = 'none';
        passwordField.style.display = 'none';
        usernameFieldid.style.display = 'none';
        passwordFieldid.style.display = 'none';
    }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    var userType = document.getElementById('usertype').value;
    if (userType === 'Admin') {
        event.preventDefault();
        window.location.href = 'http://127.0.0.1:8000/admin/login/?next=/admin/';
    }
});