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
    father_name = fields.Char(
        string="Father name",
    )
    father_birth_date = fields.Date(
        string="Father birth date",
    )
    father_profession = fields.Char(
        string="Father profession",
    )
    father_company = fields.Char(
        string="Father company",
    )
    mother_name = fields.Char(
        string="Mother name",
    )
    mother_birth_date = fields.Date(
        string="Mother birth date",
    )
    mother_profession = fields.Char(
        string="Mother profession",
    )
    mother_company = fields.Char(
        string="Mother company",
    )
    home_phone = fields.Char(
        string="Home phone",
    )
    father_phone = fields.Char(
        string="Father phone",
    )
    father_company_phone = fields.Char(
        string="Father company phone",
    )
    mother_phone = fields.Char(
        string="Mother phone",
    )
    mother_company_phone = fields.Char(
        string="Mother company phone",
    )
    other_phone = fields.Char(
        string="Other phone",
    )
    contact_type = fields.Selection(
        selection=[
            ("father", "Father"),
            ("mother", "Mother"),
            ("tutor", "Tutor"),
        ],
        string="Contact type",
        default="father",
    )
