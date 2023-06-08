# -*- coding utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProjectMilestone(models.Model):
    _inherit = "project.milestone"

    total_hours = fields.Float(string="Total Hours", required=False,)
    progress_manual = fields.Float("Progress manual")
