# -*- coding: utf-8 -*-
{
    'name': "SaaS_AccessManagement",

    'summary': "modulo para brindar productos de servicios saas",

    'description': """
este modulo es para poder brindar productos para ofrecer odoo como servicio saas junto con el modulo de sucripcion. 
    """,

    'author': "automateai",
    'website': "https://automateai.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'product',
        'sale_management',
        'website_sale',
        'subscription_oca',
        'base_automation', 
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/saas_security_rules.xml',
        'views/product_template_views.xml',
        'views/sale_subscription_views.xml',
        'data/automated_actions.xml',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

