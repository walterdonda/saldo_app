# -*- coding: utf-8 -*-
{
    'name': "Saldo APP",

    'summary': """
        Registra de forma simple ingresos y egresos fincancieros.""",

    'description': """
        Integración con el módulo base para registrar movimientos financieros.
    """,

    'author': "Walter Donda",
    'license': "LGPL-3",
    'website': "https://odoo-runbot.sytes.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir_model_access.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
