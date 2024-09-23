from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    attendance_count = fields.Integer(string='Attendance Count', compute='_compute_attendance_count')

    @api.depends('attendance_count')
    def _compute_attendance_count(self):
        AttendanceLine = self.env['attendance.record.line']
        for partner in self:
            attendance_lines = AttendanceLine.search([('student_id', '=', partner.id)])
            partner.attendance_count = len(attendance_lines)
