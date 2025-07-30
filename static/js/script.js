
// Ajoutez une classe active lorsque vous cliquez sur le lien d'inscription
document.getElementById("registerTab").addEventListener("click", function() {
  document.getElementById("loginTab").classList.remove("text-orange");
  this.classList.add("text-orange");
});

// Ajoutez une classe active lorsque vous cliquez sur le lien de connexion
document.getElementById("loginTab").addEventListener("click", function() {
  document.getElementById("registerTab").classList.remove("text-orange");
  this.classList.add("text-orange");
});





// jquery ready start
$(document).ready(function() {
	// jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE,
    For sliders, interactions and other

    */ ///////////////////////////////////////


	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });

    $(".increment-btn").click(function(e){
        e.preventDefault();
        var inc_value = $(this).closest('.product-data').find('.qty-input').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value)? 0: value;
        if(value< 10){
            value++;
            $(this).closest('.product-data').find('.qty-input').val(value);
        }
    })

    $(".decrement-btn").click(function(e){
        e.preventDefault();
        var dec_value = $(this).closest('.product-data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value)? 0: value;
        if(value > 1){
            value--;
            $(this).closest('.product-data').find('.qty-input').val(value);
        }
    })


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if





});
// jquery end

setTimeout(function(){
  $('#message').fadeOut('slow')
}, 4000)

