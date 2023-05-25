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
                var roundQuantity = Number((multiple * length).toFixed(1))
                $form.find('.product-number').val(roundQuantity);
                totalWeight = Math.ceil(multiple* weightItem);        
                $form.find('.product-weight').val(totalWeight);
            }, 1800);
        } else {
            timeout = setTimeout(function() {
                quantityItem = Math.ceil(totalWeight / weightItem);
                quantityMetr = Number((quantityItem * length).toFixed(1))
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


$(document).ready(function(){    

    var timeout = null;

    $('.product-number-cart').on('keyup', function(e) {
        e.preventDefault();
        clearTimeout(timeout);
        var $productCart = $(this).closest('.product-data-cart');             
        var cartProductNmb = $productCart.find('.product-number-cart').val();  
        console.log(cartProductNmb)         
        var lengthCart = parseFloat($(this).data('len'));  
        console.log(lengthCart)         
        //var weightItem = parseFloat($(this).data('weight'));           
        //var quantity = $form.find('.product-number').val();        
        //var totalWeight = $form.find('.product-weight').val();       
        timeout = setTimeout(function(){
            var multiple = Math.ceil(cartProductNmb / lengthCart)
            var roundQuantity = Number((multiple * lengthCart).toFixed(1))
            $productCart.find('.product-number-cart').val(roundQuantity);
            // totalWeight = Math.ceil(multiple* weightItem);        
            // $form.find('.product-weight').val(totalWeight);
        }, 1500);       
    });

});

$(document).ready(function(){
    $('.btn-buy').click(function(e){ /* Клик по кнопке "Добавить в корзину" */
	var btnWrap = $(this).parents('.btn-wrap'); /* Запоминаем враппер кнопки */
  	btnWrap.append('<div class="animtocart"></div>'); /* Добавляем во враппер кружок, который будет анимирован и улетать от кнопки в корзину */
    $('.animtocart').css({ /* Присваиваем стили кружку и позицию курсора мыши */
    	'position' : 'absolute',
      	'background' : 'blue',
      	'width' :  '25px',
      	'height' : '25px',
      	'border-radius' : '100px',
      	'z-index' : '9999999999',
      	'left' : e.pageX-25,
    	'top' : e.pageY-25,
    });
	var cart = $('.btn-cart').offset(); /* Получаем местоположение корзины на странице, чтобы туда полетел кружок */
	$('.animtocart').animate({ top: cart.top + 'px', left: cart.left + 'px', width: 0, height: 0 }, 800, function(){ /* Делаем анимацию полёта кружка от кнопки в корзину и по окончанию, удаляем его */
		$(this).remove();
    });
});

   
});    


$(document).ready(function () {
    // $('.subcategory-list').scrollbar();

    $('#subcategory-search-input').on('input', function () {
        var searchValue = $(this).val().toLowerCase();
        $('.subcategory-list li').each(function () {
            var text = $(this).text().toLowerCase();
            if (text.indexOf(searchValue) >= 0) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});
