# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date(
        string="Birth date",
        required=True,
    )
    birth_place = fields.Char(
        string="Birth place",
    )
    ss_number = fields.Char(
        string="S.S. number",
    )
    brothers_number = fields.Integer(
        string="Brothers number",
    )
    name = fields.Char(
        string="name",
    )
    birth_date_contact = fields.Date(
        string="Birth date",
    )
    company = fields.Char(
        string="Company",
    )
    home_phone = fields.Char(
        string="Home phone",
    )
    company_phone = fields.Char(
        string="Company phone",
    )
    discapacity = fields.Boolean(
        string="Discapacity",
        default=False,
    )
    grade_of_discapacity = fields.Integer(
        string="Grade of discapacity"
    )
    scholarships_and_grants = fields.Char(
        string="Scholarships and grants"
    )
    allergies = fields.Char(
        string="Allergies"
    )
    observations = fields.Char(
        string="Observations"
    )
    contact_type = fields.Selection(
        selection=[
            ("father", "Father"),
            ("mother", "Mother"),
            ("tutor", "Tutor"),
            ("school", "School"),
        ],
        string="Contact type",
        default="father",
        required=True,
    )
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res.update({'type': 'contact'})
        return res
