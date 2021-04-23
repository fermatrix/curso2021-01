from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')
    state = fields.Selection(
        [('new', 'New'),
        ('asignado', 'Asignado'),
        ('proceso', 'En proceso'),
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('cancelado', 'Cancelado')],
        string='State',
        default='new')
    time = fields.Float(
        string='Time') 
    assigned = fields.Boolean(
        string='Assigned',
        readonly=True)
    date_limit = fields.Date(
        string='Date Limit')
    action_corrective = fields.Html(
        string='Corrective Action',
        help='Describe corrective actions')
    action_preventive = fields.Html(
        string='Preventive Action',
        help='Describe preventive actions')

    def marcar_asignado(self):
        self.set_state('asignado')

    def marcar_enproceso(self):
        self.set_state('proceso')

    def marcar_pendiente(self):
        self.set_state('pendiente')

    def marcar_resuelto(self):
        self.set_state('resuelto')
    
    def marcar_cancelado(self):
        self.set_state('cancelado')

    def set_state(self, new_state): 
        self.ensure_one()
        self.state = new_state
        self.assigned = True

    def set_reset(self): 
        self.ensure_one()
        self.state = 'new'
        self.assigned = False


