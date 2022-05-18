# -*- coding utf-8 -*-
from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    init_date = fields.Date(string="Init Date", required=False,)
    progress_manual = fields.Float("Progress manual")

    @api.onchange('timesheet_ids')
    @api.depends('timesheet_ids')
    def compute_progres_manual(self):
        for task in self:
            task.update({
                'progress_manual': sum(task.timesheet_ids.mapped('progress'))
            })