class BaseMessageBuilder:
  # Message Types
  MSG_REPLY = 1
  MSG_READ = 4
  MSG_WRITE = 6

  def __init__(self, src_addr, dest_addr) -> None:
    self.src_addr = src_addr
    self.dest_addr = dest_addr
    pass

  def read_setting(self, setting_id):
    pass

  def write_setting(self, setting_id, payload_value = None, payload_type = None):
    pass

  # "82 80 90 E0 04 00 8A"
  def device_type(self):
    pass

  # "82 80 90 E1 04 00 89"
  def device_serial(self):
    pass

  # "82 80 A4 01 04 00 55"
  def device_status(self):
    pass

