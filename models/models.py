# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repair(models.Model):
    _inherit = 'repair.order'

    employee_reparador = fields.Many2one('hr.employee', 'Reparador')
    tiempo = fields.Integer("Tiempo (minutos)")
    gastos = fields.Float("Gastos")
    total = fields.Float("Total")
    revision = fields.Boolean("Revisión")