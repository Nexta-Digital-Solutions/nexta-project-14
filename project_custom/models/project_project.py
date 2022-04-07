# -*- coding utf-8 -*-
from odoo import models, fields, api, _


class Project(models.Model):
    _inherit = "project.project"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for project in self:
            return {'domain': {'responsible_customer': [('parent_id', '=', project.partner_id.id)]}}

    init_date = fields.Date(string="Init Date", required=False,)
    end_date = fields.Date(string="End Date", required=False,)
    responsible_customer = fields.Many2one(comodel_name="res.partner", string="Responsible Customer", required=False)
    business_consultant = fields.Many2one(comodel_name="res.users", string="Business Consultant", required=False)
    functional_consultant = fields.Many2one(comodel_name="res.users", string="Functional Consultant", required=False)
    type_lines_ids = fields.One2many(comodel_name="project.timesheet.type.line", inverse_name="project_id", string="Timesheet Type lines", required=False, )