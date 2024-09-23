from odoo import api, models, fields

class AttendanceRecordLine(models.Model):
    _name = 'attendance.record.line'
    _description = 'Attendance Record Line'

    attendance_record_id = fields.Many2one('attendance.record', string='Attendance Record', ondelete='cascade')
    student_id = fields.Many2one('res.partner', string='Student', domain=[('is_company', '=', False)], required=True)
    present = fields.Boolean(string='Present', default=True)

    activity = fields.Char(related='attendance_record_id.activity', string='Actividad', store=True)
    group_id = fields.Many2one(related='attendance_record_id.group_id', string='Grupo', store=True)
