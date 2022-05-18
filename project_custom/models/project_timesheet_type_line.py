# -*- coding utf-8 -*-
from odoo import models, fields, api, _


class ProjectTimesheetTypeLine(models.Model):
    _name = "project.timesheet.type.line"
    _description = "Project Timesheet types lines"

    name = fields.Char(string="Name", computed="compute_name", store=True)
    timesheet_type = fields.Many2one(comodel_name="project.timesheet.type", string="Type", required=True)
    total_hours = fields.Float(string="Total Hours", required=False,)
    hours_spent = fields.Float(string="Hours Spent", required=False, compute="_compute_spent_hours", store=True)
    remaining_hours = fields.Float(string="Remaining Hours", required=False, compute="_compute_spent_hours", store=True)
    spend_percentage = fields.Float(string="Remaining percent", required=False, compute="_compute_spent_hours", store=True)
    project_id = fields.Many2one(comodel_name="project.project", string="Project",required=True)
    project_init_date = fields.Date(string="Project Init Date", related="project_id.init_date")
    project_end_date = fields.Date(string="Project End Date", related="project_id.end_date")


    @api.onchange('timesheet_type', 'project_id')
    def compute_name(self):
        for line in self:
            if line.timesheet_type and line.project_id:
                line.name = "[{}]{}".format(line.project_id.name, line.timesheet_type.name)

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
                spend_percentage = 100-(total*100)/line.total_hours if line.total_hours else 0
            line.update({
                'hours_spent':total,
                'remaining_hours':remaining,
                'spend_percentage':spend_percentage,
            })