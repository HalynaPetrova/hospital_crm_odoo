from odoo import fields, models


class DiseaseType(models.Model):
    _name = "hospital.disease.type"
    _description = "Disease Type"
    _order = "name"

    name = fields.Char(string="Name", required=True)
