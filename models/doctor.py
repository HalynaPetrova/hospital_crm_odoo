from odoo import fields, models, api


class Patient(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"
    _inherit = "hospital.abstract.person"
    _order = "first_name"

    specialty = fields.Char(string="Speciality")
    is_intern = fields.Boolean(string="Is Intern")
    mentor_id = fields.Many2one(
        "hospital.doctor", string="Mentor", domain=[("is_intern", "=", False)]
    )



