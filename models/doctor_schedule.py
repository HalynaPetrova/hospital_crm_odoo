from odoo import fields, models


class DoctorSchedule(models.Model):
    _name = "hospital.doctor.schedule"
    _description = "Doctor Schedule"
    _order = "name"

    name = fields.Char(string="Name", required=True)
