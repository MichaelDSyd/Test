from odoo import fields, models

class Book(models.Model):
    _inherit = "library.book"
    is_available = fields.Boolean("Is Available?")
#TEST CHAR FIELD BELOW
    test_char = fields.Char("Test Char Field")
#ISBN 13 or 10 VALID
    isbn = fields.Char(help="use a valid ISB-13 or ISB-10.")
    publisher_id = fields.Many2one(index=True)
#_CHECK_ISBN 10 DIGIT
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            total = sum(
                a * b for a, b in zip(digits[:9],
                ponderators)
            )
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()