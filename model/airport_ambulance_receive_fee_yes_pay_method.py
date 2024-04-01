from odoo import api, fields, models


class AirportAmbulanceReceiveFeeYesPayMethod(models.Model):
    _name = 'airport.ambulance.receive.fee.yes.pay.method'
    _description = 'Airport Ambulance Receive Fee Yes Pay Method'

    name = fields.Char(string='已收費方式的名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'receive_fee_yes_pay_method_id')