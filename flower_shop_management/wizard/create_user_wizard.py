from odoo import models,fields,api

class RelatedUser(models.TransientModel):
    _name="related.user"
    _description="Related User"
    
    
    rel_id=fields.Many2one('res.users',string="Related User")
    user_type=fields.Many2one('res.groups',string="User Group")
    email=fields.Char("Email")
    password=fields.Char("Password")
    
    def update_user(self):
        for rec in self: 
            searched_rec=self.env['res.users'].search([('id',"=",self.rel_id.id)]) 
            # searched_pass=self.env['change.password.user'].search([]) 
            # print("============",len(searched_pass))
            if searched_rec:
                searched_rec.write({'name' : self.rel_id.name})
                searched_rec.write({'login' : self.email})
                searched_rec.write({'password' : self.password})
                
           
    
    
    
    
    