from odoo import fields, models

class Book (models.Model):
    _inheret = "library.book"
    is_available = fields.Boolean("Is Available?")