# -*- coding utf-8 -*-
from odoo import models, fields, _


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    timesheet_type = fields.Many2one(comodel_name="project.timesheet.type", string="Type")
    progress = fields.Float(string="% Progress",)
    #milestone_id = fields.Many2one(comodel_name="project.milestone", string="Milestone", related="task_id.milestone_id", store=True)
    progress_manual = fields.Float("Progress manual", related="task_id.progress_manual", store=True)
    planned_hours = fields.Float(string="Planned Hours", related="task_id.planned_hours", store=True)
