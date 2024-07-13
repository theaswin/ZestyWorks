from odoo import models,fields,api,_

class ColorDetails(models.Model):
    _name="color.details"
    _description=" Color of a plant"
    
    name=fields.Char(string="Name",required="True",copy="False")
    code= fields.Char(string="Code",required="True",copy="False")
    
    _sql_constraints = [
        
        ('name_unique','UNIQUE(name)',"Color Name should be unique"),
        ('code_unique','UNIQUE(code)',"Color Code should be unique")
        ]    