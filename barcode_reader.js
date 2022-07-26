odoo.define('my_char_widget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');
    //var rpc = require("web.rpc")

    var charfield = AbstractField.extend({
        tagName: 'div',
        supportedFieldTypes: ['char'],

        events: {
            'keypress .o_field_widget': function inputAction(e) {
                if (e.keyCode == 13) {
                    e.target.parentElement.focus()
                    console.log("enter button pressed")
                    var in_put = e.target.value
                    this._rpc({
                        model: 'purchase.return',
                        method: 'normal',
                        args: [in_put],
                    })
                    e.target.value = ''
                    console.log(this)
                }
            }
        },
        init: function () {
            this._super.apply(this, arguments);
        },
        _renderEdit: function () {

            this.$el.append($('<input>', {
                'class': 'o_field_widget o_input o_required_modifier',
                'name': 'barcode'
            }));
        },

    });

    fieldRegistry.add('field_enter', charfield);

    return {
        charfield: charfield,
    };
})