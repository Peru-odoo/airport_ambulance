from odoo import models, fields, api


class AirportAmbulanceFirstAid(models.Model):
    _name = 'airport.ambulance.first.aid'
    _description = 'Airport Ambulance First Aid'

    name = fields.Char(string='急救處置名稱')