{
    'name': 'Dynamic Web Template',
    'version': '1.0',
    'author': 'Your Name',
    'depends': ['base', 'website'],
    'data': [
        # views
        'views/template1.xml',
        'views/template2.xml',
        'views/template3.xml',
        # data
        'data/templates.xml',
        'data/processes.xml',
        # security
        'security/ir.model.access.csv',
    ],
    'installable': True,
	'application': True,
}

