from odoo import models, fields, api


class AirportAmbulanceFirstAidDrugIv(models.Model):
    _name = 'airport.ambulance.first.aid.drug.iv'
    _description = 'Airport Ambulance First Aid Drug Intravenous Infusion'

    name = fields.Char(string='靜脈輸液名稱')