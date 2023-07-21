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

class Category(models.Model):
    _name = 'saldo_app.category'
    _description = 'Categoría'

    name = fields.Char('Nombre')

class Tag(models.Model):
    _name = 'saldo_app.tag'
    _description = 'Tag'

    name = fields.Char('Nombre')
        