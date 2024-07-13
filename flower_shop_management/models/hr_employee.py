from odoo import fields, models, api, _

from datetime import date


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    rel_id=fields.Many2one('res.users',"Related User")
    
    def action_create_rel_user(self):
        # print("--------hi-----------")
        return{
            'type': 'ir.actions.act_window',
            'name': 'Open Wizard User Create',
            'res_model': 'related.user',
            'view_mode':'form',
       
            'context': {
                'default_rel_id': self.rel_id.id,                
            },
            'target': 'new',
            }