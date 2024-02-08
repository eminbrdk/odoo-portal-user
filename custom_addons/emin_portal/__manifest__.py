{
    'name': 'Emin-Portal',
    'version': '1.0',
    'summary': 'Modul for Emin Portal',
    'author': 'Muhammed Emin Bardakcı',
    'depends': ["base", "portal"],
    'category': "Portal",
    'data': [
        'security/ir.model.access.csv',

        "views/portal_template.xml",
        "views/student_view.xml",
        "views/menu_item.xml",
    ],
    "demo": [],
    'installable': True,
    'license': 'LGPL-3',
}