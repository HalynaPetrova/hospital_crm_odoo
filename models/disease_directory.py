from odoo import fields, models


class DiseaseDirectory(models.Model):
    _name = "hospital.disease_directory"
    _description = "Disease Directory"
    _order = "name"

    name = fields.Char(string="Name", required=True)
