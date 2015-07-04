$(function() {

    var sameShipping = $('#id_same_billing_shipping');


    // prepopulate shipping fields with billing values if "same as" checkbox
    // checked by iterating the billing fields, mapping each billing field name
    // to the shipping field name and setting its value
    $('#checkout-form').submit(function() {
        if (sameShipping.attr('checked')) {
            $('input[name^=shipping_]').each(function() {
                var billingName = this.name.replace('shipping_', 'billing_');
                $('input[name=' + billingName + ']').attr('value', this.value);
            });
            $('select[name^=shipping_]').each(function() {
                var billingSelected = $(this).children('option[selected]').val();
                var billingSelName = this.name.replace('shipping_', 'billing_');
                $('select[name=' + billingSelName + '] option[value=' + billingSelected +']').attr('selected', 'selected');
            });
        }
    });


    // show/hide shipping fields on change of "same as" checkbox and call on load
    sameShipping.change(function() {
        $('#billing_fields')[sameShipping.attr('checked') ? 'hide' : 'show']();
    }).change();

});
