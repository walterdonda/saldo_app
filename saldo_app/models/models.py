from odoo import fields, models

class Movimiento(models.Model):
    _name = 'saldo_app.movimiento'
    _description = 'Movimiento'

    name = fields.Char(string = 'Descripción')
    move_type = fields.Selection([
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso')], string='Tipo de movimiento')
    date = fields.Date('Fecha del movimiento')
    move_amount = fields.Monetary(string ='Monto')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)
    receipt_image = fields.Binary('Imagen adjunta del recibo')
    user_id = fields.Many2one('res.users', string='Usuario')
    category_id = fields.Many2one('saldo_app.category', string='Categoría')
    tag_ids = fields.Many2many('saldo_app.tag', string='Etiquetas')
    notas = fields.Html('Notas')

class Category(models.Model):
    _name = 'saldo_app.category'
    _description = 'Categoría'

    name = fields.Char('Nombre')

class Tag(models.Model):
    _name = 'saldo_app.tag'
    _description = 'Etiquetas de movimientos'

    name = fields.Char('Nombre')

class ResUsers(models.Model):
    _inherit = 'res.users'
    movimiento_ids = fields.One2many('saldo_app.movimiento', 'user_id', string='Movimientos')
    
    
        