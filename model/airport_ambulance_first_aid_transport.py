from odoo import models, fields, api


class AirportAmbulanceFirstAidTransport(models.Model):
    _name = 'airport.ambulance.first.aid.transport'
    _description = 'Airport Ambulance First Aid Transport'

    name = fields.Char(string='搬運名稱')