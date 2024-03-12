# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birth_date = fields.Date(string="Birth date")
    birth_place = fields.Char(string="Birth place")
    ss_number = fields.Char(string="S.S. number")
    brethren_number = fields.Integer(string="Brethren number")
    father_name = fields.Char(string="Father name")
    father_age = fields.Integer(string="Father age")
    father_profession = fields.Char(string="Father profession")
    father_company = fields.Char(string="Father company")
    mother_name = fields.Char(string="Mother name")
    mother_age = fields.Integer(string="Mother age")
    mother_profession = fields.Char(string="Mother profession")
    mother_company = fields.Char(string="Mother company")
    home_phone = fields.Char(string="Home phone")
    father_phone = fields.Char(string="Father phone")
    father_company_phone = fields.Char(string="Father company phone")
    mother_phone = fields.Char(string="Mother phone")
    mother_company_phone = fields.Char(string="Mother company phone")
    other_phone = fields.Char(string="Other phone")
