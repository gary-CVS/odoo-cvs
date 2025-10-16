from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model_create_multi
    def create(self, vals_list):
        """Assure que tous les nouveaux produits utilisent le gramme comme unité de poids."""
        products = super().create(vals_list)
        gram_uom = self.env.ref("uom.product_uom_gram", raise_if_not_found=False)
        for product in products:
            if gram_uom and product.weight_uom_name == "kg":
                # Juste pour être sûr que la conversion est correcte
                if product.weight:
                    product.weight = product.weight * 1000
        return products

    def _get_weight_uom_name_from_ir_config_parameter(self):
        """Force l'affichage des unités en grammes."""
        return "g"
