# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2024 ZestyBeanz Technologies Pvt Ltd(<http://www.zbeanztech.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Flower Shop  Management',
    'version' : '16.0.0.0',
    'category' : 'Sales',
    'summary' : 'This module deals with sale of flowers in a shop',
    'sequence' : -1,
    'description' : """This module deals with sale of flowers in a shop""", 
    'author' :'Zest Beanz Technologies',       
    'license': 'LGPL-3', 
    'website' : 'www.flower.com',  
    'depends' : ['product','sale','account','hr'],
    'data' : [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/plant_details.xml',
        'views/color_details.xml',
        'views/brand_details.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/hr_employee_views.xml',        
        'views/menu_view.xml',
        'wizard/sale_details_wizard.xml',
        'wizard/create_user_wizard.xml',
        'reports/sale_order_report.xml',        
        'reports/report.xml',
        'reports/plant_report.xml',
        
        ],
    
    'test':  [],
    'demo': [],
    'assets': {
        'point_of_sale.assets': [          
            'pharmacy_management/static/src/xml/**/*',
            'pharmacy_management/static/src/js/**/*',
            # 'pharmacy_management/static/src/js/order_reciept.js',
            # 'pharmacy_management/static/src/js/product_code.js',
            # 'pharmacy_management/static/src/js/user_phone.js',
            # 'pharmacy_management/static/src/js/product_expiry.js',
            # 'pharmacy_management/static/src/js/search.js',
            # 'pharmacy_management/static/src/js/newbutton.js',
            # 'pharmacy_management/static/src/js/validation_quantity.js',
            # 'pharmacy_management/static/src/js/order_addnote.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,        
 }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
