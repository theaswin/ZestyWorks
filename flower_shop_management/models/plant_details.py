from odoo import models,fields,api,_

class PlantDetails(models.Model):
    _name="plant.details"
    _description=" Plants in a shop"
    
    name=fields.Char(string="Name")
    image= fields.Binary(string="Image")
    color_ids=fields.Many2many('color.details','plant_color_rel','plant_id','color_id',string="Color")
    plant_type=fields.Selection([('indoor','Indoor'),('outdoor','Outdoor')],string="Type")
    flowering_type=fields.Selection([('flowering','Flowering'),('non_flowering','Non Flowering')],string="Flowering Type")
    brand_id=fields.Many2one('brand.details',string="Brand")
    material_feature=fields.Char(string="Material Feature")
    speacial_feature=fields.Text(string="Special Feature")
    sunlight_exposure=fields.Selection([('partial_shade','Partial Shade'),('full_shade','Full Shade '),('full_sun','Full Sun ')],string="Sunlight Exposure ")
    expected_blooming=fields.Selection([('summer','Summer'),('winter','Winter '),('spring','Spring')],string="Expected Blooming Period")
