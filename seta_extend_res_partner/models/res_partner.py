# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


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
    contact_type = fields.Selection(
        selection=[
            ("father", "Father"),
            ("mother", "Mother"),
            ("tutor", "Tutor"),
        ],
        string="Contact type",
        default="father",
        required=True,
    )
