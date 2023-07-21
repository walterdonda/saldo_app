# -*- coding: utf-8 -*-
# from odoo import http


# class SaldoApp(http.Controller):
#     @http.route('/saldo_app/saldo_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saldo_app/saldo_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('saldo_app.listing', {
#             'root': '/saldo_app/saldo_app',
#             'objects': http.request.env['saldo_app.saldo_app'].search([]),
#         })

#     @http.route('/saldo_app/saldo_app/objects/<model("saldo_app.saldo_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saldo_app.object', {
#             'object': obj
#         })
