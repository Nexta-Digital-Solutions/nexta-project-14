# -*- coding utf-8 -*-
from odoo import models, fields, api, _


class ProjectTimesheetTypeLine(models.Model):
    _name = "project.timesheet.type.line"
    _description = "Project Timesheet types lines"

    timesheet_type = fields.Many2one(comodel_name="project.timesheet.type", string="Type", required=True)
    total_hours = fields.Float(string="Total Hours", required=False,)
    hours_spent = fields.Float(string="Hours Spent", required=False, compute="_compute_spent_hours", store=True)
    remaining_hours = fields.Float(string="Remaining Hours", required=False, compute="_compute_spent_hours", store=True)
    spend_percentage = fields.Float(string="Remaining percent", required=False, compute="_compute_spent_hours", store=True)
    project_id = fields.Many2one(comodel_name="project.project", string="Project",)

    @api.onchange('project_id.task_ids.timesheet_ids', 'hours_spent')
    @api.depends('project_id.task_ids.timesheet_ids','hours_spent')
    def _compute_spent_hours(self):
        for line in self:
            timesheet_line_ids = line.project_id.task_ids.mapped('timesheet_ids')
            total = 0.0
            remaining = 0.0
            spend_percentage = 0.0
            if bool(timesheet_line_ids):
                type_lines = timesheet_line_ids.filtered(lambda x: line.timesheet_type and x.timesheet_type.id == line.timesheet_type.id)
                total  = sum(type_lines.mapped('unit_amount'))
                remaining = line.total_hours - total
                spend_percentage = (total*100)/line.total_hours if line.total_hours else 0
            line.update({
                'hours_spent':total,
                'remaining_hours':remaining,
                'spend_percentage':spend_percentage,
            })