{
    'name': 'Gestión de Terapias',
    'version': '16.0.1.0.0',
    'category': 'Association',
    'summary': 'Gestión de terapias para asociaciones',
    'description': 'Registra terapias, vincula alumnos y terapeutas, integra con facturación.',
    'author': 'Ivan Parrado Garcia',
    'website': '',
    'depends': ['base', 'contacts', 'account', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/therapy_session_view.xml',
        'views/therapy_menu.xml',
        'views/res_partner_view_inherit.xml',
        'views/account_move_line_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'images': [
        'static/description/icon.png',
        'static/description/logo.png',
    ],
}
