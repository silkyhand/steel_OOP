$(document).ready(function(){
    $('.header').height($(window).height());
   })


$(document).ready(function(){
var form = $('#form_buying_product');
console.log(form);
form.on('submit', function(e){
    e.preventDefault();
    console.log('123');
    var nmb = $("#quantity").val();
    var weigth = $("#weigth").val();
    console.log(nmb);
    console.log(weigth);
    var submit_btn = $("#submit_btn");
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data('name');
    console.log(product_id);
    console.log(product_name);
})
})   



$(document).ready(function() {
    $("#quantity").keyup(function() {
       $("#weigth").val($(this).val() * 2); 
    }); 
});


$(document).ready(function() {
    $("#weigth").keyup(function() {
       $("#quantity").val($(this).val() / 2); 
    }); 
});