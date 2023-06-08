from odoo import fields, models
from odoo.exceptions import ValidationError
class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    _order = "name, date_published desc"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner",
      string="Publisher")
    author_ids = fields.Many2many("res.partner",
      string="Authors")

#Business Logic to Check ISBN

    def check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12],
              ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

#Validation Error Code

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("please provide an ISBN for %s" % book.name)
            if book.isbn and not book._checkisbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
        return True 
