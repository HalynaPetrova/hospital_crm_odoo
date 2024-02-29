from odoo import models, fields, api


class AbstractPerson(models.AbstractModel):
    _name = "hospital.abstract.person"
    _description = "Abstract Person"
    _rec_name = "full_name"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full name", compute="_compute_full_name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="Email")

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for person in self:
            person.full_name = f"{person.first_name} {person.last_name}"
