from odoo import models, fields, api

class AirportAmbulanceFirstAidTrauma(models.Model):
    _name = 'airport.ambulance.first.aid.trauma'
    _description = 'Airport Ambulance First Aid Trauma'

    name = fields.Char(string='創傷處置名稱')