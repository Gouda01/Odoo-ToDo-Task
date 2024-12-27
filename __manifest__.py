{
    'name': "To-Do Management",
    'version': '17.0.0.1.0',
    'depends': ['base', 'mail'],
    'author': "Mohamed Gouda",
    'category': '',

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/task_view.xml',
    ],
    'assets': {
        
    },

    'application' : True,

}