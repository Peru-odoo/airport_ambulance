from odoo import models, fields, api
import datetime


class AirportAmbulanceDrugRecord(models.Model):
    _name = 'airport.ambulance.drug.record'
    _description = 'Airport Ambulance Drug Record'

    name = fields.Char(string='藥名')
    given_time = fields.Datetime(string='給藥時間', default=lambda self: fields.Datetime.now())
    given_time_str = fields.Char(string='給藥時間字串', compute='_compute_given_time_str', store=True)
    given_method = fields.Char(string='給藥途徑')
    given_dose = fields.Char(string='給藥劑量')
    given_who = fields.Char(string='執行者')
    ambulance_table_id = fields.Many2one('airport.ambulance.table', string='救護車單紀錄')

    # 按下按鈕更新給藥時間
    def btn_refresh_given_time(self):
        self.given_time = fields.Datetime.now()

    # 從給藥時間取出時與分
    @api.depends('given_time')
    def _compute_given_time_str(self):
        for record in self:
            record.given_time_str = (record.given_time + datetime.timedelta(hours=8)).strftime('%H:%M')
