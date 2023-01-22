from ithopy.payloads import BasePayload


class DeviceStatusPayload(BasePayload):
    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.data = [0x0] * 19
        self.data_type = 0  # not sure what this is, but it needs to be zero

        pass

    def parse(self, data, payload_type):
        if len(data) < 16:
            self.data_type = -1
            self.setting_id = -1
            self.payload_value = -1
            self.payload_type = -1
            return -1

        self.data_type = data[16]
        # can be used to look up the correct payload_type, right?
        self.setting_id = data[17]
        self.payload_type = payload_type

        _num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        _resolution = self.payload_type['resolution']

        value = (
            data[0] << 24) | (
            data[1] << 16) | (
            data[2] << 8) | data[3]

        self.payload_value = value

        return self.payload_value

    def build(self):
        num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        resolution = self.payload_type['resolution']

        self.data[16] = self.data_type
        self.data[17] = self.setting_id  # "index" column in the CSV

        value = self.payload_value * resolution

        if (num_bytes > 0):
            self.data[3] = value & 0xFF

        if (num_bytes > 1):
            self.data[2] = (value >> 8) & 0xFF

        if (num_bytes > 2):
            self.data[1] = (value >> 16) & 0xFF
            self.data[0] = (value >> 24) & 0xFF

        return self

    # 0	ReqFanspeed	Requested fanspeed	%
    # 1	Balance	Balance	%
    # 2	toefanspeed	supply fan	rpm
    # 3	toefanactspeed	supply fan actual	rpm
    # 4	affanspeed	exhaust fan	rpm
    # 5	affanactspeed	exhaust fan actual	rpm
    # 6	toetemp	supply temp	°C
    # 7	aftemp	exhaust temp	°C
    # 8	status	Status
    # 9	Tin	Room temp	°C
    # 10	Tout	Outdoor temp	°C
    # 11	vorstklep	Valve position	pulse
    # 12	bypklep	Bypass position	pulse
    # 13	SumCnt	Summercounter
    # 14	SumDay	Summerday
    # 15	FrostTim	Frost timer	sec
    # 16	BoilTim	Boiler timer	min
    # 17	StartCnt	Frost block
    # 18	CurPos	Current position
    # 19	VKKswitch	VKKswitch
    # 20	GHEswitch	GHEswitch
    # 21	AirCounter	Airfilter counter
    def __dict__(self):
        return {
            # TODO
        }
