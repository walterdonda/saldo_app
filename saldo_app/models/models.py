from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Movimiento(models.Model):
    _name = "saldo_app.movimiento"
    _description = "Movimiento"
    _inherit = "mail.thread"

    name = fields.Char(string="Descripción")
    move_type = fields.Selection(
        [("ingreso", "Ingreso"), ("egreso", "Egreso")],
        string="Tipo de movimiento",
        tracking=True,
    )
    date = fields.Date("Fecha del movimiento", tracking=True)
    move_amount = fields.Monetary(string="Monto", tracking=True)
    user_id = fields.Many2one('res.users', string='Usuario', default= lambda self: self.env.user.id)
    company_id = fields.Many2one(
        "res.company", string="Empresa", default=lambda self: self.env.company.id
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        default=lambda self: self.env.company.currency_id,
        tracking=True,
    )
    receipt_image = fields.Binary("Imagen adjunta del recibo", tracking=True)
    user_id = fields.Many2one("res.users", string="Usuario",default=lambda self: self.env.user.id)
    category_id = fields.Many2one("saldo_app.category", string="Categoría")
    tag_ids = fields.Many2many(comodel_name="saldo_app.tag", string="Etiquetas")
    notas = fields.Html(string="Notas", )
    user_email = fields.Char(related='user_id.email', string="Correo del usuario")
    
    @api.constrains('move_amount')
    def _constrains_move_amount(self):
        if(self.move_amount < 0):
            raise ValidationError("El monto del movimiento no puede ser menor que 0")
        elif(self.move_amount > 100000):
            raise ValidationError("El monto del movimiento no puede ser mayor que 100000")
    
    @api.onchange('move_type')
    def _onchange_move(self):
        if(self.move_type == 'ingreso'):
            self.name = 'Ingreso: '

        elif(self.move_type == 'egreso'):
            self.name = 'Egreso: '
    
        
class Category(models.Model):
    _name = "saldo_app.category"
    _description = "Categoría"

    name = fields.Char("Nombre")

    def ver_movimientos(self):
        return{
            "name":f"Movimientos de la categoría  {self.name}",
            "type": "ir.actions.act_window",
            "res_model": "saldo_app.movimiento",
            "views": [[False,"tree"]],
            "target": "new",
            "domain": [["category_id",'=',self.id]]
        }


class Tag(models.Model):
    _name = "saldo_app.tag"
    _description = "Etiquetas de movimientos"

    name = fields.Char("Nombre")


class ResUsers(models.Model):
    _inherit = "res.users"
    movimiento_ids = fields.One2many(
        "saldo_app.movimiento", "user_id", string="Movimientos"
    )

    def mi_cuenta(self):
        return {
            "name": f"Mi cuenta",
            "type": "ir.actions.act_window",
            "res_model": "res.users",
            "res_id": self.env.user.id,
            "views": [[False, "form"]],
            "target": "self"
        }
    currency_id = fields.Many2one('res.currency', string='Moneda')

    total_ingresos = fields.Monetary(compute='_compute_movimientos', string='Total_ingresos')
    total_egresos = fields.Monetary(compute='_compute_movimientos', string='total_egresos')
    @api.depends('movimiento_ids')
    def _compute_movimientos(self):
        for record in self:
            record.total_ingresos = sum(record.movimiento_ids.filtered(lambda m: m.move_type == 'ingreso').mapped("move_amount"))
            record.total_egresos = sum(record.movimiento_ids.filtered(lambda m: m.move_type == 'egreso').mapped("move_amount"))