from odoo import models, fields


class AirportAmbulanceSex(models.Model):
    _name = 'airport.ambulance.sex'
    _description = 'Airport ambulance sex model'

    name = fields.Char(string='性別名稱')
    ambulance_table_ids = fields.One2many('airport.ambulance.table', 'sex_id')
