from hardware_watcher import ImportWatcher


class DoorBellController:

    def __init__(self):
        self.hooked_pins = ImportWatcher()

    def open_door(self):
        pass

    def toggle_bell(self, enabled):
        pass
