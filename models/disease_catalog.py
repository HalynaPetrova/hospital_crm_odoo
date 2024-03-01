from odoo import fields, models


class DiseaseCatalog(models.Model):
    _name = "hospital.disease.catalog"
    _description = "Disease Catalog"
    _order = "name"

    name = fields.Char(string="Name", required=True)
