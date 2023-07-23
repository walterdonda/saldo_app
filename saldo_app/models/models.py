from odoo import fields, models

class Movimiento(models.Model):
    _name = 'saldo_app.movimiento'
    _description = 'Movimiento'

    name = fields.Char('Nombre')
    move_type = fields.Selection([
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso')

    ], string='Tipo de movimiento')
    date = fields.Datetime(string= 'Fecha de movimiento')
    move_amount = fields.Float('Monto del movimiento')
    receipt_image = fields.Binary('Imagen adjunta del recibo')
    user_id = fields.Many2one('res.users', string='Usuario')
    category_id = fields.Many2one('saldo_app.category', string='Categoría')
    tag_ids = fields.Many2many('saldo_app.tag', string='Tags')

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
    
    
        