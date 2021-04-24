from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(required=True)
    description = fields.Text(translate = True)
    date = fields.Date()
    state = fields.Selection(
        [('new', 'New'),
        ('assigned', 'Assigned'),
        ('inprocess', 'In Process'),
        ('pending', 'Pending'),
        ('solved', 'Solved'),
        ('canceled', 'Canceled')],
        string='State',
        default='new')
    time = fields.Float() 
    assigned = fields.Boolean(readonly=True)
    date_limit = fields.Date()
    action_corrective = fields.Html(help='Describe corrective actions')
    action_preventive = fields.Html(help='Describe preventive actions')

    def mark_assigned(self):
        self.set_state('assigned')

    def mark_inprocess(self):
        self.set_state('inprocess')

    def mark_pending(self):
        self.set_state('pending')

    def mark_solved(self):
        self.set_state('solved')
    
    def mark_canceled(self):
        self.set_state('canceled')

    def set_state(self, new_state): 
        self.ensure_one()
        self.state = new_state
        self.assigned = True

    def set_reset(self): 
        self.ensure_one()
        self.state = 'new'
        self.assigned = False


