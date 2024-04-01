from odoo import models, fields, api


class AirportAmbulanceNonTraumaEmergency(models.Model):
    _name = 'airport.ambulance.non.trauma.emergency'
    _description = 'Airport Ambulance Non Trauma Emergency'

    name = fields.Char(string='急症名稱')