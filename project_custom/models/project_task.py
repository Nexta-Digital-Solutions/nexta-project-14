# -*- coding utf-8 -*-
from odoo import models, fields,_


class ProjectTask(models.Model):
    _inherit = "project.task"

    init_date = fields.Date(string="Init Date", required=False,)
    progress_manual = fields.Float("Progress manual")