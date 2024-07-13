from odoo import models,fields,api

class AccountMove(models.Model):
   
    _inherit="account.move"
    
    global_discount=fields.Float("Global Discount")
    
    @api.model_create_multi
    def create(self, vals_list):
        res  = super(AccountMove, self).create(vals_list)
        # print("-----------------helloo-----------")
        for rec in res:                     
                sale_order=self.env['sale.order'].search([('invoice_ids','in',[rec.id])])                             
                rec.global_discount=sale_order.global_discount
                # print("===========================",rec.global_discount)        
        return res
    
    