$(document).ready(function(){    
var form = $('#form_buying_product'); 
console.log(form);
form.on('submit', function(e){
    e.preventDefault();
    var nmb = $("#quantity").val();
    var weigth = $("#weigth").val();   
    var submit_btn = $("#submit_btn");
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data('name');
   

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;  
        data.weigth = weigth;      
        var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val();        
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

            
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                // console.log("OK");
                // console.log(data.products_total_nmb);
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

    // $("#quantity").keyup(function() {
    //     $("#weigth").val($(this).val() * 2);
    // }) 
     

    // $("#weigth").keyup(function() {
    //     $("#quantity").val($(this).val() / 2); 
     
    // }) 

    var timeout = null;
    
    $('.product-number, .product-weight').on('keyup', function() {
        clearTimeout(timeout);        
        var $form = $(this).closest('.product-data');        
        var length = parseFloat($(this).data('length'));         
        var weightItem = parseFloat($(this).data('weight'));      
        var quantity = $form.find('.product-number').val();        
        var totalWeight = $form.find('.product-weight').val();
        
    
        if ($(this).hasClass('product-number')) {
            timeout = setTimeout(function() {
                var multiple = Math.ceil(quantity / length)
                var roundQuantity = multiple * length
                $form.find('.product-number').val(roundQuantity);
                totalWeight = Math.ceil(roundQuantity * weightItem);        
                $form.find('.product-weight').val(totalWeight);
            }, 1000);
        } else {
            timeout = setTimeout(function() {
                quantity = Math.ceil(totalWeight / weightItem );
                console.log(quantity)
                totalWeight = Math.ceil(quantity * weightItem)
                console.log(totalWeight)
                $form.find('.product-number').val(quantity);
                $form.find('.product-weight').val(totalWeight);
            }, 1000);    
        }        
        $form.find('.btn-buy').data('quantity', quantity);
        $form.find('.btn-buy').data('total-price', totalPrice);
    });           
});  

// function roundProductNumber(){
//     var productNumber = document.getElementById("quantity_not_list").value;
//     var productlength = "{{ product.length }}";
//     console.log(productNumber)
//     console.log(productlength)
//     var multiple = Math.ceil(productNumber / productlength)
//     var roundProductNumber = multiple * productlength
//     console.log(roundProductNumber)
//     document.getElementById("quantity_not_list").value = roundProductNumber
// }

// document.getElementById("quantity_not_list").addEventListener("input", roundProductNumber)




