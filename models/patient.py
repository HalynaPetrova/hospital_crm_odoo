from odoo import fields, models, api


class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Model"
    _inherit = "hospital.abstract.person"
    _order = "first_name"

    birth_date = fields.Date(string="Birth", required=True)
    age = fields.Integer(string="Age", compute="_compute_age")
    passport_data = fields.Char(string="Passport")
    contact_person = fields.Char(string="Contact Name")
    personal_doctor = fields.Char(string="Personal doctor")

    @api.depends("birth_date")
    def _compute_age(self):
        for person in self:
            if person.birth_date:
                today = fields.Date.today()
                person.age = today.year - person.birth_date.year
                if person.birth_date.month >= today.month and person.birth_date.day > today.day:
                    person.age -= 1
            else:
                person.age = 0

    _sql_constraints = [
        (
            "check_unique_passport_data",
            "UNIQUE(passport_data)",
            "Passport data must be unique!",
        ),
    ]
