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
    
    
    
    
    
    
