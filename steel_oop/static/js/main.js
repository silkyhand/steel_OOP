$(document).ready(function(){    
var form = $('#form_buying_product'); 
console.log(form);
form.on('submit', function(e){
    e.preventDefault();
    var nmb = $("#quantity").val();
    var weigth = $("#weigth").val();
    console.log(nmb);
    console.log(weigth);
    var submit_btn = $("#submit_btn");
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data('name');
    console.log(product_id);
    console.log(product_name);

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;  
        data.weigth = weigth;      
        var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val();        
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

    console.log(data)    
        
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (products_total_nmb) {
                    $("#products_total_nmb").text(data.products_total_nmb);  
                }
            },
            error: function(){
                console.log("error")
            }
        })
    })
});  


$(document).ready(function(){
    $('.header').height($(window).height());

    $("#quantity").keyup(function() {
        $("#weigth").val($(this).val() * 2);
    }) 
     

    $("#weigth").keyup(function() {
        $("#quantity").val($(this).val() / 2); 
     
    }) 
});     