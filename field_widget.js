odoo.define('my_char_widget', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');
    var fieldRegistry = require('web.field_registry');

    var charfield = AbstractField.extend({
        // className: ' my-class',
        tagName: 'div',
        supportedFieldTypes: ['char'],
        events: {
            'keypress .o_field_widget': function inputAction(e) {
                // div.focus()
                console.log("on the event")
                if (e.keyCode == 13) {
                    e.target.parentElement.focus()
                    console.log("enter button pressed")
                    setTimeout(function () {
                        e.target.focus()
                        console.log("i did my job")
                    }, 500)
                } else {
                    console.log("not expected key");
                }
            }


        },

        init: function () {
            this._super.apply(this, arguments);
        },
        _renderEdit: function () {
            this.$el.empty();
            this.$el.removeClass();

            this.$el.attr("tabindex","0")

            this.$el.append($('<input>', {
                'class': 'o_field_widget o_input o_required_modifier',
            }));
        },
        _renderReadonly: function () {

            this.$el.addClass("my-class");


        },


    });

    fieldRegistry.add('charwidget', charfield);

    return {
        charfield: charfield,
    };
})