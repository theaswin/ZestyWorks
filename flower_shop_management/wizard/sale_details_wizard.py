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


class SaleReports(models.TransientModel):
    _name="sale.reports"
    _description="Sale Reports"
    
    from_date=fields.Date("From Date")
    to_date=fields.Date("To Date")
    # plant_type=fields.Selection([('indoor','Indoor'),('outdoor','Outdoor')],string="Type")
    
    def print_pdf(self):
        for rec in self:
            
            domain = [('create_date','>=', rec.from_date),('create_date','<=', rec.to_date)]
            sale_order_data = self.env['sale.order'].search(domain)
            print("datas>>>>>>>>>>>>>>>>>>>>>>>>>>>",len(sale_order_data))
            
            # for sale in sale_order_data:
            #
            #     plant_list=[]
            #     dict1={
            #         'reference_number' : sale.name,
            #         'customer_name' : sale.partner_id.name,
            #         'create_date' : sale.create_date,
            #         # 'product_name' : sale.order_line.product_template_id.name,
            #
            #         }
            #     print("----------",dict1)
            # list1=[]
            # list2=[]
            # for plant in sale_order_data:
            #     if(plant.order_line.product_template_id.plant_type=='indoor'):
            #         list1.append(plant)
            #     else:
            #         list2.append(plant)
            #
            # print("====================",list)
            # print("====================",list2)
            #
            

        
    def print_excel(self):
        print("---hii---")
        for rec in self:            
            domain = [('date_order','>=', rec.from_date),('date_order','<=', rec.to_date)]
            sale_order_data = self.env['sale.order'].search(domain)
           
     
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
        col=1
        sheet = workbook.add_worksheet('Time period Sale record')
        
        sheet.set_column('E:E',10)
        sheet.set_column('D:D',20)
        sheet.set_column('C:C',20)
        sheet.set_column('F:F',10)
        sheet.set_column('G:G',10)
        sheet.set_column('B:B',15) 
        
        sheet.write(row+1,col+2,'Start Date',format_title1 )
        sheet.write(row+2,col+2,'End Date',format_title1 )
        sheet.write(row+1,col+3,str(self.from_date),format_title1 )
        sheet.write(row+2,col+3,str(self.to_date),format_title1 )

        sheet.write(row+6,col+1,'Customer Name',format_title1 )
        sheet.write(row+6,col+2,'Order Date',format_title1 )
        sheet.write(row+6,col+3,'Product',format_title1 )
        sheet.write(row+6,col+4,'Quantity',format_title1 )
        sheet.write(row+6,col+5,'Unit Price',format_title1 )
        sheet.write(row+6,col+6,'Total',format_title1 )

        sheet.write(row+4,col,'Indoor Plants',format_title_total )

        if sale_order_data:
            for record in sale_order_data:
                
                for line in record.order_line:
                    
                    if(line.product_template_id.plant_type=='indoor'):
                        sheet.write(row+7,col+1,record.partner_id.name,format_title2)
                        sheet.write(row+7,col+2,str(line.create_date),format_title2 )
                        sheet.write(row+7,col+3,line.product_template_id.name,format_title2 )
                        sheet.write(row+7,col+4,str(line.product_uom_qty),format_title2 )
                        sheet.write(row+7,col+5,str(line.price_unit),format_title2 )
                        sheet.write(row+7,col+6,str(line.price_subtotal),format_title2 )
                        row = row+1
                        col + col+1
                        
        row=row+9               
        sheet.write(row,col,'Outdoor Plants',format_title_total )
        
        sheet.write(row+2,col+1,'Customer Name',format_title1 )
        sheet.write(row+2,col+2,'Order Date',format_title1 )
        sheet.write(row+2,col+3,'Product',format_title1 )
        sheet.write(row+2,col+4,'Quantity',format_title1 )
        sheet.write(row+2,col+5,'Unit Price',format_title1 )
        sheet.write(row+2,col+6,'Total',format_title1 )


        if sale_order_data:
            for record in sale_order_data:
                
                for line in record.order_line:
                    
                    if(line.product_template_id.plant_type=='outdoor'):
                        sheet.write(row+3,col+1,record.partner_id.name,format_title2)
                        sheet.write(row+3,col+2,str(line.date_order),format_title2 )
                        sheet.write(row+3,col+3,line.product_template_id.name,format_title2 )
                        sheet.write(row+3,col+4,str(line.product_uom_qty),format_title2 )
                        sheet.write(row+3,col+5,str(line.price_unit),format_title2 )
                        sheet.write(row+3,col+6,str(line.price_subtotal),format_title2 )
                        row = row+1
                        col + col+1                

        workbook.close()
        output.seek(0)
        result = base64.b64encode(output.read())
        report_id = self.env['common.xlsx.out'].sudo().create({'filedata': result, 'filename': 'Customer Report.xls'})
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/binary/download_document?model=common.xlsx.out&field=filedata&id=%s&filename=%s.xls' % (
                report_id.id, 'Time period Sale Report'),
            'target': 'new',
        }
        output.close()
        
    
            
        
        