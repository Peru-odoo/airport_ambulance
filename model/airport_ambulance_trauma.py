from odoo import models, fields, api


class AirportAmbulanceTrauma(models.Model):
    _name = 'airport.ambulance.trauma'
    _description = 'Airport Ambulance Trauma'

    name = fields.Char(string='創傷名稱')