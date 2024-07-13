from odoo import models,fields,api,_

class BrandDetails(models.Model):
    _name="brand.details"
    _description=" Brand of a plant"
    
    name=fields.Char(string="Name",required="True",copy="False")
    code= fields.Char(string="Code",required="True",copy="False")
    
    _sql_constraints = [
        
        ('name_unique','UNIQUE(name)',"Brand Name should be unique"),
        ('code_unique','UNIQUE(code)',"Brand Code should be unique")
        ]    