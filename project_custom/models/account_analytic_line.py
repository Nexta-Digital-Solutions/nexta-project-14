# -*- coding utf-8 -*-
from odoo import models, fields, _


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    timesheet_type = fields.Many2one(comodel_name="project.timesheet.type", string="Type", required=True)
    progress = fields.Float(string="% Progress",)