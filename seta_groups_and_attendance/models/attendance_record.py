# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api,models, fields

class AttendanceRecord(models.Model):
    _name = 'attendance.record'
    _description = 'Attendance Record'

    name = fields.Char(string='Name', compute="compute_name", store=True)
    activity = fields.Char(string='Activity', required=True)
    group_id = fields.Many2one('contact.group', string='Group', required=True)
    attendance_record_line_ids = fields.One2many('attendance.record.line', 'attendance_record_id',
                                                 string='Attendance Lines')
    color = fields.Integer(string='Color', compute='_compute_color')
    create_date = fields.Datetime(string='Creation Date', default=lambda self: fields.Datetime.now())
    student_names = fields.Char(string='Student Names', compute='_compute_student_names', store=True)

    @api.depends('activity', 'group_id')
    def compute_name(self):
        for record in self:
            record.name = f"{record.activity} - {record.group_id.name}"


    @api.depends('attendance_record_line_ids.student_id')
    def _compute_student_names(self):
        for record in self:
            student_names = ', '.join(record.attendance_record_line_ids.mapped('student_id.name'))
            record.student_names = student_names

    @api.depends('attendance_record_line_ids.present')
    def _compute_color(self):
        for record in self:
            if all(line.present for line in record.attendance_record_line_ids):
                record.color = 10 #Verde
            else:
                record.color = 3 #Amarillo

    @api.onchange('group_id')
    def _onchange_group_id(self):
        self.attendance_record_line_ids = [(5, 0, 0)]
        if self.group_id:
            students = self.group_id.contact_ids
            lines = []
            for student in students:
                lines.append((0, 0, {
                    'student_id': student.id,
                    'present': True,
                }))
            self.attendance_record_line_ids = lines
