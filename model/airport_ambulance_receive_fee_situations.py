from odoo import models, fields, api


class AirportAmbulanceReceiveFeeSituations(models.Model):
    _name = 'airport.ambulance.receive.fee.situations'
    _description = 'Airport Ambulance Receive Fee Situations'

    name = fields.Char(string='收費情況名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'receive_fee_situations_id')