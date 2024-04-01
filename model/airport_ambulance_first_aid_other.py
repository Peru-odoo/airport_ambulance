from odoo import models, fields, api


class AirportAmbulanceFirstAidOther(models.Model):
    _name = 'airport.ambulance.first.aid.other'
    _description = 'Airport Ambulance First Aid Other'

    name = fields.Char(string='其他處置名稱')