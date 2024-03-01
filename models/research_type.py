from odoo import fields, models


class ResearchType(models.Model):
    _name = "hospital.research.type"
    _description = "Research Type"
    _order = "name"

    name = fields.Char(string="Name", required=True)
