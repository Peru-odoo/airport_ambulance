from odoo import models, fields, api


class AirportAmbulanceTraumaMoi(models.Model):
    _name = 'airport.ambulance.trauma.moi'
    _description = 'Airport Ambulance Trauma Mechanism of Injury'

    name = fields.Char(string='受傷機轉名稱')