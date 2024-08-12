# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalDiagnostic(models.Model):
    _name = 'medical.diagnostic'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Medical diagnostic"

    name = fields.Char(
        string="Diagnostic Name",
        required=True,
        index=True,
        tracking=True,
    )
    res_partner_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
        inverse_name="medical_diagnostic_ids",
    )
    diagnostic_date = fields.Date(
        string="Diagnostic date",
    )
    diagnosis = fields.Char(
        string="Diagnosis",
    )
    applied_techniques = fields.Char(
        string="Applied techniques",
    )
    result = fields.Char(
        string="Result",
    )
    professional = fields.Char(
        string="Professional",
    )
    type_medical_diagnostic_id = fields.Many2one(
        comodel_name="type.medical.diagnostic",
        string="Type medical diagnostic",
    )
