from odoo import models, fields, api


class AirportAmbulanceNonTrauma(models.Model):
    _name = 'airport.ambulance.non.trauma'
    _description = 'Airport Ambulance Non Trauma'

    name = fields.Char(string='非創傷名稱')