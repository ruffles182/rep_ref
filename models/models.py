# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repair(models.Model):
    _inherit = 'repair.order'

    employee_reparador = fields.Many2one('hr.employee', 'Reparador')
    tiempo = fields.Integer("Tiempo (minutos)")
    gastos = fields.Float("Gastos")
    total = fields.Float("Total")
    revision = fields.Boolean("Revisión")

    # wizard para el form view de elección de días
class rep_ref_reporte(models.TransientModel):
    _name = 'rep_ref.reporte.wizard'

    reparador = fields.Many2one('hr.employee', "Reparador")
    date_start = fields.Date(string="Fecha inicial", required=True, default=fields.Date.today)
    date_end = fields.Date(string="Fecha final", required=True, default=fields.Date.today)


    def get_report(self):   
        
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'reparador': self.reparador.id,
                'date_start': self.date_start,
                'date_end': self.date_end,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `_get_report_values()` and pass `data` automatically.
        return self.env.ref('rep_ref.reparador_report').report_action(self, data=data)


        # """Call when button 'Get Report' clicked.
        # """
        # data = {
        #     'ids': self.ids,
        #     'model': self._name,
        #     'form': {
        #         'date_start': self.date_start,
        #         'date_end': self.date_end,
        #     },
        # }

        # # use `module_name.report_id` as reference.
        # # `report_action()` will call `_get_report_values()` and pass `data` automatically.
        # return self.env.ref('rep_ref.recap_report_reparador').report_action(self, data=data)

    class ReporteReparadores(models.AbstractModel):
        """Abstract Model for report template.

        for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
        """

        _name = 'report.rep_ref.reparador_report_view'

        # @api.model
        def _get_report_values(self, docids, data=None):
            date_start = data['form']['date_start']
            date_end = data['form']['date_end']
            reparadorForm = data['form']['reparador']
            # date_start_obj = datetime.strptime(date_start, DATE_FORMAT)
            # date_end_obj = datetime.strptime(date_end, DATE_FORMAT)
            # date_diff = (date_end_obj - date_start_obj).days + 1
            cuenta = 0
            docs = []
            nombre_reparador = ""
            reparador = 0
            repairs = self.env['repair.order'].search([], order='name asc')
            for repair in repairs:
                if (repair.employee_reparador.id == reparadorForm):
                    folio = repair.name
                    efectivo = repair.amount_total
                    tiempo = repair.tiempo
                    gastos = repair.gastos
                    total = efectivo - gastos
                    nombre_reparador = repair.employee_reparador.name



                    docs.append({
                        'folio': folio,
                        'efectivo': efectivo,
                        'tiempo': tiempo,
                        'gastos': gastos,
                        'total': total,
                    })

            cuenta = len(docs)

            return {
                'employee': nombre_reparador,
                'revisiones': cuenta,
                'date_start': date_start,
                'date_end': date_end,
                'docs': docs,
            }