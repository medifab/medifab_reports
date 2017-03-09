from odoo import api, fields, models, _
import json

# class ProductInventoryReportData(models.Model):
#     '''This class is taken just for printing report of product inventory transaction'''
#     
#     _name="productinventoryreport.data"
#     
#     product_templ_id = fields.Many2one('product.template','Product')
#     date = fields.Date('Date',help="Date of transaction")
#     type_id = fields.Many2one('stock.picking.type','Picking Type')
#     reference_id = fields.Many2one('stock.picking','Reference')
#     origin = fields.Char('Source Document')
#     quantity = fields.Float('Quantity')
#     location_id = fields.Many2one('stock.location','Destination Location')
#     stock_id = fields.Many2one('stock.move','Stock')

class StockMove(models.Model):
    _inherit = "stock.move"
    
    product_tmpl_id = fields.Many2one('product.template','Product Template')

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    report_header_name = fields.Char('Report Header Name',default="Order Confirmation")
    
class ProductTemplate(models.Model):
    _inherit = "product.template"
    
#     product_report_id = fields.One2many('productinventoryreport.data','product_templ_id')
    stock_id = fields.One2many('stock.move','product_tmpl_id')
    report_header_name = fields.Char('Report Header Name',default="Inventory Transaction")
    
    @api.multi
    def print_product_transaction_report(self):
#         productInventoryReportObj = self.env['productinventoryreport.data']
        stockMoveObj = self.env['stock.move']
        product_ids = self.product_variant_id
        product_ids = [each.id for each in product_ids]
        productTransactions = stockMoveObj.search([('product_id','in',product_ids)])
        for eachProductTransaction in productTransactions:
            eachProductTransaction.product_tmpl_id = self.id
#         for each in productTransactions:
#             search_stock_id = productInventoryReportObj.search([('stock_id','=',each.id)])
#             newdata = {
#                            'date' : each.date,
#                            'type_id' : each.picking_type_id.id,
#                            'reference_id':each.picking_id.id,
#                            'origin':each.origin,
#                            'quantity': each.quant_ids[0].qty if each.quant_ids else 0,
#                            'location_id':each.location_dest_id.id,
#                            'product_templ_id':self.id,
#                            'stock_id':each.id
#                     }
#             if search_stock_id:
#                 #update exiting record in new table
#                 search_stock_id.write(newdata)
#             else:
#                 productInventoryReportObj.create(newdata)
#                 if each.location_id.id:
#                     newdata['quantity'] = newdata['quantity'] - 2*newdata['quantity']
#                     newdata['location_id'] = each
#                     productInventoryReportObj.create(newdata)
        return {
                'type': 'ir.actions.report.xml',
                'report_name': 'medifab_reports.report_product_transactions',
                'file':'medifab_reports.report_product_transactions',
                'report_type':'qweb-pdf',
                'model':'product.template',
                }