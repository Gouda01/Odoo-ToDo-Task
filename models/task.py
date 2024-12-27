from odoo import models, fields, api

class Task(models.Model) :
    _name = 'task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=1, tracking=1)
    # assign_to = fields.Char(required=1)
    assign_to_id = fields.Many2one('res.partner', required=1, tracking=1)
    description = fields.Text()
    due_date = fields.Date(tracking=1)
    status = fields.Selection([
        ('new', 'New'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new', tracking=1)


    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exits')
    ]

    def action_new(self):
        for rec in self:
            rec.status = "new"


    def action_inprogress(self):
        for rec in self:
            rec.status= "inprogress"

    def action_completed(self):
        for rec in self:
            rec.status= "completed"

