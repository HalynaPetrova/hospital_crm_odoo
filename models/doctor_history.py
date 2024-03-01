from odoo import fields, models


class DoctorHistory(models.Model):
    _name = "hospital.doctor.history"
    _description = "Doctor History"
    _order = "name"

    name = fields.Char(string="Name", required=True)
