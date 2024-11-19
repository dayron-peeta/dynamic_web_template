from odoo import models, fields

class Process(models.Model):
    _name = 'dynamic_web_template.process'
    _description = 'Process'

    name = fields.Char(string='Process Name', required=True)
    template_id = fields.Many2one('dynamic_web_template.template', string='Template', required=True)
