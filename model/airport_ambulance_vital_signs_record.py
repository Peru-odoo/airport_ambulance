from odoo import models, fields, api
import datetime


class AirportAmbulanceVitalSignsRecord(models.Model):
    _name = 'airport.ambulance.vital.signs.record'
    _description = 'Airport Ambulance Vital Signs Record'

    record_time = fields.Datetime(string='紀錄時間', default=lambda self: fields.Datetime.now())
    record_time_str = fields.Char(string='紀錄時間字串', compute='_compute_record_time_str', store=True)
    record_time_final = fields.Char(string='紀錄時間(最終)', compute='_compute_record_time_final', store=True)
    arrive_triage_station = fields.Selection([('yes', '是'), ('no', '否')], string='是否抵達到院後檢傷站', default='no')
    conscious_situation = fields.Selection([('alert', '清'), 
                                            ('voice', '聲'), 
                                            ('pain', '痛'),
                                            ('unresponsive', '否')], string='意識狀態')
    temperature = fields.Char(string='體溫')
    palse = fields.Char(string='脈搏')
    breath = fields.Char(string='呼吸')
    blood_pressure = fields.Char(string='血壓')
    sp02 = fields.Char(string='血氧')
    gcs_e = fields.Char(string='GCS-E')
    gcs_v = fields.Char(string='GCS-V')
    gcs_m = fields.Char(string='GCS-M')
    gcs_final = fields.Char(string='最終的GCS', compute='_compute_gcs_final', store=True)
    ambulance_table_id = fields.Many2one('airport.ambulance.table', string='救護車單紀錄')

    # 按下按鈕更新紀錄時間
    def btn_refresh_record_time(self):
        self.record_time = fields.Datetime.now()

    # 從紀錄時間取出時與分
    @api.depends('record_time')
    def _compute_record_time_str(self):
        for record in self:
            record.record_time_str = (record.record_time + datetime.timedelta(hours=8)).strftime('%H:%M')

    # 當抵達到院後檢傷站時，紀錄時間會變成到院後檢傷站
    @api.depends('record_time', 'arrive_triage_station')
    def _compute_record_time_final(self):
        for record in self:
            if record.arrive_triage_station:
                if record.arrive_triage_station == 'yes':
                    record.record_time_final = '到院後檢傷站'
                else:
                    record.record_time_final = (record.record_time + datetime.timedelta(hours=8)).strftime('%Y年%m月%d日 %H時%M分%S秒')
            else:
                record.record_time_final = (record.record_time + datetime.timedelta(hours=8)).strftime('%Y年%m月%d日 %H時%M分%S秒')

    # 將gcs_e, gcs_v, gcs_m的值合併成gcs_final
    @api.depends('gcs_e', 'gcs_v', 'gcs_m')
    def _compute_gcs_final(self):
        for record in self:
            temp = ''
            if record.gcs_e:
                temp += 'E:{} '.format(record.gcs_e)
            if record.gcs_v:
                temp += 'V:{} '.format(record.gcs_v)
            if record.gcs_m:
                temp += 'M:{} '.format(record.gcs_m)
            record.gcs_final = temp