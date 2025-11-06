from odoo import models, fields, api

class TherapySession(models.Model):
    _name = 'therapy.session'
    _description = 'Sesión de Terapia'

    fecha_terapia = fields.Date(string='Fecha')
    hora_inicio = fields.Char(string='Hora Inicio')
    hora_fin = fields.Char(string='Hora Fin')
    alumno_id = fields.Many2one('res.partner', string='Alumno', domain="[('is_student','=',True)]")
    terapeuta_id = fields.Many2one('res.partner', string='Terapeuta')
    producto_id = fields.Many2one('product.product', string='Producto')
    iva = fields.Float(string='IVA')
    precio = fields.Monetary(string='Precio', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    @api.onchange('producto_id')
    def _onchange_producto_id(self):
        if self.producto_id:
            self.precio = self.producto_id.lst_price

    def action_crear_factura(self):
        for session in self:
            invoice_vals = {
                'partner_id': session.alumno_id.id,
                'move_type': 'out_invoice',
                'invoice_date': session.fecha_terapia,
                'therapy_alumno_id': session.alumno_id.id,
                'therapy_hora_inicio': session.hora_inicio,
                'therapy_hora_fin': session.hora_fin,
                'invoice_line_ids': [
                    (0, 0, {
                        'product_id': session.producto_id.id,
                        'name': f"Terapia realizada el {session.fecha_terapia.strftime('%d/%m/%Y') if session.fecha_terapia else ''}",
                        'quantity': 1,
                        'price_unit': session.precio,
                        # Campos personalizados para la línea de factura
                        'therapy_fecha_terapia': session.fecha_terapia,
                        'therapy_terapeuta_id': session.terapeuta_id.id,
                        'therapy_iva': session.iva,
                        'therapy_session_id': session.id,
                    })
                ],
            }
            factura = self.env['account.move'].create(invoice_vals)
            # Asignar número de factura según la secuencia de Odoo
            if factura.move_type == 'out_invoice' and factura.state == 'draft':
                factura._onchange_journal_id()
                factura._onchange_partner_id()
            return {
                'type': 'ir.actions.act_window',
                'name': 'Factura',
                'res_model': 'account.move',
                'view_mode': 'form',
                'res_id': factura.id,
                'target': 'current',
            }

    def action_save_session(self):
        # Guardar el registro actual (Odoo lo hace automáticamente, pero puedes añadir lógica extra aquí)
        return True

    def action_clear_fields(self):
        for session in self:
            session.fecha_terapia = False
            session.hora_inicio = False
            session.hora_fin = False
            session.alumno_id = False
            session.terapeuta_id = False
            session.producto_id = False
            session.iva = 0.0
            session.precio = 0.0
        return {
            'type': 'ir.actions.act_window_close',
        }

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Es Alumno')
    terapia_ids = fields.One2many('therapy.session', 'alumno_id', string='Terapias Realizadas')

    saldo_inicial = fields.Float(string='Saldo Inicial')  # Ahora editable manualmente

    @api.depends('saldo_inicial', 'terapia_ids.precio')
    def _compute_saldo_actual(self):
        for partner in self:
            total_gastado = sum(partner.terapia_ids.mapped('precio'))
            partner.saldo_actual = partner.saldo_inicial - total_gastado

    saldo_actual = fields.Float(string='Saldo Actual', compute='_compute_saldo_actual', store=True)

    def action_ver_saldo(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Detalle de Saldo',
            'res_model': 'res.partner',
            'view_mode': 'form',
            'views': [(self.env.ref('seta_therapies_management.view_partner_saldo_modal').id, 'form')],
            'res_id': self.id,
            'target': 'new',
        }
