from odoo import models, fields

class Template(models.Model):
    _name = 'dynamic_web_template.template'
    _description = 'Template'

    name = fields.Char(string='Template Name', required=True)
    sequence = fields.Integer(string='Sequence')
    view_id = fields.Many2one('ir.ui.view', string="Website process form", domain=[('type', '=', 'qweb')])


