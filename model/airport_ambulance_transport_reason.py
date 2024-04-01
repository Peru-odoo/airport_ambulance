from odoo import models, fields, api


class AirportAmbulanceTransportReason(models.Model):
    _name = 'airport.ambulance.transport.reason'
    _description = 'Airport Ambulance Transport Reason'

    name = fields.Char(string='運送原因名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'transport_reason_id')