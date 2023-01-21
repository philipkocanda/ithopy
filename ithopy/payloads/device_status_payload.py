from ithopy.payloads import BasePayload


class DeviceStatusPayload(BasePayload):
    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.byteArr = [0x0] * 19
        self.data_type = 0  # not sure what this is, but it needs to be zero

        pass

    def parse(self, byteArr, payload_type):
        if len(byteArr) < 16:
            self.data_type = -1
            self.setting_id = -1
            self.payload_value = -1
            self.payload_type = -1
            return -1

        self.data_type = byteArr[16]
        # can be used to look up the correct payload_type, right?
        self.setting_id = byteArr[17]
        self.payload_type = payload_type

        _num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        _resolution = self.payload_type['resolution']

        value = (
            byteArr[0] << 24) | (
            byteArr[1] << 16) | (
            byteArr[2] << 8) | byteArr[3]

        self.payload_value = value

        return self.payload_value

    def build(self):
        num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        resolution = self.payload_type['resolution']

        self.byteArr[16] = self.data_type
        self.byteArr[17] = self.setting_id  # "index" column in the CSV

        value = self.payload_value * resolution

        if (num_bytes > 0):
            self.byteArr[3] = value & 0xFF

        if (num_bytes > 1):
            self.byteArr[2] = (value >> 8) & 0xFF

        if (num_bytes > 2):
            self.byteArr[1] = (value >> 16) & 0xFF
            self.byteArr[0] = (value >> 24) & 0xFF

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
    def inspect(self):
        return {
            # TODO
        }

    # bytestring representation of the payload
    def __str__(self):
        return " ".join(self.build().byteArr)
