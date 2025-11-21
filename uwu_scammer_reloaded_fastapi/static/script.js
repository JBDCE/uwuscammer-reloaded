function submit_entry(card_number, expiry_date, security_code) {
    console.log(card_number);
    console.log(expiry_date);
    console.log(security_code);
}

$(document).ready(function(){
    const entry_form = $('#entry_form');
    const submit_button = $('#submit_btn');
    const card_num_field = $('#card_num');
    const expiry_field = $('#expiry');
    const cvs_field = $('#cvs');
    submit_button.on("click", function(event){
        submit_entry(
            card_num_field.val(),
            expiry_field.val(),
            cvs_field.val()
        );
        entry_form.removeClass('load_in');
        entry_form.addClass('sendoff');
        setTimeout(function(){
            entry_form.addClass('hidden');
            card_num_field.val('');
            expiry_field.val('');
            cvs_field.val('');
            window.location.reload();
        }, 1000);
    });
    setTimeout(function(){
        entry_form.removeClass('hidden');
        entry_form.addClass('load_in');
    }, 500);
});

