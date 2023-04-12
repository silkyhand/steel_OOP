$(document).ready(function(){    
    $('.btn-buy').click(function(e) {
        e.preventDefault();
        var row = $(this).closest('tr'); 
        var productQuantity = row.find('.product-number').val();        
        var productWeight = row.find('.product-weight').val();       
        var productId = $(this).data('product_id'); 
        var name = $(this).data('name'); 
        var url = $(this).data("action");
        

        var data = {};
        data.product_id = productId;
        data.nmb = productQuantity;  
        var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val(); 
        data.weight = productWeight;  
        // var csrf = $('input[name=csrfmiddlewaretoken]').val();            
        // var csrf_token = jQuery("[name=csrfmiddlewaretoken]").val();        
        data["csrfmiddlewaretoken"] = csrf_token;        
            
        $.ajax({            
            type: 'POST',
            url: url,
            data: data,
            cache: true,
            success: function (data) {                
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
