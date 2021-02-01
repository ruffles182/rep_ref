# -*- coding: utf-8 -*-
# from odoo import http


# class RepRef(http.Controller):
#     @http.route('/rep_ref/rep_ref/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rep_ref/rep_ref/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rep_ref.listing', {
#             'root': '/rep_ref/rep_ref',
#             'objects': http.request.env['rep_ref.rep_ref'].search([]),
#         })

#     @http.route('/rep_ref/rep_ref/objects/<model("rep_ref.rep_ref"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rep_ref.object', {
#             'object': obj
#         })
