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

$(document).ready( function () {
    $('#myTable').DataTable();
} );

$(document).ready(function() {
    $('.update-btn').on('click', function() {
        var userID = $(this).data('user-id');
        $.ajax({
            type: 'GET',
            url: '/get_user_data/' + userID + '/',
            success: function(response) {
                $('#update-user-id').val(response.UserID); // Set user ID in the hidden input
                $('input[name="firstname"]').val(response.FirstName);
                $('input[name="lastname"]').val(response.LastName);
                $('input[name="email"]').val(response.Username);
                $('input[name="password"]').val(response.Password);
                $('input[name="mobile_no"]').val(response.Mobile_No);
                $('textarea[name="address"]').val(response.Address);
                $('input[name="zip_code"]').val(response.Zipcode);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});



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

// side dropdown
