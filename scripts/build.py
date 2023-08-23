from jinja2 import Template


def build_interface(interface_name, description, vlan, ip_address, mask):
    variables = {'interface_name':interface_name,
                'description':description,
                'vlan':vlan,
                'ip_address':ip_address,
                'mask':mask}
    with open('./scripts/jinja_templates/interface.j2') as file:
        jinja_template = Template(file.read())
        config = jinja_template.render(variables=variables)
        return config

def build_vlan(vlan_name, vlan_id):
    variables = {'vlan_name':vlan_name,
                'vlan_id':vlan_id}
    with open('./scripts/jinja_templates/vlan.j2') as file:
        jinja_template = Template(file.read())
        config = jinja_template.render(variables=variables)
        return config