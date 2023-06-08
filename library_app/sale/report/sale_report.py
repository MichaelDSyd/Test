def init (self):
    tools.drop_view_if_exists(self.env.cr, self._table)
    self.env.cr.execute(
        "CREATE or REPLACE VIEW %s as (%s)"
        % (self._table, self.query())
    )