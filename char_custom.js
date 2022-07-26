odoo.define('uni_pos.FieldChar', function (require) {
    "use strict";

    var FieldChar = require('web.basic_fields').FieldChar;
    var registry = require('web.field_registry');

    var FieldCharCustom = FieldChar.extend({
        _onKeydown: function (e) {
            if (e.which === $.ui.keyCode.ENTER) {
                var element = document.getElementsByName('barcode');
                console.log(element)
                element[0].value = e.target.value
                var event = new Event('change');
                console.log(event)
                element[0].dispatchEvent(event);
                return false;
            }
            this._super.apply(this, arguments);
        },
    });

    registry.add('char_custom', FieldCharCustom);

});