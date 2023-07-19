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

    @api.model
    def create(self, vals):
        # Code before create: should use the 'vals' dict
        new_record = super().create(vals)
        # Code after create: can use the 'new_record'
        # created
        if new_record.stage_id.state in ("open", "close"):
            raise exceptions.UserError(
                "State not allowed for new checkouts."
            )
        return new_record
        
    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)

      def write(self, vals):
        # Code before write: 'self' has the old values
        if "stage_id" in vals:
            Stage = self.env["library.checkout.stage"]
            old_state = self.stage_id.state
            new_state =
              Stage.browse(vals["stage_id"]).state
            if new_state != old_state and new_state ==
              "open":
                vals['checkout_date'] = fields.Date.today()
            if new_state != old_state and new_state ==
               "done":
                vals['close_date'] = fields.Date.today()
        super().write(vals)
        # Code after write: can use 'self' with the updated
        # values
        return True 