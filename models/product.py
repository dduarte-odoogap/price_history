from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
import json
import logging
import inspect
from pprint import pprint

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _name = 'product.product.history'

    name = fields.Text(string="Vals", required=True)
    value = fields.Float(string='Sale Base Price', digits='Product Price', required=True, default=0.0)
    product_id = fields.Many2one('product.product', 'Product', required=True)
    code_context = fields.Text(string="Code context", required=True)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def write(self, vals):
        if 'standard_price' in vals:
            code_context = self.env["ir.config_parameter"].sudo().get_param("price_history.code_context", False)
            standard_price = vals['standard_price']
            data = {
                'name': json.dumps(vals),
                'value': standard_price,
                'product_id': self.id
            }
            if code_context:
                stack_trace = ""
                for frame in inspect.stack()[1:]:
                    stack_trace += "# %s\n%s\n%s" % (
                        frame.filename, "-" * 50, frame.code_context and frame.code_context[0] or 'N/A')
                data.update({'code_context': stack_trace})
            # if negative we remove it but will log
            if float_compare(standard_price, 0.0, precision_digits=3) < 0.0:
                _logger.info("Prices cannot be negative")
                vals.pop('standard_price')
            self.env['product.product.history'].create(data)
        return super(ProductProduct, self).write(vals)
