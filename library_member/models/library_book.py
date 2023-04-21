from odoo import fields, models

class Book(models.Model):
    _inherit = "library.book"
    is_available = fields.Boolean("Is Available?")
    #TEST CHAR FIELD BELOW
    test_char = fields.Char("Test Char Field")
    #ISBN 13 or 10 VALID
    isbn = fields.Char(help="use a valid ISB-13 or ISB-10.")
    publisher_id = fields.Many2one(index=True)