# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date(string="Birth date")
    birth_place = fields.Char(string="Birth place")
    ss_number = fields.Char(string="S.S. number")
