# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields

class ContactGroup(models.Model):
    _name = 'contact.group'
    _description = 'Group of Contacts'

    name = fields.Char(string='Group Name', required=True)
    contact_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Students',
        domain=[('is_company', '=', False)]
    )
    attendance_ids = fields.One2many('attendance.record', 'group_id', string='Attendance Records')

    @api.model
    def create(self, vals):
        group = super(ContactGroup, self).create(vals)
        if 'contact_ids' in vals:
            self._update_contact_group(vals['contact_ids'][0][2], group.id)
        return group

    def write(self, vals):
        res = super(ContactGroup, self).write(vals)
        if 'contact_ids' in vals:
            for group in self:
                self._update_contact_group(vals['contact_ids'][0][2], group.id)
        return res

    def _update_contact_group(self, contact_ids, group_id):
        self.env['res.partner'].search([('group_id', '=', group_id)]).write({'group_id': False})
        if contact_ids:
            self.env['res.partner'].browse(contact_ids).write({'group_id': group_id})
