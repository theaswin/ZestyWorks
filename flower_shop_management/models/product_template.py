from odoo import models,fields,api
from _datetime import datetime,date
class ProductTemplate(models.Model):
   
    _inherit="product.template"
    
    is_flower=fields.Boolean(string="Is Flower?")
    plant_id=fields.Many2one('plant.details',string="Plant",domain="[('flowering_type','=','flowering')]" )
    plant_type=fields.Selection([('indoor','Indoor'),('outdoor','Outdoor')],string="Type",related="plant_id.plant_type",store=True)
    brand_id=fields.Many2one('brand.details',string="Brand",related="plant_id.brand_id",store="True")
    material_feature=fields.Char(string="Material Feature",related="plant_id.material_feature",store="True")
    speacial_feature=fields.Text(string="Special Feature",related="plant_id.speacial_feature")
    sunlight_exposure=fields.Selection([('partial_shade','Partial Shade'),('full_shade','Full Shade '),('full_sun','Full Sun ')],string="Sunlight Exposure ",related="plant_id.sunlight_exposure")
    expected_blooming=fields.Selection([('summer','Summer'),('winter','Winter '),('spring','Spring')],string="Expected Booming Period",related="plant_id.expected_blooming")


    
    
class ProductProduct(models.Model):
   
    _inherit="product.product"
    
    color_ids=fields.Many2many('color.details','flower_color_rel','flower_id','color_id',string="Color")
