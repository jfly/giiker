import gatt

def initialize(on_state_change):
    manager = gatt.DeviceManager(adapter_name='hci0')
    device = GiikerDevice(mac_address='C2:DD:1F:F8:CB:DA', manager=manager, on_state_change=on_state_change)
    print("Connecting... ", end="")
    device.connect()
    print("connected!")

    manager.run()

class GiikerDevice(gatt.Device):
    def __init__(self, *args, on_state_change=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._on_state_change = on_state_change

    def services_resolved(self):
        super().services_resolved()

        cube_service_uuid = "0000aadb-0000-1000-8000-00805f9b34fb"
        cube_characteristic_uuid = "0000aadc-0000-1000-8000-00805f9b34fb"
        (cube_characteristic,) = [ characteristic for service in self.services for characteristic in service.characteristics if service.uuid == cube_service_uuid and characteristic.uuid == cube_characteristic_uuid ]
        cube_characteristic.enable_notifications()

    def characteristic_value_updated(self, characteristic, value):
        giiker_state = GiikerState(value)
        if self._on_state_change is not None:
            self._on_state_change(giiker_state)

class GiikerState():
    def __init__(self, value: bytes):
        assert len(value) == 20
        self.value = value

        self.cube_state = value[:16]
        self.recent_moves = list(map(GiikerMove, value[16:]))

class GiikerMove():
    def __init__(self, value):
        face = value // 16
        amount = value % 16

        if amount == 9:
            print("Encountered the mystical 9")
            amount = 2

        self.face = ["?", "B", "D", "L", "U", "R", "F"][face]
        self.amount = [0, 1, 2, -1][amount]

    def __str__(self):
        return self.face + { 0: "0", 1: "", 2: "2", -1: "'" }[self.amount]