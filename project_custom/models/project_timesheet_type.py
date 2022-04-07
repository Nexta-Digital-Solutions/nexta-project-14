# -*- coding utf-8 -*-
from odoo import models, fields, _


class ProjectTimeseetType(models.Model):
    _name = "project.timesheet.type"
    _description = "Project Timesheet types"

    name = fields.Char(string="Name", required=True)