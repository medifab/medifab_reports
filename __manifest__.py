# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Medifab Reports',
    'version' : '1.1',
    'summary': 'Report customization for product inventory, sale order, invoice',
    'sequence': 30,
    'description': """
    New Report for products which gives details of inventory transaction performed on each product, Customization in sale order and invoice reports
    """,
    'category': 'Report',
    'images' : [],
    'depends' : ['stock','report'],
    'data': [
             'data/paperformat.xml',
             'views/product_view.xml',
             'report/report_product_transactions.xml',
             'report/report_sale_order_confirm.xml',
             'report/report_invoice1.xml',
             'views/template.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
