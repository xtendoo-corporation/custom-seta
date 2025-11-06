# -*- coding: utf-8 -*-
{
    'name': 'Seta Search Filter',
    'version': '16.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Filtros personalizados para contactos: compañía y representantes legales',
    'author': 'Ivan Parrado Garcia',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_filter.xml',
    ],
    'installable': True,
    'application': False,
    'images': [
        'static/description/icon.png',
        'static/description/logo.png',
    ],
    'uninstall_hook': 'uninstall_hook',
}
