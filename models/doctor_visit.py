from odoo import fields, models


class DoctorVisit(models.Model):
    _name = "hospital.doctor.visit"
    _description = "Doctor Visit"
    _order = "name"

    name = fields.Char(string="Name", required=True)
