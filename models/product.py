from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
import json


class ProductProduct(models.Model):
    _name = 'product.product.history'

    name = fields.Text(string="Vals", required=True)
    value = fields.Float(string='Sale Base Price', digits='Product Price', required=True, default=0.0)
    product_id = fields.Many2one('product.product', 'Product', required=True)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def write(self, vals):
        res = super(ProductProduct, self).write(vals)
        if 'standard_price' in vals:
            standard_price = vals['standard_price']
            # if negative we remove it but will log
            if float_compare(standard_price, 0.0, precision_digits=3) < 0.0:
                vals.pop('standard_price')
            self.env['product.product.history'].create({
                'name': json.dumps(vals),
                'value': vals['standard_price'],
                'product_id': self.id
            })
        return res
