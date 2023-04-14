# -*- coding utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = "project.task"

    init_date = fields.Date(string="Init Date", required=False,)
    progress_manual = fields.Float("Progress manual")

    @api.onchange('timesheet_ids')
    @api.depends('timesheet_ids')
    def compute_progres_manual(self):
        for task in self:
            if sum(task.timesheet_ids.mapped('progress')) > 1:
                raise UserError(_('The sum of all progress lines cannot be greater than 100%'))
            task.update({
                'progress_manual': sum(task.timesheet_ids.mapped('progress'))
            })