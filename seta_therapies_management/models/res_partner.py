# Este archivo se ha restablecido a su estado original, sin campos personalizados ni lógica de representantes.
# Puedes volver a añadir la lógica de representantes, filtros y relaciones cuando lo desees.

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'


    is_student = fields.Boolean(string='Es alumno')
    representante_de = fields.Char(
        string='Representante de',
        compute='_compute_representante_de',
        store=True
    )
    alumno_ids = fields.One2many('res.partner', 'parent_id', string='Alumnos')
    saldo_inicial = fields.Monetary(
        string='Saldo inicial',
        currency_field='currency_id',
        compute='_compute_saldo_inicial',
        store=True
    )
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)
    invoice_ids = fields.One2many(
        'account.move', 'partner_id', string='Facturas')
    total_terapias = fields.Monetary(
        string='Total terapias',
        currency_field='currency_id',
        compute='_compute_total_terapias',
        store=True
    )
    terapia_count = fields.Integer(
        string='Terapias',
        compute='_compute_terapia_count',
        store=False
    )



    @api.depends('is_student', 'invoice_ids.amount_total', 'invoice_ids.state')
    def _compute_saldo_inicial(self):
        for partner in self:
            total = 0.0
            if partner.is_student:
                invoices = partner.invoice_ids.filtered(lambda inv: inv.move_type == 'out_invoice' and inv.state == 'posted')
                total = sum(invoices.mapped('amount_total'))
            partner.saldo_inicial = total

    def _compute_total_terapias(self):
        for partner in self:
            total = 0.0
            if partner.terapia_ids:
                total = sum(partner.terapia_ids.mapped('precio'))
            partner.total_terapias = total

    def _compute_terapia_count(self):
        for partner in self:
            partner.terapia_count = len(partner.terapia_ids)

    def action_ver_terapias(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Terapias',
            'res_model': 'therapy.session',
            'view_mode': 'tree,form',
            'domain': [('alumno_id', '=', self.id)],
            'context': {
                'default_alumno_id': self.id,
                'search_default_alumno_id': self.id,
                'create': True,
            },
            'target': 'current',
        }
