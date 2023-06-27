from odoo import fields, models

class Checkout(models.Model):
    _name = "library.checkout"
    _description = "Checkout Request"

    member_id = fields.Many2one(
        "library.member",
        required=True,
    )
    user_id = fields.Many2one(
        "res.users",
        "Librarian",
        default=lambda s: s.env.user,
    )
    request_date = fields.Date(
        default=lambda s: fields.Date.today(),
    )