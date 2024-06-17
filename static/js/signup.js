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

function formsubmit(){
    alert("your details has been registered")
}



// adding new fields
function showFields() {
    var selectfield = document.getElementById("idv");
    var selectedValue = selectfield.value;
    // Hide all fields
    document.getElementById('customerFields').style.display = 'none';
    document.getElementById('vendorFields').style.display = 'none';
    // Show fields based on selected value
    if (selectedValue == "Customer") {
        document.getElementById('customerFields').style.display = 'block';
    } else if (selectedValue == "Vendor") {
        document.getElementById('vendorFields').style.display = 'block';
    }
}

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