from odoo import models, api, fields

class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket')
    
class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Tag'

    name = fields.Char()
    ticket_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tickets')     

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
    assigned = fields.Boolean(
        compute = '_compute_assigned'
    )
    date_limit = fields.Date()
    action_corrective = fields.Html(help='Describe corrective actions')
    action_preventive = fields.Html(help='Describe preventive actions')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to')
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions')
    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags')    

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

    def set_reset(self): 
        self.ensure_one()
        self.state = 'new'

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            if self.user_id:
                record.assigned = True
            else:
                record.assigned = False              

    ticket_qty = fields.Integer(
        string='Ticket quantity',
        compute='_compute_ticket_qty')

    @api.depends('user_id')
    def _compute_ticket_qty(self):
        for record in self:
            other_tickets = self.env['helpdesk.ticket'].search([('user_id', '=', record.user_id.id)])
            if record.user_id.id == 0:
                record.ticket_qty = False
            else:
                record.ticket_qty = len(other_tickets)

    tag_name = fields.Char(
        string = 'Tag Name'
    )

    def create_tag(self):
        self.ensure_one()
        self.write({
            'tag_ids': [(0,0, {'name': self.tag_name})]
            })
        self.tag_name = False