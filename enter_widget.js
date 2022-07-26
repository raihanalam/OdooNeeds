odoo.define('my_char_widget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    //var rpc = require("web.rpc")

    var charfield = AbstractField.extend({
        events: {
            'keypress .o_field_widget': function inputAction(e) {
                e.preventDefault();
                if(e.keyCode == 13){
                        console.log("enter Press");
                        debugger;
                        //var element = $('input[name="barcode_change"]');
                        var element = document.getElementsByName('barcode_change');
                        console.log(element)
                        element[0].value = e.target.value
                        var event = new Event('change');
                        console.log(event)
                        element[0].dispatchEvent(event);
                        return false;
                }
            }
        },
        init: function () {
            this._super.apply(this, arguments);
        },
        _renderEdit: function () {
            this.$el.append($('<input>', {
                'class': 'o_field_widget o_field_char o_quick_editable o_input o_required_modifier',
                'name': 'barcode',
                'type':'text',
                'id': 'o_field_input_13'
            }));
        },
    });

    fieldRegistry.add('field_enter', charfield);

    return {
        charfield: charfield,
    };
})