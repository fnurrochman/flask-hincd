from wtforms import Form, StringField, IntegerField, validators

class buildinterface_form(Form):
    interface_name = StringField('Interface Name', [validators.InputRequired()])
    description = StringField('Description')
    vlan = IntegerField('VLAN', [validators.InputRequired()])
    ip_address = StringField('IP Address', [validators.InputRequired()])
    mask = StringField('Netmask', [validators.InputRequired()])

class buildvlan_form(Form):
    vlan_name = StringField('VLAN Name', [validators.InputRequired()])
    vlan_id = IntegerField('VLAN ID', [validators.InputRequired()])