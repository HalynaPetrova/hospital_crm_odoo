from odoo import fields, models


class Diagnosis(models.Model):
    _name = "hospital.diagnosis"
    _description = "Diagnosis"
    _order = "name"

    name = fields.Char(string="Name", required=True)
