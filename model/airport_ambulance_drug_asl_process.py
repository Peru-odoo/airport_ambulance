from odoo import models, fields, api


class AirportAmbulanceDrugAslProcess(models.Model):
    _name = 'airport.ambulance.drug.asl.process'
    _description = 'Airport Ambulance Drug ASL Process'

    name = fields.Char(string='ASL處置名稱')
    