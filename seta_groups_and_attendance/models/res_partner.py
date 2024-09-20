# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # def action_view_attendance_records(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Attendance Records',
    #         'view_mode': 'tree,form',
    #         'res_model': 'attendance.record',
    #         'domain': [('attendance_record_line_ids.student_id', '=', self.id)],
    #         'context': dict(self._context),
    #     }
