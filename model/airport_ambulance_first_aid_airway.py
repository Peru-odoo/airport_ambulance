from odoo import models, fields, api


class AirportAmbulanceFirstAidAirway(models.Model):
    _name = 'airport.ambulance.first.aid.airway'
    _description = 'Airport Ambulance First Aid Airway'

    name = fields.Char(string='呼吸道處置名稱')