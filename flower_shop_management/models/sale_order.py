from odoo import models,fields,api
from _datetime import datetime,date
from odoo.exceptions import  ValidationError
import re
import json
import io
from odoo.tools import date_utils
import base64
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class SaleOrder(models.Model):
   
    _inherit="sale.order"
    
    global_discount=fields.Float("Global Discount")
    is_show_discount=fields.Boolean(compute="_for_showdiscount_group",store=False, string="Show discount",default=False)

    
    
    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total','global_discount')
    def _compute_amounts(self):
        res  = super(SaleOrder, self)._compute_amounts()
        print("--------------",self.amount_total)
        for rec in self:
           
            rec.amount_total=rec.amount_total*(1-(rec.global_discount/100.0))            
        print("===========amount_total===============",rec.amount_total)
        return res
    
    
    def _for_showdiscount_group(self):
        for record in self:
            if self.env.user.has_group('flower_shop_management.show_discount'):
                record.is_show_discount=True
            else:
                record.is_show_discount=False
                
                
    def plant_sale_details(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        format_title1 = workbook.add_format({
            'bold': True,
            'align': 'center',
            'font_size': 12,
            'font': 'Arial',
            'border': True
        })           
        format_title2 = workbook.add_format({
            'bold': False,
            'align': 'center',
            'font_size':10,
            'font': 'Times New Roman',
            'border': False
        })
        format_title3 = workbook.add_format({
            'bold': False,
            'align': 'center',
            'font_size':12,
            'font': 'Times New Roman',
            'border': False
        })
        format_title_total = workbook.add_format({
            'bold': True,
            'align': 'center',
            'font_size':12,
            'font': 'Times New Roman',
            'border': False,
            'font_color' : 'red'
        })        
        row=1
        col=3
        sheet = workbook.add_worksheet('Customer Report')
       
        sheet.set_column('D:D',15)
        sheet.set_column('E:E',20)
        sheet.set_column('J:J',20)
        sheet.write(row+1,col,'Customer Name',format_title1 )
        sheet.write(row+2,col,'Order Date',format_title1 )
        
        col=col+1

        if(self.partner_id):
            sheet.write(row+1,col,self.partner_id.name,format_title2)
        else:
            sheet.write(row+1,col,'-',format_title2)
        row=row+1
        if(self.date_order):
            sheet.write(row+1,col,str(self.date_order),format_title2)
        else:
            sheet.write(row+1,col,'-',format_title2)
            
            
        row=row+5
        sheet.write(row,col,'Product',format_title1 )
        sheet.write(row,col+1,'Quantity',format_title1 )
        sheet.write(row,col+2,'Unit Price',format_title1 )
        sheet.write(row,col+3,'Subtotal',format_title1 )
        row=row+1
        sum=0
        if(self.order_line):
            for rec in self.order_line:
                
                if(rec.product_template_id):
                    sheet.write(row,col,rec.product_template_id.name,format_title2)
                else:
                    sheet.write(row,col,'-',format_title2)
                    
                if(rec.product_uom_qty):
                    sheet.write(row,col+1,rec.product_uom_qty,format_title2)
                else:
                    sheet.write(row,col+1,'-',format_title2)
                    
                if(rec.price_unit):
                    sheet.write(row,col+2,str(rec.price_unit),format_title2)
                else:
                    sheet.write(row,col+2,'-',format_title2)
                    
                if(rec.price_subtotal):
                    sheet.write(row,col+3,str(rec.price_subtotal),format_title2)

                else:
                    sheet.write(row,col+3,'-',format_title2)
                row=row+1   
        
        
        col=col+5
        row=row+5
        
        

        row=row+1
        sheet.write(row,col,'Global Discount',format_title1 )
        if(self.global_discount):
            sheet.write(row,col+1,str(self.global_discount)+"%",format_title2)
        else:
            sheet.write(row,col+1,'-',format_title2)
         
        row=row+1
       
        sheet.write(row,col,'Total Price',format_title_total )
        if(self.amount_total):
            sheet.write(row,col+1,str(self.amount_total)+"$",format_title2)
        else:
            sheet.write(row,col+1,'-',format_title2)
        



        
                        

        
        
        workbook.close()
        output.seek(0)
        result = base64.b64encode(output.read())
        report_id = self.env['common.xlsx.out'].sudo().create({'filedata': result, 'filename': 'Customer Report.xls'})
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/binary/download_document?model=common.xlsx.out&field=filedata&id=%s&filename=%s.xls' % (
                report_id.id, self.partner_id.name),
            'target': 'new',
        }
        output.close()
        

        