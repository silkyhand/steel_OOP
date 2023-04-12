$(document).ready(function(){    
    var $button = $('.product'); 
    console.log($button);
    $button.on('submit', function(e){
        e.preventDefault();
        var nmb = $("#quantity").val();
        var weight = $button.find("#weight").val();
        console.log(nmb);
        console.log(weight);
        var submit_btn = $("#submit_btn");
        console.log(submit_btn);
        var product_id = submit_btn.data('product_id');       
        var product_name = submit_btn.data('name');        
        var url = $button.attr("action");
        console.log(url)

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;  
        data.weight = weight;      
        var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val();        
        data["csrfmiddlewaretoken"] = csrf_token;
        
            
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
                totalWeight = Math.ceil(multiple* weightItem);        
                $form.find('.product-weight').val(totalWeight);
            }, 1800);
        } else {
            timeout = setTimeout(function() {
                quantityItem = Math.ceil(totalWeight / weightItem);
                quantityMetr = quantityItem * length
                totalWeight = Math.ceil(quantityItem * weightItem)
                console.log(totalWeight)
                $form.find('.product-number').val(quantityMetr);
                $form.find('.product-weight').val(totalWeight);
            }, 1800);    
        }        
        // $form.find('.btn-buy').data('quantity', quantity);
        //$form.find('.btn-buy').data('total-price', totalPrice);
    });           
});  
