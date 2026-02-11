# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015-2024 DevIntelle Consulting Service Pvt.Ltd
#    (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Survey Portal | Survey Answers Portal | Website Portal for Survey',
    'version': '18.0.1.0.0',
    'sequence': 1,
    'category': 'Survey',
    'license': 'LGPL-3',
    'description':
        """
Survey Portal View Survey Answers from Portal for Survey Your to customer portal user to view survey answers from the website to my account portal Odoo Print Survey Answers PDF enables you to save or print survey responses in PDF for analysis and record keeping. Further, you can save the responses in the system or any remote storage Export Survey Answer In XLS Export Survey Answer In XLS Report Export Survey In XLS Export Completed Survey Answers Export  Group Surveys Export Survey In Excel Export Survey In XLSX Export Survey XLSX Survey Export Survey Excel Odoo

    """,
    'summary': 'Survey Portal View Survey Answers from Portal Print Survey Answers PDF Your to customer portal user to view survey answers from the website to my account portal Odoo Print Survey Answers PDF enables you to save or print survey responses in PDF for analysis and record keeping. Further, you can save the responses in the system or any remote storage Export Survey Answer In XLS Export Survey Answer In XLS Report Export Survey In XLS Export Completed Survey Answers Export  Group Surveys Export Survey In Excel Export Survey In XLSX Export Survey XLSX Survey Export Survey Excel Odoo',
    'depends': ['website', 'survey'],
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/portal_views.xml',
    ],
    'images': ['images/main_screenshot.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,

    # author and support Details
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'https://www.devintellecs.com',
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd',
    'support': 'devintelle@gmail.com',
    'price': 27.0,
    'currency': 'EUR',
    'pre_init_hook': 'pre_init_check',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
