from odoo import fields, models


class ResearchCatalog(models.Model):
    _name = "hospital.research.catalog"
    _description = "Research Catalog"
    _order = "name"

    name = fields.Char(string="Name", required=True)
