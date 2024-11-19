# controller.py
from odoo import http
from odoo.http import request

class DynamicTemplateController(http.Controller):

    @http.route('/my_process/<model("dynamic_web_template.template"):template>', type='http', auth='user',
                methods=['GET', 'POST'], website=True, csrf=False)
    def render_dynamic_template(self, template, **kwargs):
        # Preparar valores para pasar a la vista
        values = {
            'template': template.name
        }
        return request.env['ir.ui.view']._render_template(template.view_id.xml_id, values)


