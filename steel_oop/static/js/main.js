$(document).ready(function(){
    $('.header').height($(window).height());
   })


$(document).ready(function(){
var form = $('#form_buying_product');
console.log(form);
form.on('submit', function(e){
    e.preventDefault();
    console.log('123');
})
})   