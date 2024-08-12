# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class TypeMedicalDiagnostic(models.Model):
    _name = 'type.medical.diagnostic'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Type medical diagnostic"

    name = fields.Char(
        string="Type diagnostic Name",
        required=True,
        index=True,
    )
    medical_diagnostic_id = fields.One2many(
        comodel_name="medical.diagnostic",
        required=True,
        inverse_name="type_medical_diagnostic_id",
    )
