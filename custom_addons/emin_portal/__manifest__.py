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
        "views/school_view.xml",
        "views/menu_item.xml",
    ],
    "demo": [],
    "assets": {
        "web.assets_frontend": [
            "emin_portal/static/src/js/new_student_validation.js",
        ]
    },
    'installable': True,
    'license': 'LGPL-3',
}