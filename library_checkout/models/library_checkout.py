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
    line_ids = fields.One2many(
        "library.checkout.line",
        "checkout_id",
        string="Borrowed Books",
    )
    #Added api.model and stage_id/state
    @api.model
    def _default_stage_id(self):
        Stage = self.env ["library.checkout.stage"]
        return Stage.search([("state","=","new")],
          limit=1)
    @api.model
    def _group_expand_stage_id(self, stages, domain,
      order):
        return stages.search([], order=order)
    stage_id = fields.Many2one(
        "library.checkout.stage",
        default=_default_stage_id,
        group_expand="_group_expand_stage_id")
    state = fields.Selection(related="stage_id.state")
        