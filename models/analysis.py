from odoo import fields, models


class Analysis(models.Model):
    _name = "hospital.analysis"
    _description = "analysis"
    _order = "name"

    name = fields.Char(string="Name", required=True)
