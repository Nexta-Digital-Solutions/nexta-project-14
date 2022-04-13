# -*- coding: utf-8 -*-

{
    'name': 'Detailed Project Timesheet',
    'version': '1.2',
    'category': 'Project',
    'sequence': 6,
    'author' : 'NextaDS',
    'website' : 'http://www.nextads.es',
    'summary': "Detailed project timesheet" ,
    'description': """

=======================

Detailed project timesheet.

""",
    'depends': ['project','timesheet_grid','hr_timesheet'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_timesheet_type_views.xml',
        'views/project_timesheet_type_line.xml',
        'data/project_timesheet_type_data.xml',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
}