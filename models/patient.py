from datetime import datetime

from odoo import fields, models, api


class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Model"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birth_date = fields.Date(string="Birth", required=True)
    age = fields.Integer(string="Age", compute="_compute_age")
    passport_data = fields.Char(string="Passport")
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone")
    contact_person = fields.Char(string="Contact Name")
    personal_doctor = fields.Char(string="Personal")

    # @api.depends("birth_date")
    # def _compute_age(self):
    #     for rec in self:
    #         self.age = datetime.today() - rec.birth_date.year
    #
    #
    # # today = datetime.today()
    # # age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    # # return age
    # #

# # print(datetime.today())
#
#
# for patient in self:
#     if patient.birth_date:
#         birth_date_str = patient.birth_date.strftime("%Y-%m-%d")
#         birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
#         today = datetime.now().date()
#         age = (
#                 today.year
#                 - birth_date.year
#                 - ((today.month, today.day) < (birth_date.month, birth_date.day))
#         )
#         patient.age = age
#     else: