from ithopy.message import Message
from ithopy.payload import Payload
from ithopy.base_message_builder import BaseMessageBuilder
from .hru_device import HruDevice

class HruMessageBuilder(BaseMessageBuilder):
  def write_setting(self, setting_id, payload_value = None, payload_type = None):
    payload = Payload()
    payload.payload_type  = payload_type
    payload.payload_value = payload_value
    payload.setting_id    = setting_id

    msg           = Message()
    msg.src       = self.src_addr
    msg.dest      = self.dest_addr
    msg.msg_class = HruDevice.SETTINGS_MSG
    msg.type      = BaseMessageBuilder.MSG_WRITE
    msg.payload   = payload

    return msg

  def read_setting(self, setting_id):
    payload = Payload()
    payload.setting_id = setting_id

    msg           = Message()
    msg.src       = self.src_addr
    msg.dest      = self.dest_addr
    msg.msg_class = HruDevice.SETTINGS_MSG
    msg.type      = BaseMessageBuilder.MSG_READ
    msg.payload   = payload

    return msg

  def set_supply_fan_rpm(self, value):
    if value > 3600 or value < 0:
      raise Exception('Value out of range')

    return self.write_setting(
      HruDevice.SET_SUPPLY_FAN_RPM, value, Payload.DATA_TYPES['2_bytes']
    )

  def set_exhaust_fan_rpm(self, value):
    if value > 3600 or value < 0:
      raise Exception('Value out of range')

    return self.write_setting(
      HruDevice.SET_EXHAUST_FAN_RPM, value, Payload.DATA_TYPES['2_bytes']
    )

  # value = 0-1
  def set_manual_mode(self, value):
    return self.write_setting(
      HruDevice.SET_MANUAL_MODE, (1 if value == True else 0), Payload.DATA_TYPES['1_byte']
    )

  # 0=closed, 800=bypass, -800=frost
  def set_valve_position(self, value):
    if value > 800 or value < -800:
      raise Exception('Value out of range')

    return self.write_setting(
      HruDevice.SET_VALVE_POSITION, value, Payload.DATA_TYPES['2_bytes']
    )
