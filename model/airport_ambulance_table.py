from odoo import models, fields, api
import datetime


class AirportAmbulanceTable(models.Model):
    _name = 'airport.ambulance.table'
    _description = 'Airport Ambulance Table'

    name = fields.Char(string='姓名')
    sex_id = fields.Many2one('airport.ambulance.sex', string='性別')
    id_or_passport = fields.Char(string='身分證字號或護照號碼')
    age = fields.Integer(string='年齡')
    address = fields.Char(string='地址')
    property_handed = fields.Selection([('no', '未經手'), ('yes', '有')], string='患者財物經手')
    property_detail = fields.Text(string='病患財物明細')
    custodian_name = fields.Char(string='保管人姓名')
    custodian_sign = fields.Binary(string='保管人簽名')
    plate_number = fields.Char(string='車牌號碼')
    attendance_datetime = fields.Datetime(string='出勤日期與時間', default=lambda self: fields.Datetime.now())
    attendance_datetime_strf = fields.Char(string='出勤日期與時間字串', compute='_compute_attendance_datetime_strf', store=True)
    attendance_datetime_strf_date = fields.Char(string='出勤日期與時間字串(日期)', compute='_compute_attendance_datetime_strf', store=True)
    arrival_scene_datetime = fields.Datetime(string='到達現場日期與時間', default=lambda self: fields.Datetime.now())
    arrival_scene_datetime_strf = fields.Char(string='到達現場日期與時間字串', compute='_compute_arrival_scene_datetime_strf', store=True)
    leave_scene_datetime = fields.Datetime(string='離開現場日期與時間', default=lambda self: fields.Datetime.now())
    leave_scene_datetime_strf = fields.Char(string='離開現場日期與時間字串', compute='_compute_leave_scene_datetime_strf', store=True)
    arrival_hospital_datetime = fields.Datetime(string='到達醫院日期與時間', default=lambda self: fields.Datetime.now())
    arrival_hospital_datetime_strf = fields.Char(string='到達醫院日期與時間字串', compute='_compute_arrival_hospital_datetime_strf', store=True)
    leave_hospital_datetime = fields.Datetime(string='離開醫院日期與時間', default=lambda self: fields.Datetime.now())
    leave_hospital_datetime_strf = fields.Char(string='離開醫院日期與時間字串', compute='_compute_leave_hospital_datetime_strf', store=True)
    return_datetime = fields.Datetime(string='返回待命日期與時間', default=lambda self: fields.Datetime.now())
    return_datetime_strf = fields.Char(string='返回待命日期與時間字串', compute='_compute_return_datetime_strf', store=True)
    incident_place_category_id = fields.Many2one('airport.medical.incident.place.category', string='發生地點類別')
    incident_place_category_2_id = fields.Many2one('airport.medical.incident.place.category.2', string='發生地點類別2')
    incident_place_t11_id = fields.Many2one('airport.medical.incident.place.t1.1', string='發生地點-第一航廈-1')
    incident_place_t12_id = fields.Many2one('airport.medical.incident.place.t1.2', string='發生地點-第一航廈-2')
    incident_place_t13_id = fields.Many2one('airport.medical.incident.place.t1.3', string='發生地點-第一航廈-3')
    incident_place_t14_id = fields.Many2one('airport.medical.incident.place.t1.4', string='發生地點-第一航廈-4')
    incident_place_t21_id = fields.Many2one('airport.medical.incident.place.t2.1', string='發生地點-第二航廈-1')
    incident_place_t22_id = fields.Many2one('airport.medical.incident.place.t2.2', string='發生地點-第二航廈-2')
    incident_place_t23_id = fields.Many2one('airport.medical.incident.place.t2.3', string='發生地點-第二航廈-3')
    incident_place_t24_id = fields.Many2one('airport.medical.incident.place.t2.4', string='發生地點-第二航廈-4')
    incident_place_ra1_id = fields.Many2one('airport.medical.incident.place.ra.1', string='發生地點-遠端機坪-1')
    incident_place_ra2_id = fields.Many2one('airport.medical.incident.place.ra.2', string='發生地點-遠端機坪-2')
    incident_place_ra3_id = fields.Many2one('airport.medical.incident.place.ra.3', string='發生地點-遠端機坪-3')
    incident_place_ra4_id = fields.Many2one('airport.medical.incident.place.ra.4', string='發生地點-遠端機坪-4')
    incident_place_cfs1_id = fields.Many2one('airport.medical.incident.place.cfs.1', string='發生地點-貨運站/機坪其他-1')
    incident_place_cfs2_id = fields.Many2one('airport.medical.incident.place.cfs.2', string='發生地點-貨運站/機坪其他-2')
    incident_place_cfs3_id = fields.Many2one('airport.medical.incident.place.cfs.3', string='發生地點-貨運站/機坪其他-3')
    incident_place_cfs4_id = fields.Many2one('airport.medical.incident.place.cfs.4', string='發生地點-貨運站/機坪其他-4')
    incident_place_nh_id = fields.Many2one('airport.medical.incident.place.nh', string='發生地點-諾富特飯店')
    incident_place_cabin_id = fields.Many2one('airport.medical.incident.place.cabin', string='發生地點-飛機機艙內')
    incident_place_other = fields.Char(string='發生地點-其他')
    incident_place_final = fields.Char(compute='_compute_incident_place_other', store=True, readonly=False, string='最終的發生地點')
    transport_hospital_or_place_id = fields.Many2one('airport.medical.ambulance.referral', string='送往醫院或地點')
    transport_hospital_or_place_other = fields.Char(string='送往其他醫院或地點')
    transport_hospital_or_place_final = fields.Char(string='最終送往醫院或地點', compute='_compute_transport_hospital_or_place_final', store=True)
    transport_reason_id = fields.Many2one('airport.ambulance.transport.reason', string='運送原因')
    trauma_classification_ids = fields.Many2many('airport.ambulance.trauma.classification', 
                                                 'airport_ambulance_trauma_classification_rel', 
                                                 'ambulance_table_id', 
                                                 'trauma_classification_id', string='創傷類別')
    trauma_classification_is_choose_non_trauma = fields.Boolean(string='創傷類別是否選擇非創傷')
    non_trauma_ids = fields.Many2many('airport.ambulance.non.trauma', 
                                      'airport_ambulance_non_trauma_rel', 
                                      'ambulance_table_id',
                                      'non_trauma_id', string='非創傷類別')
    non_trauma_is_choose_emergency = fields.Boolean(string='非創傷類別是否選擇急症')
    non_trauma_emergency_ids = fields.Many2many('airport.ambulance.non.trauma.emergency', 
                                                'airport_ambulance_non_trauma_emergency_rel', 
                                                'ambulance_table_id',
                                                'non_trauma_emergency_id', string='非創傷急症')
    non_trauma_emergency_is_choose_other = fields.Boolean(string='非創傷急症是否選擇其他')
    non_trauma_emergency_other = fields.Char(string='非創傷急症其他')
    non_trauma_is_choose_general = fields.Boolean(string='非創傷是否選擇一般疾病')
    non_trauma_general_ids = fields.Many2many('airport.ambulance.non.trauma.general',   
                                              'airport_ambulance_non_trauma_general_rel', 
                                              'ambulance_table_id',
                                              'non_trauma_general_id', string='非創傷一般疾病')
    trauma_classification_is_choose_trauma = fields.Boolean(string='創傷類別是否選擇創傷')
    trauma_ids = fields.Many2many('airport.ambulance.trauma', 
                                  'airport_ambulance_trauma_rel', 
                                  'ambulance_table_id',
                                  'trauma_id', string='創傷類別')
    trauma_is_choose_general = fields.Boolean(string='創傷是否選擇一般外傷')
    trauma_general_ids = fields.Many2many('airport.ambulance.trauma.general', 
                                          'airport_ambulance_trauma_general_rel', 
                                          'ambulance_table_id', 
                                          'trauma_general_id', string='創傷一般外傷')
    trauma_general_is_choose_other = fields.Boolean(string='創傷一般外傷是否選擇其他')
    trauma_general_other = fields.Char(string='創傷一般外傷其他')
    trauma_is_choose_mechanism_of_injury = fields.Boolean(string='創傷是否選擇受傷機轉')
    trauma_mechanism_of_injury_ids = fields.Many2many('airport.ambulance.trauma.moi', 
                                                      'airport_ambulance_trauma_moi_rel', 
                                                      'ambulance_table_id', 
                                                      'trauma_moi_id', string='創傷受傷機轉') 
    trauma_is_choose_fall = fields.Boolean(string='創傷是否選擇墜落')
    trauma_fall_distance = fields.Char(string='墜落高度')
    trauma_is_choose_burns = fields.Boolean(string='創傷是否選擇燒燙傷')
    trauma_burns_degree = fields.Char(string='燒燙傷程度')
    trauma_burns_area = fields.Char(string='燒燙傷面積')
    trauma_is_choose_other = fields.Boolean(string='創傷是否選擇其他')
    trauma_other = fields.Char(string='創傷其他')
    allergy_ids = fields.Many2many('airport.ambulance.allergy', 
                                   'airport_ambulance_allergy_rel', 
                                   'ambulance_table_id', 
                                   'allergy_id', string='過敏史')
    allergy_is_choose_food = fields.Boolean(string='過敏史是否選擇食物')
    allergy_food = fields.Char(string='過敏食物')
    allergy_is_choose_drug = fields.Boolean(string='過敏史是否選擇藥物')
    allergy_drug = fields.Char(string='過敏藥物')
    allergy_is_choose_other = fields.Boolean(string='過敏史是否選擇其他')
    allergy_other = fields.Char(string='其他過敏史')
    chief_complaint = fields.Text(string='主訴')
    chief_complaint_is_telled_by_other = fields.Selection([('no', '否'), ('yes', '是')], string='主訴是否由他人代訴')
    past_history_ids = fields.Many2many('airport.ambulance.past.history', 
                                        'airport_ambulance_past_history_rel', 
                                        'ambulance_table_id', 
                                        'past_history_id', string='過去病史')
    past_history_is_choose_other = fields.Boolean(string='過去病史是否選擇其他')
    past_history_other = fields.Char(string='過去病史其他')
    first_aid_ids = fields.Many2many('airport.ambulance.first.aid', 
                                     'airport_ambulance_first_aid_rel', 
                                     'ambulance_table_id', 
                                     'first_aid_id', string='急救處置')
    first_aid_is_choose_airway = fields.Boolean(string='急救處置是否選擇呼吸道處置')
    first_aid_airway_ids = fields.Many2many('airport.ambulance.first.aid.airway', 
                                            'airport_ambulance_first_aid_airway_rel', 
                                            'ambulance_table_id', 
                                            'first_aid_airway_id', string='呼吸道處置')
    first_aid_airway_is_choose_nose = fields.Boolean(string='呼吸道處置是否選擇鼻管')
    first_aid_airway_nose_flow = fields.Char(string='鼻管流量')
    first_aid_airway_is_choose_mask = fields.Boolean(string='呼吸道處置是否選擇面罩')
    first_aid_airway_mask_flow = fields.Char(string='面罩流量')
    first_aid_airway_is_choose_lma = fields.Boolean(string='呼吸道處置是否選擇LMA')
    first_aid_airway_lma_size = fields.Char(string='LMA號碼')
    first_aid_airway_is_choose_igel = fields.Boolean(string='呼吸道處置是否選擇Igel')
    first_aid_airway_igel_size = fields.Char(string='Igel號碼')
    first_aid_airway_is_choose_et = fields.Boolean(string='呼吸道處置是否選擇氣管內管')
    first_aid_airway_et_size = fields.Char(string='氣管內管號碼')
    first_aid_airway_is_choose_other = fields.Boolean(string='呼吸道處置是否選擇其他')
    first_aid_airway_other = fields.Char(string='呼吸道處置其他')
    first_aid_is_choose_trauma = fields.Boolean(string='急救處置是否選擇創傷處置')
    first_aid_trauma_ids = fields.Many2many('airport.ambulance.first.aid.trauma', 
                                            'airport_ambulance_first_aid_trauma_rel', 
                                            'ambulance_table_id', 
                                            'first_aid_trauma_id', string='創傷處置')
    first_aid_trauma_is_choose_other = fields.Boolean(string='創傷處置是否選擇其他')
    first_aid_trauma_other = fields.Char(string='創傷處置其他')
    first_aid_is_choose_transport = fields.Boolean(string='急救處置是否選擇搬運')
    first_aid_transport_ids = fields.Many2many('airport.ambulance.first.aid.transport', 
                                               'airport_ambulance_first_aid_transport_rel', 
                                               'ambulance_table_id', 
                                               'first_aid_transport_id', string='搬運')
    first_aid_is_choose_cpr = fields.Boolean(string='急救處置是否選擇心肺復甦術')
    first_aid_cpr_ids = fields.Many2many('airport.ambulance.first.aid.cpr', 
                                         'airport_ambulance_first_aid_cpr_rel', 
                                         'ambulance_table_id', 
                                         'first_aid_cpr_id', string='心肺復甦術')
    first_aid_cpr_is_choose_cpr = fields.Boolean(string='心肺復甦術是否選擇CPR')
    first_aid_cpr_cpr_minutes = fields.Char(string='CPR分鐘數')
    first_aid_cpr_is_choose_aed = fields.Boolean(string='心肺復甦術是否選擇使用AED')
    first_aid_cpr_aed_ids = fields.Many2many('airport.ambulance.first.aid.cpr.aed',
                                             'airport_ambulance_first_aid_cpr_aed_rel', 
                                             'ambulance_table_id', 
                                             'first_aid_cpr_aed_id', string='使用AED')
    first_aid_cpr_aed_is_choose_elect = fields.Boolean(string='使用AED是否選擇電擊去顫')
    first_aid_cpr_aed_elect_times = fields.Char(string='電擊去顫次數')
    first_aid_is_choose_drug = fields.Boolean(string='急救處置是否選擇藥物處置')
    first_aid_drug_ids = fields.Many2many('airport.ambulance.first.aid.drug', 
                                          'airport_ambulance_first_aid_drug_rel', 
                                          'ambulance_table_id', 
                                          'first_aid_drug_id', string='藥物處置')
    first_aid_drug_is_choose_iv = fields.Boolean(string='藥物處置是否選擇靜脈輸液')
    first_aid_drug_iv_body_part = fields.Char(string='靜脈輸液部位')
    first_aid_drug_iv_ids = fields.Many2many('airport.ambulance.first.aid.drug.iv', 
                                             'airport_ambulance_first_aid_drug_iv_rel', 
                                             'ambulance_table_id', 
                                             'first_aid_drug_iv_id', string='靜脈輸液')
    first_aid_drug_iv_is_choose_ns = fields.Boolean(string='靜脈輸液是否選擇0.9%N/S')
    first_aid_drug_iv_ns_ml = fields.Char(string='0.9%N/S使用ml')
    first_aid_drug_iv_is_choose_lr = fields.Boolean(string='靜脈輸液是否選擇LR')
    first_aid_drug_iv_lr_ml = fields.Char(string='LR使用ml')
    first_aid_drug_iv_is_choose_gs = fields.Boolean(string='靜脈輸液是否選擇葡萄糖液')
    first_aid_drug_iv_gs_type = fields.Char(string='葡萄糖液種類')
    first_aid_drug_iv_gs_ml = fields.Char(string='葡萄糖液使用ml')
    first_aid_drug_is_choose_ntg = fields.Boolean(string='藥物處置是否選擇NTG')
    first_aid_drug_ntg_pieces = fields.Char(string='NTG使用片數')
    first_aid_drug_is_choose_bronchodilator = fields.Boolean(string='藥物處置是否選擇支氣管擴張劑')
    first_aid_drug_bronchodilator_times = fields.Char(string='支氣管擴張劑使用次數')
    first_aid_is_choose_other = fields.Boolean(string='急救處置是否選擇其他處置')
    first_aid_other_ids = fields.Many2many('airport.ambulance.first.aid.other', 
                                           'airport_ambulance_first_aid_other_rel', 
                                           'ambulance_table_id', 
                                           'first_aid_other_id', string='其他處置')
    first_aid_other_is_choose_other = fields.Boolean(string='其他處置是否選擇其他')
    first_aid_other_other = fields.Char(string='其他處置')
    human_body_image_note = fields.Text(string='人體圖備註')
    drug_record_ids = fields.One2many('airport.ambulance.drug.record', 'ambulance_table_id', string='藥物紀錄')
    drug_asl_process_ids = fields.Many2many('airport.ambulance.drug.asl.process', 
                                            'airport_ambulance_drug_asl_process_rel', 
                                            'ambulance_table_id', 
                                            'drug_asl_process_id', string='ASL處置')
    drug_asl_process_is_choose_on_tube = fields.Boolean(string='ASL處置是否選擇氣管內管')
    drug_asl_process_on_tube_size = fields.Char(string='氣管內管號碼')
    drug_asl_process_on_tube_fix_cm = fields.Char(string='氣管內管固定長度')
    drug_asl_process_is_choose_elect = fields.Boolean(string='ASL處置是否選擇手動電擊')
    drug_asl_process_elect_times = fields.Char(string='手動電擊次數')
    drug_asl_process_elect_joule = fields.Char(string='手動電擊焦耳')
    drug_online_mentor_illustration = fields.Text(string='線上指導醫師指導說明')
    vital_signs_record_ids = fields.One2many('airport.ambulance.vital.signs.record', 'ambulance_table_id', string='生命徵象紀錄')
    attending_crew_ids = fields.One2many('airport.ambulance.attending.crews.record', 'ambulance_table_id', string='隨車救護人員記錄')
    receive_unit = fields.Char(string='接收單位')
    receive_unit_sign = fields.Binary(string='接收單位簽名')
    receive_unit_datetime = fields.Datetime(string='接收時間', default=lambda self: fields.Datetime.now())
    receive_unit_datetime_str = fields.Char(string='接收時間字串', compute='_compute_receive_unit_datetime_str', store=True)
    reject_transport = fields.Selection([('no', '否'), ('yes', '是')], string='拒絕送醫', default='no')
    reject_transport_name = fields.Char(string='拒絕送醫姓名', compute='_compute_reject_transport_name', store=True, readonly=False)
    reject_transport_sign = fields.Binary(string='拒絕送醫簽名')
    relation_name = fields.Char(string='關係人姓名')
    relation_identity_id = fields.Many2one('airport.ambulance.relation.identity', string='關係人身分')
    relation_phone = fields.Char(string='關係人聯絡電話')
    relation_sign = fields.Binary(string='關係人簽名')
    ambulance_fee = fields.Char(string='救護車費用')
    oxygen_fee = fields.Char(string='氧氣使用費用')
    total_fee = fields.Integer(string='總費用', compute='_compute_total_fee', store=True)
    receive_fee_situations_id = fields.Many2one('airport.ambulance.receive.fee.situations', string='收費情況')
    receive_fee_yes_pay_method_id = fields.Many2one('airport.ambulance.receive.fee.yes.pay.method', string='已收費方式')
    receive_fee_no_pay_method_id = fields.Many2one('airport.ambulance.receive.fee.no.pay.method', string='未收費方式')
    receive_fee_no_pay_method_request_target = fields.Char(string='統一請款對象')
    human_body_image = fields.Binary(string='人形圖', compute='_compute_human_body_image', store=True)
    human_body_image_encode = fields.Char(string='人形圖編碼')

    # 處理當發生地點分類1已點擊後，要點擊發生地點分類2時的邏輯問題
    @api.onchange('incident_place_category_id')
    def _onchange_incident_place_category_id(self):
        if self.incident_place_category_id:
            self.incident_place_category_2_id = ''
            self.incident_place_t11_id = ''
            self.incident_place_t12_id = ''
            self.incident_place_t13_id = ''
            self.incident_place_t14_id = ''
            self.incident_place_t21_id = ''
            self.incident_place_t22_id = ''
            self.incident_place_t23_id = ''
            self.incident_place_t24_id = ''
            self.incident_place_ra1_id = ''
            self.incident_place_ra2_id = ''
            self.incident_place_ra3_id = ''
            self.incident_place_ra4_id = ''
            self.incident_place_cfs1_id = ''
            self.incident_place_cfs2_id = ''
            self.incident_place_cfs3_id = ''
            self.incident_place_cfs4_id = ''
            self.incident_place_nh_id = ''
            self.incident_place_cabin_id = ''
            self.incident_place_other = ''
            self.incident_place_final = ''

    # 處理當發生地點分類2已點擊後，要點擊發生地點分類1時的邏輯問題
    @api.onchange('incident_place_category_2_id')
    def _onchange_incident_place_category_2_id(self):
        if self.incident_place_category_2_id:
            self.incident_place_category_id = ''
            self.incident_place_t11_id = ''
            self.incident_place_t12_id = ''
            self.incident_place_t13_id = ''
            self.incident_place_t14_id = ''
            self.incident_place_t21_id = ''
            self.incident_place_t22_id = ''
            self.incident_place_t23_id = ''
            self.incident_place_t24_id = ''
            self.incident_place_ra1_id = ''
            self.incident_place_ra2_id = ''
            self.incident_place_ra3_id = ''
            self.incident_place_ra4_id = ''
            self.incident_place_cfs1_id = ''
            self.incident_place_cfs2_id = ''
            self.incident_place_cfs3_id = ''
            self.incident_place_cfs4_id = ''
            self.incident_place_nh_id = ''
            self.incident_place_cabin_id = ''
            self.incident_place_other = ''
            self.incident_place_final = ''

    # 處理T1已點擊後，要點擊其他T1列表選項時的邏輯問題
    @api.onchange('incident_place_t11_id')
    def _onchange_incident_place_t11_id(self):
        if self.incident_place_t11_id:
            self.incident_place_final = '第一航廈 - ' + str(self.env['airport.medical.incident.place.t1.1'].search([('id', '=', self.incident_place_t11_id.id)]).name)
            self.incident_place_t12_id = ''
            self.incident_place_t13_id = ''
            self.incident_place_t14_id = ''
            self.incident_place_other = ''
    
    # 處理T1已點擊後，要點擊其他T1列表選項時的邏輯問題
    @api.onchange('incident_place_t12_id')
    def _onchange_incident_place_t12_id(self):
        if self.incident_place_t12_id:
            self.incident_place_final = '第一航廈 - ' + str(self.env['airport.medical.incident.place.t1.2'].search([('id', '=', self.incident_place_t12_id.id)]).name)
            self.incident_place_t11_id = ''
            self.incident_place_t13_id = ''
            self.incident_place_t14_id = ''
            self.incident_place_other = ''

    # 處理T1已點擊後，要點擊其他T1列表選項時的邏輯問題
    @api.onchange('incident_place_t13_id')
    def _onchange_incident_place_t13_id(self):
        if self.incident_place_t13_id:
            self.incident_place_final = '第一航廈 - ' + str(self.env['airport.medical.incident.place.t1.3'].search([('id', '=', self.incident_place_t13_id.id)]).name)
            self.incident_place_t11_id = ''
            self.incident_place_t12_id = ''
            self.incident_place_t14_id = ''
            self.incident_place_other = ''

    # 處理T1已點擊後，要點擊其他T1列表選項時的邏輯問題
    @api.onchange('incident_place_t14_id')
    def _onchange_incident_place_t14_id(self):
        if self.incident_place_t14_id:
            self.incident_place_final = '第一航廈 - ' + str(self.env['airport.medical.incident.place.t1.4'].search([('id', '=', self.incident_place_t14_id.id)]).name)
            self.incident_place_t11_id = ''
            self.incident_place_t12_id = ''
            self.incident_place_t13_id = ''
            self.incident_place_other = ''

    # 處理T2已點擊後，要點擊其他T2列表選項時的邏輯問題
    @api.onchange('incident_place_t21_id')
    def _onchange_incident_place_t21_id(self):
        if self.incident_place_t21_id:
            self.incident_place_final = '第二航廈 - ' + str(self.env['airport.medical.incident.place.t2.1'].search([('id', '=', self.incident_place_t21_id.id)]).name)
            self.incident_place_t22_id = ''
            self.incident_place_t23_id = ''
            self.incident_place_t24_id = ''
            self.incident_place_other = ''
    
    # 處理T2已點擊後，要點擊其他T2列表選項時的邏輯問題
    @api.onchange('incident_place_t22_id')
    def _onchange_incident_place_t22_id(self):
        if self.incident_place_t22_id:
            self.incident_place_final = '第二航廈 - ' + str(self.env['airport.medical.incident.place.t2.2'].search([('id', '=', self.incident_place_t22_id.id)]).name)
            self.incident_place_t21_id = ''
            self.incident_place_t23_id = ''
            self.incident_place_t24_id = ''
            self.incident_place_other = ''

    # 處理T2已點擊後，要點擊其他T2列表選項時的邏輯問題
    @api.onchange('incident_place_t23_id')
    def _onchange_incident_place_t23_id(self):
        if self.incident_place_t23_id:
            self.incident_place_final = '第二航廈 - ' + str(self.env['airport.medical.incident.place.t2.3'].search([('id', '=', self.incident_place_t23_id.id)]).name)
            self.incident_place_t21_id = ''
            self.incident_place_t22_id = ''
            self.incident_place_t24_id = ''
            self.incident_place_other = ''

    # 處理T2已點擊後，要點擊其他T2列表選項時的邏輯問題
    @api.onchange('incident_place_t24_id')
    def _onchange_incident_place_t24_id(self):
        if self.incident_place_t24_id:
            self.incident_place_final = '第二航廈 - ' + str(self.env['airport.medical.incident.place.t2.4'].search([('id', '=', self.incident_place_t24_id.id)]).name)
            self.incident_place_t21_id = ''
            self.incident_place_t22_id = ''
            self.incident_place_t23_id = ''
            self.incident_place_other = ''

    # 處理Ra已點擊後，要點擊其他Ra列表選項時的邏輯問題
    @api.onchange('incident_place_ra1_id')
    def _onchange_incident_place_ra1_id(self):
        if self.incident_place_ra1_id:
            self.incident_place_final = '遠端機坪 - ' + str(self.env['airport.medical.incident.place.ra.1'].search([('id', '=', self.incident_place_ra1_id.id)]).name)
            self.incident_place_ra2_id = ''
            self.incident_place_ra3_id = ''
            self.incident_place_ra4_id = ''
            self.incident_place_other = ''

    # 處理Ra已點擊後，要點擊其他Ra列表選項時的邏輯問題
    @api.onchange('incident_place_ra2_id')
    def _onchange_incident_place_ra2_id(self):
        if self.incident_place_ra2_id:
            self.incident_place_final = '遠端機坪 - ' + str(self.env['airport.medical.incident.place.ra.2'].search([('id', '=', self.incident_place_ra2_id.id)]).name)
            self.incident_place_ra1_id = ''
            self.incident_place_ra3_id = ''
            self.incident_place_ra4_id = ''
            self.incident_place_other = ''

    # 處理Ra已點擊後，要點擊其他Ra列表選項時的邏輯問題
    @api.onchange('incident_place_ra3_id')
    def _onchange_incident_place_ra3_id(self):
        if self.incident_place_ra3_id:
            self.incident_place_final = '遠端機坪 - ' + str(self.env['airport.medical.incident.place.ra.3'].search([('id', '=', self.incident_place_ra3_id.id)]).name)
            self.incident_place_ra1_id = ''
            self.incident_place_ra2_id = ''
            self.incident_place_ra4_id = ''
            self.incident_place_other = ''

    # 處理Ra已點擊後，要點擊其他Ra列表選項時的邏輯問題
    @api.onchange('incident_place_ra4_id')
    def _onchange_incident_place_ra4_id(self):
        if self.incident_place_ra4_id:
            self.incident_place_final = '遠端機坪 - ' + str(self.env['airport.medical.incident.place.ra.4'].search([('id', '=', self.incident_place_ra4_id.id)]).name)
            self.incident_place_ra1_id = ''
            self.incident_place_ra2_id = ''
            self.incident_place_ra3_id = ''
            self.incident_place_other = ''

    # 處理Cfs已點擊後，要點擊其他Cfs列表選項時的邏輯問題
    @api.onchange('incident_place_cfs1_id')
    def _onchange_incident_place_cfs1_id(self):
        if self.incident_place_cfs1_id:
            self.incident_place_final = '貨運站/機坪其他 - ' + str(self.env['airport.medical.incident.place.cfs.1'].search([('id', '=', self.incident_place_cfs1_id.id)]).name)
            self.incident_place_cfs2_id = ''
            self.incident_place_cfs3_id = ''
            self.incident_place_cfs4_id = ''
            self.incident_place_other = ''
            
    # 處理Cfs已點擊後，要點擊其他Cfs列表選項時的邏輯問題
    @api.onchange('incident_place_cfs2_id')
    def _onchange_incident_place_cfs2_id(self):
        if self.incident_place_cfs2_id:
            self.incident_place_final = '貨運站/機坪其他 - ' + str(self.env['airport.medical.incident.place.cfs.2'].search([('id', '=', self.incident_place_cfs2_id.id)]).name)
            self.incident_place_cfs1_id = ''
            self.incident_place_cfs3_id = ''
            self.incident_place_cfs4_id = ''
            self.incident_place_other = ''

    # 處理Cfs已點擊後，要點擊其他Cfs列表選項時的邏輯問題
    @api.onchange('incident_place_cfs3_id')
    def _onchange_incident_place_cfs3_id(self):
        if self.incident_place_cfs3_id:
            self.incident_place_final = '貨運站/機坪其他 - ' + str(self.env['airport.medical.incident.place.cfs.3'].search([('id', '=', self.incident_place_cfs3_id.id)]).name)
            self.incident_place_cfs1_id = ''
            self.incident_place_cfs2_id = ''
            self.incident_place_cfs4_id = ''
            self.incident_place_other = ''

    # 處理Cfs已點擊後，要點擊其他Cfs列表選項時的邏輯問題
    @api.onchange('incident_place_cfs4_id')
    def _onchange_incident_place_cfs4_id(self):
        if self.incident_place_cfs4_id:
            self.incident_place_final = '貨運站/機坪其他 - ' + str(self.env['airport.medical.incident.place.cfs.4'].search([('id', '=', self.incident_place_cfs4_id.id)]).name)
            self.incident_place_cfs1_id = ''
            self.incident_place_cfs2_id = ''
            self.incident_place_cfs3_id = ''
            self.incident_place_other = ''

    # 處理Nh已點擊後，組合出最終發生地點
    @api.onchange('incident_place_nh_id')
    def _onchange_incident_place_nh_id(self):
        if self.incident_place_nh_id:
            self.incident_place_final = '諾富特飯店 - ' + str(self.env['airport.medical.incident.place.nh'].search([('id', '=', self.incident_place_nh_id.id)]).name)

    # 處理Cabin，組合出最終發生地點
    @api.onchange('incident_place_cabin_id')
    def _onchange_incident_place_cabin_id(self):
        if self.incident_place_cabin_id:
            self.incident_place_final = '飛機機艙內 - ' + str(self.env['airport.medical.incident.place.cabin'].search([('id', '=', self.incident_place_cabin_id.id)]).name)

    # 將incident_place_other的內容加入到incident_place_final
    @api.depends('incident_place_other')
    def _compute_incident_place_other(self):
        if self.incident_place_other:
            if len(str(self.incident_place_other)) > 0:
                self.incident_place_final += ' - ' + str(self.incident_place_other)

    # 點擊送往醫院或地點的選項時，將送往其他醫院或地點的輸入框清空
    @api.onchange('transport_hospital_or_place_id')
    def _onchange_transport_hospital_or_place_id(self):
        if self.transport_hospital_or_place_id:
            self.transport_hospital_or_place_other = ''
            
    # 產生最終送往醫院或地點的字串
    @api.depends('transport_hospital_or_place_id', 'transport_hospital_or_place_other')
    def _compute_transport_hospital_or_place_final(self):
        for record in self:
            if record.transport_hospital_or_place_id:
                if record.transport_hospital_or_place_id.id != 10:
                    record.transport_hospital_or_place_final = record.transport_hospital_or_place_id.name
                else:
                    record.transport_hospital_or_place_final = record.transport_hospital_or_place_other

    # 按下按鈕更新出勤日期與時間
    def btn_refresh_attendance_datetime(self):
        self.attendance_datetime = fields.Datetime.now()

    # 從出勤日期與時間取出時與分
    @api.depends('attendance_datetime')
    def _compute_attendance_datetime_strf(self):
        for record in self:
            record.attendance_datetime_strf = (record.attendance_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')
            record.attendance_datetime_strf_date = (record.attendance_datetime + datetime.timedelta(hours=8)).strftime('西元%Y年%m月%d日')

    # 按下按鈕更新到達現場日期與時間
    def btn_refresh_arrival_scene_datetime(self):
        self.arrival_scene_datetime = fields.Datetime.now()
    
    # 從到達現場日期與時間取出時與分
    @api.depends('arrival_scene_datetime')
    def _compute_arrival_scene_datetime_strf(self):
        for record in self:
            record.arrival_scene_datetime_strf = (record.arrival_scene_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')
    
    # 按下按鈕更新離開現場日期與時間
    def btn_refresh_leave_scene_datetime(self):
        self.leave_scene_datetime = fields.Datetime.now()

    # 從離開現場日期與時間取出時與分
    @api.depends('leave_scene_datetime')
    def _compute_leave_scene_datetime_strf(self):
        for record in self:
            record.leave_scene_datetime_strf = (record.leave_scene_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')

    # 按下按鈕更新到達醫院日期與時間
    def btn_refresh_arrival_hospital_datetime(self):
        self.arrival_hospital_datetime = fields.Datetime.now()

    # 從到達醫院日期與時間取出時與分
    @api.depends('arrival_hospital_datetime')
    def _compute_arrival_hospital_datetime_strf(self):
        for record in self:
            record.arrival_hospital_datetime_strf = (record.arrival_hospital_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')

    # 按下按鈕更新離開醫院日期與時間
    def btn_refresh_leave_hospital_datetime(self):
        self.leave_hospital_datetime = fields.Datetime.now()

    # 從離開醫院日期與時間取出時與分
    @api.depends('leave_hospital_datetime')
    def _compute_leave_hospital_datetime_strf(self):
        for record in self:
            record.leave_hospital_datetime_strf = (record.leave_hospital_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')

    # 按下按鈕更新返回待命日期與時間
    def btn_refresh_return_datetime(self):
        self.return_datetime = fields.Datetime.now()

    # 從返回待命日期與時間取出時與分
    @api.depends('return_datetime')
    def _compute_return_datetime_strf(self):
        for record in self:
            record.return_datetime_strf = (record.return_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')
    
    # 開啟編輯人形圖頁面的按鈕
    def btn_open_edit_human_body_image_webpage(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'airport_ambulance/static/src/webpage/index.html',
            'target': 'new',
        }
    
    # 根據human_body_image_encode顯示人形圖
    @api.depends('human_body_image_encode')
    def _compute_human_body_image(self):
        for record in self:
            if record.human_body_image_encode:
                record.human_body_image = record.human_body_image_encode

    # 根據創傷類別勾選的項目，決定要顯示的列表
    @api.onchange('trauma_classification_ids')
    def _onchange_trauma_classification_ids(self):
        # 選擇非創傷
        if 1 in self.trauma_classification_ids.ids:
            self.trauma_classification_is_choose_non_trauma = True
        else:
            self.trauma_classification_is_choose_non_trauma = False
            self.non_trauma_ids = [(5, 0, 0)]
            self.non_trauma_is_choose_emergency = False
            self.non_trauma_emergency_ids = [(5, 0, 0)]
            self.non_trauma_emergency_is_choose_other = False
            self.non_trauma_emergency_other = ''
            self.non_trauma_is_choose_general = False
            self.non_trauma_general_ids = [(5, 0, 0)]
        # 選擇創傷
        if 2 in self.trauma_classification_ids.ids:
            self.trauma_classification_is_choose_trauma = True
        else:
            self.trauma_classification_is_choose_trauma = False
            self.trauma_ids = [(5, 0, 0)]
            self.trauma_is_choose_general = False
            self.trauma_general_ids = [(5, 0, 0)]
            self.trauma_general_is_choose_other = False
            self.trauma_general_other = ''
            self.trauma_is_choose_mechanism_of_injury = False
            self.trauma_mechanism_of_injury_ids = [(5, 0, 0)]
            self.trauma_is_choose_fall = False
            self.trauma_fall_distance = ''
            self.trauma_is_choose_burns = False
            self.trauma_burns_degree = ''
            self.trauma_burns_area = ''
            self.trauma_is_choose_other = False
            self.trauma_other = ''
    
    # 根據非創傷類別勾選的項目，決定要顯示的列表
    @api.onchange('non_trauma_ids')
    def _onchange_non_trauma_ids(self):
        # 選擇急症
        if 1 in self.non_trauma_ids.ids:
            self.non_trauma_is_choose_emergency = True
        else:
            self.non_trauma_is_choose_emergency = False
            self.non_trauma_emergency_ids = [(5, 0, 0)]
            self.non_trauma_emergency_is_choose_other = False
            self.non_trauma_emergency_other = ''
        # 選擇一般疾病
        if 2 in self.non_trauma_ids.ids:
            self.non_trauma_is_choose_general = True
        else:
            self.non_trauma_is_choose_general = False
            self.non_trauma_general_ids = [(5, 0, 0)]

    # 勾選非創傷急症的其他，才顯示其他欄位
    @api.onchange('non_trauma_emergency_ids')
    def _onchange_non_trauma_emergency_ids(self):
        if 13 in self.non_trauma_emergency_ids.ids:
            self.non_trauma_emergency_is_choose_other = True
        else:
            self.non_trauma_emergency_is_choose_other = False
            self.non_trauma_emergency_other = ''

    # 根據創傷類別勾選的項目，決定要顯示的列表
    @api.onchange('trauma_ids')
    def _onchange_trauma_ids(self):
        # 選擇一般外傷
        if 1 in self.trauma_ids.ids:
            self.trauma_is_choose_general = True
        else:
            self.trauma_is_choose_general = False
            self.trauma_general_ids = [(5, 0, 0)]
            self.trauma_general_is_choose_other = False
            self.trauma_general_other = ''
        # 選擇受傷機轉
        if 2 in self.trauma_ids.ids:
            self.trauma_is_choose_mechanism_of_injury = True
        else:
            self.trauma_is_choose_mechanism_of_injury = False
            self.trauma_mechanism_of_injury_ids = [(5, 0, 0)]
        # 選擇墜落
        if 5 in self.trauma_ids.ids:
            self.trauma_is_choose_fall = True
        else:
            self.trauma_is_choose_fall = False
            self.trauma_fall_distance = ''
        # 選擇燒燙傷
        if 7 in self.trauma_ids.ids:
            self.trauma_is_choose_burns = True
        else:
            self.trauma_is_choose_burns = False
            self.trauma_burns_degree = ''
            self.trauma_burns_area = ''
        # 選擇其他
        if 11 in self.trauma_ids.ids:
            self.trauma_is_choose_other = True
        else:
            self.trauma_is_choose_other = False
            self.trauma_other = ''

    # 勾選創傷一般外傷的其他，才顯示其他欄位
    @api.onchange('trauma_general_ids')
    def _onchange_trauma_general_ids(self):
        if 6 in self.trauma_general_ids.ids:
            self.trauma_general_is_choose_other = True
        else:
            self.trauma_general_is_choose_other = False
            self.trauma_general_other = ''

    # 根據過敏史勾選的項目，決定要顯示的列表
    @api.onchange('allergy_ids')
    def _onchange_allergy_ids(self):
        # 選擇食物
        if 3 in self.allergy_ids.ids:
            self.allergy_is_choose_food = True
        else:
            self.allergy_is_choose_food = False
            self.allergy_food = ''
        # 選擇藥物
        if 4 in self.allergy_ids.ids:
            self.allergy_is_choose_drug = True
        else:
            self.allergy_is_choose_drug = False
            self.allergy_drug = ''
        # 選擇其他
        if 5 in self.allergy_ids.ids:
            self.allergy_is_choose_other = True
        else:
            self.allergy_is_choose_other = False
            self.allergy_other = ''

    # 勾選過去病史的其他，才顯示其他欄位
    @api.onchange('past_history_ids')
    def _onchange_past_history_ids(self):
        if 11 in self.past_history_ids.ids:
            self.past_history_is_choose_other = True
        else:
            self.past_history_is_choose_other = False
            self.past_history_other = ''
    
    # 根據急救處置勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_ids')
    def _onchange_first_aid_ids(self):
        # 選擇呼吸道處置
        if 1 in self.first_aid_ids.ids:
            self.first_aid_is_choose_airway = True
        else:
            self.first_aid_is_choose_airway = False
            self.first_aid_airway_ids = [(5, 0, 0)]
            self.first_aid_airway_is_choose_nose = False
            self.first_aid_airway_nose_flow = ''
            self.first_aid_airway_is_choose_mask = False
            self.first_aid_airway_mask_flow = ''
            self.first_aid_airway_is_choose_lma = False
            self.first_aid_airway_lma_size = ''
            self.first_aid_airway_is_choose_igel = False
            self.first_aid_airway_igel_size = ''
            self.first_aid_airway_is_choose_et = False
            self.first_aid_airway_et_size = ''
            self.first_aid_airway_is_choose_other = False
            self.first_aid_airway_other = ''
        # 選擇創傷處置
        if 2 in self.first_aid_ids.ids:
            self.first_aid_is_choose_trauma = True
        else:
            self.first_aid_is_choose_trauma = False
            self.first_aid_trauma_ids = [(5, 0, 0)]
            self.first_aid_trauma_is_choose_other = False
            self.first_aid_trauma_other = ''
        # 選擇搬運
        if 3 in self.first_aid_ids.ids:
            self.first_aid_is_choose_transport = True
        else:
            self.first_aid_is_choose_transport = False
            self.first_aid_transport_ids = [(5, 0, 0)]
        # 選擇心肺復甦術
        if 4 in self.first_aid_ids.ids:
            self.first_aid_is_choose_cpr = True
        else:
            self.first_aid_is_choose_cpr = False
            self.first_aid_cpr_ids = [(5, 0, 0)]
            self.first_aid_cpr_is_choose_cpr = False
            self.first_aid_cpr_cpr_minutes = ''
            self.first_aid_cpr_is_choose_aed = False
            self.first_aid_cpr_aed_ids = [(5, 0, 0)]
            self.first_aid_cpr_aed_is_choose_elect = False
            self.first_aid_cpr_aed_elect_times = ''
        # 選擇藥物處置
        if 5 in self.first_aid_ids.ids:
            self.first_aid_is_choose_drug = True
        else:
            self.first_aid_is_choose_drug = False
            self.first_aid_drug_ids = [(5, 0, 0)]
            self.first_aid_drug_is_choose_iv = False
            self.first_aid_drug_iv_body_part = ''
            self.first_aid_drug_iv_ids = [(5, 0, 0)]
            self.first_aid_drug_iv_is_choose_ns = False
            self.first_aid_drug_iv_ns_ml = ''
            self.first_aid_drug_iv_is_choose_lr = False
            self.first_aid_drug_iv_lr_ml = ''
            self.first_aid_drug_iv_is_choose_gs = False
            self.first_aid_drug_iv_gs_type = ''
            self.first_aid_drug_iv_gs_ml = ''
            self.first_aid_drug_is_choose_ntg = False
            self.first_aid_drug_ntg_pieces = ''
            self.first_aid_drug_is_choose_bronchodilator = False
            self.first_aid_drug_bronchodilator_times = ''
        # 選擇其他處置
        if 6 in self.first_aid_ids.ids:
            self.first_aid_is_choose_other = True
        else:
            self.first_aid_is_choose_other = False
            self.first_aid_other_ids = [(5, 0, 0)]
            self.first_aid_other_is_choose_other = False
            self.first_aid_other_other = ''

    # 根據創傷處置勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_trauma_ids')
    def _onchange_first_aid_trauma_ids(self):
        # 選擇其他
        if 7 in self.first_aid_trauma_ids.ids:
            self.first_aid_trauma_is_choose_other = True
        else:
            self.first_aid_trauma_is_choose_other = False
            self.first_aid_trauma_other = ''
    
    # 根據呼吸道處置勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_airway_ids')
    def _onchange_first_aid_airway_ids(self):
        # 選擇鼻管
        if 5 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_nose = True
        else:
            self.first_aid_airway_is_choose_nose = False
            self.first_aid_airway_nose_flow = ''
        # 選擇面罩
        if 6 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_mask = True
        else:
            self.first_aid_airway_is_choose_mask = False
            self.first_aid_airway_mask_flow = ''
        # 選擇LMA
        if 9 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_lma = True
        else:
            self.first_aid_airway_is_choose_lma = False
            self.first_aid_airway_lma_size = ''
        # 選擇Igel
        if 10 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_igel = True
        else:
            self.first_aid_airway_is_choose_igel = False
            self.first_aid_airway_igel_size = ''
        # 選擇氣管內管
        if 11 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_et = True
        else:
            self.first_aid_airway_is_choose_et = False
            self.first_aid_airway_et_size = ''
        # 選擇其他
        if 12 in self.first_aid_airway_ids.ids:
            self.first_aid_airway_is_choose_other = True
        else:
            self.first_aid_airway_is_choose_other = False
            self.first_aid_airway_other = ''

    # 根據心肺復甦術勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_cpr_ids')
    def _onchange_first_aid_cpr_ids(self):
        # 選擇CPR
        if 2 in self.first_aid_cpr_ids.ids:
            self.first_aid_cpr_is_choose_cpr = True
        else:
            self.first_aid_cpr_is_choose_cpr = False
            self.first_aid_cpr_cpr_minutes = ''
        # 選擇使用AED
        if 3 in self.first_aid_cpr_ids.ids:
            self.first_aid_cpr_is_choose_aed = True
        else:
            self.first_aid_cpr_is_choose_aed = False
            self.first_aid_cpr_aed_ids = [(5, 0, 0)]
            self.first_aid_cpr_aed_is_choose_elect = False
            self.first_aid_cpr_aed_elect_times = ''
    
    # 根據使用AED勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_cpr_aed_ids')
    def _onchange_first_aid_cpr_aed_ids(self):
        # 選擇電擊去顫
        if 1 in self.first_aid_cpr_aed_ids.ids:
            self.first_aid_cpr_aed_is_choose_elect = True
        else:
            self.first_aid_cpr_aed_is_choose_elect = False
            self.first_aid_cpr_aed_elect_times = ''
    
    # 根據藥物處置勾選的項目，決定要顯示的列表
    @api.onchange('first_aid_drug_ids')
    def _onchange_first_aid_drug_ids(self):
        # 藥物處置選擇靜脈輸液
        if 1 in self.first_aid_drug_ids.ids:
            self.first_aid_drug_is_choose_iv = True
        else:
            self.first_aid_drug_is_choose_iv = False
            self.first_aid_drug_iv_body_part = ''
            self.first_aid_drug_iv_ids = [(5, 0, 0)]
            self.first_aid_drug_iv_is_choose_ns = False
            self.first_aid_drug_iv_ns_ml = ''
            self.first_aid_drug_iv_is_choose_lr = False
            self.first_aid_drug_iv_lr_ml = ''
            self.first_aid_drug_iv_is_choose_gs = False
            self.first_aid_drug_iv_gs_type = ''
            self.first_aid_drug_iv_gs_ml = ''
        # 藥物處置選擇NTG
        if 4 in self.first_aid_drug_ids.ids:
            self.first_aid_drug_is_choose_ntg = True
        else:
            self.first_aid_drug_is_choose_ntg = False
            self.first_aid_drug_ntg_pieces = ''
        # 藥物處置選擇支氣管擴張劑
        if 5 in self.first_aid_drug_ids.ids:
            self.first_aid_drug_is_choose_bronchodilator = True
        else:
            self.first_aid_drug_is_choose_bronchodilator = False
            self.first_aid_drug_bronchodilator_times = ''
    
    # 根據靜脈輸液的項目，決定要顯示的列表
    @api.onchange('first_aid_drug_iv_ids')
    def _onchange_first_aid_drug_iv_ids(self):
        # 選擇0.9%N/S
        if 1 in self.first_aid_drug_iv_ids.ids:
            self.first_aid_drug_iv_is_choose_ns = True
        else:
            self.first_aid_drug_iv_is_choose_ns = False
            self.first_aid_drug_iv_ns_ml = ''
        # 選擇LR
        if 2 in self.first_aid_drug_iv_ids.ids:
            self.first_aid_drug_iv_is_choose_lr = True
        else:
            self.first_aid_drug_iv_is_choose_lr = False
            self.first_aid_drug_iv_lr_ml = ''
        # 選擇葡萄糖液
        if 3 in self.first_aid_drug_iv_ids.ids:
            self.first_aid_drug_iv_is_choose_gs = True
        else:
            self.first_aid_drug_iv_is_choose_gs = False
            self.first_aid_drug_iv_gs_type = ''
            self.first_aid_drug_iv_gs_ml = ''

    # 其他處置選擇其他
    @api.onchange('first_aid_other_ids')
    def _onchange_first_aid_other_ids(self):
        if 6 in self.first_aid_other_ids.ids:
            self.first_aid_other_is_choose_other = True
        else:
            self.first_aid_other_is_choose_other = False
            self.first_aid_other_other = ''

    # 根據ASL處置勾選的項目，決定要顯示的列表
    @api.onchange('drug_asl_process_ids')
    def _onchange_drug_asl_process_ids(self):
        # 選擇氣管內管
        if 1 in self.drug_asl_process_ids.ids:
            self.drug_asl_process_is_choose_on_tube = True
        else:
            self.drug_asl_process_is_choose_on_tube = False
            self.drug_asl_process_on_tube_size = ''
            self.drug_asl_process_on_tube_fix_cm = ''
        # 選擇手動電擊
        if 2 in self.drug_asl_process_ids.ids:
            self.drug_asl_process_is_choose_elect = True
        else:
            self.drug_asl_process_is_choose_elect = False
            self.drug_asl_process_elect_times = ''
            self.drug_asl_process_elect_joule = ''
        
    # 自動帶入姓名到拒絕送醫姓名
    @api.depends('name')
    def _compute_reject_transport_name(self):
        for record in self:
            if record.name:
                record.reject_transport_name = record.name

    # 當關係人身分的選項為病患時，自動帶入姓名到關係人姓名
    @api.onchange('relation_identity_id')
    def _onchange_relation_identity(self):
        if self.relation_identity_id:
            if self.relation_identity_id.id == 1:
                self.relation_name = self.name
    
    # 計算總費用
    @api.depends('ambulance_fee', 'oxygen_fee')
    def _compute_total_fee(self):
        for record in self:
            if record.ambulance_fee or record.oxygen_fee:
                record.total_fee = int(record.ambulance_fee) + int(record.oxygen_fee)
            else:
                record.total_fee = 0

    # 點選收費情形的選項時，預設清空所有相關的欄位
    @api.onchange('receive_fee_situations_id')
    def _onchange_receive_fee_situations_id(self):
        if self.receive_fee_situations_id:
            if self.receive_fee_situations_id.id == 1:
                self.receive_fee_yes_pay_method_id = ''
                self.receive_fee_no_pay_method_id = ''
                self.receive_fee_no_pay_method_request_target = ''
            elif self.receive_fee_situations_id.id == 2:
                self.receive_fee_yes_pay_method_id = ''
                self.receive_fee_no_pay_method_id = ''
                self.receive_fee_no_pay_method_request_target = ''
            elif self.receive_fee_situations_id.id == 3:
                self.receive_fee_yes_pay_method_id = ''
                self.receive_fee_no_pay_method_id = ''
                self.receive_fee_no_pay_method_request_target = ''

    # 點選未收費的付款方式的選項時，預設清空統一請款對象欄位
    @api.onchange('receive_fee_no_pay_method_id')
    def _onchange_receive_fee_no_pay_method_id(self):
        if self.receive_fee_no_pay_method_id:
            if self.receive_fee_no_pay_method_id.id == 1:
                self.receive_fee_no_pay_method_request_target = ''
            elif self.receive_fee_no_pay_method_id.id == 2:
                self.receive_fee_no_pay_method_request_target = ''
            elif self.receive_fee_no_pay_method_id.id == 3:
                self.receive_fee_no_pay_method_request_target = ''

    # 按下按鈕更新接收時間
    def btn_refresh_receive_unit_datetime(self):
        self.receive_unit_datetime = fields.Datetime.now()

    # 從接收時間取出時與分
    @api.depends('receive_unit_datetime')
    def _compute_receive_unit_datetime_str(self):
        for record in self:
            record.receive_unit_datetime_str = (record.receive_unit_datetime + datetime.timedelta(hours=8)).strftime('%H時%M分')
