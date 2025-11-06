from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    therapy_alumno_id = fields.Many2one('res.partner', string='Alumno')
    therapy_hora_inicio = fields.Char(string='Hora Inicio')
    therapy_hora_fin = fields.Char(string='Hora Fin')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    therapy_fecha_terapia = fields.Date(string='Fecha')
    therapy_terapeuta_id = fields.Many2one('res.partner', string='Terapeuta')
    therapy_iva = fields.Float(string='IVA')
    # El campo product_id y price_unit ya existen en account.move.line

    therapy_session_id = fields.Many2one('therapy.session', string='Sesión de Terapia')
