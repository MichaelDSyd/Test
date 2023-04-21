from odoo import fields, models

class Book(models.Model):
    _inherit = "library.book"
    is_available = fields.Boolean("Is Available?")
    #TEST CHAR FIELD BELOW
    test_char = fields.Char("Test Char Field")