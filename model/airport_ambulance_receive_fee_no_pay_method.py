from odoo import models, fields, api


class AirportAmbulanceReceiveFeeNoPayMethod(models.Model):
    _name = 'airport.ambulance.receive.fee.no.pay.method'
    _description = 'Airport Ambulance Receive Fee No Pay Method'

    name = fields.Char(string='未收費的方式名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'receive_fee_no_pay_method_id')