$.get('CSRFTokenManager.do', function(data) {
    var send = XMLHttpRequest.prototype.send,
    token =data;
    document.cookie='X-CSRF-Token='+token;
    XMLHttpRequest.prototype.send = function(data) {
        this.setRequestHeader('X-CSRF-Token',token);
        //dojo.cookie("X-CSRF-Token", "");
 
        return send.apply(this, arguments);
    };
 });


$(document).ready(function(){
    $('.header').height($(window).height());
    

    $("#quantity").keyup(function() {
        $("#weigth").val($(this).val() * 2);
    }) 
     

    $("#weigth").keyup(function() {
        $("#quantity").val($(this).val() / 2); 
     
    }) 

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

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb; 
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();        
        console.log(csrf_token);
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
            },
            error: function(){
                console.log("error")
            }
        })
    })
});  