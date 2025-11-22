function submit_entry(card_number, expiry_date, security_code) {
    $.ajax({
        url: '/upload',
        type: "POST",
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({
            "card_num": card_number,
            "expiry_date": expiry_date,
            "cvs": security_code
        }),
    });
}

// TODO Figure out a way to prevent the cursor jumping when this is done
function handle_cardnum_input(current_input) {
    var current_input = current_input.replaceAll(' ', '');
    var output = '';
    part1 = current_input.substring(0,4);
    if (part1.length > 0) output = output + part1;
    part2 = current_input.substring(4,8);
    if (part2.length > 0) output = output + ' ' + part2;
    part3 = current_input.substring(8,12);
    if (part3.length > 0) output = output + ' ' + part3;
    part4 = current_input.substring(12,16);
    if (part4.length > 0) output = output + ' ' + part4;
    // No this is not correct but seeing this result is fun enough
    if (output.startsWith(4)){
        $('#card_num-addon').html('<img width=40em src="https://raw.githubusercontent.com/aaronfagan/svg-credit-card-payment-icons/main/flat-rounded/visa.svg"/>');
    } else if (output.startsWith(5)) {
        $('#card_num-addon').html('<img width=40em src="https://raw.githubusercontent.com/aaronfagan/svg-credit-card-payment-icons/main/flat-rounded/mastercard.svg"/>');
    } else {
        $('#card_num-addon').html('.')
    }
    return output
}

function handle_expiry_input(current_input) {
    var current_input = current_input.replaceAll('/', '');
    var output = '';
    part1 = current_input.substring(0,2);
    if (part1.length > 0) output = output + part1;
    part2 = current_input.substring(2,4);
    if (part2.length > 0) output = output + '/' + part2;
    return output;
}

$(document).ready(function(){
    const entry_form = $('#entry_form');
    const submit_button = $('#submit_btn');
    const card_num_field = $('#card_num');
    const expiry_field = $('#expiry');
    const cvs_field = $('#cvs');

    card_num_field.on("input", function(event){
        card_num_field.val(handle_cardnum_input(card_num_field.val()));
    });

    expiry_field.on("input", function(event){
        expiry_field.val(handle_expiry_input(expiry_field.val()));
    });

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

