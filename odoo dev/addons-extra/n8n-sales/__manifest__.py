# -*- coding: utf-8 -*-
{
    'name': "n8n-sales",

    'summary': "modulo para añadir productos de automatizacion en ventas",

    'description': """
Long description of module's purpose
    """,

    'author': "Automateai",
    'website': "https://automateai.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template.xml',
        'views/settings.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

    # --- LÍNEA CLAVE PARA EL ÍCONO ---
    'icon': 'n8n-sales/static/description/icon.png',
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
}

