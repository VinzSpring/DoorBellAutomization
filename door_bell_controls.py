from hardware_watcher import ImportWatcher


class DoorBellController:

    def __init__(self):
        self.hooked_pins = ImportWatcher()

    def open_door(self):
        pass

    def toggle_bell_tone(self, enabled):
        pass

    def send_audio(self, audio):
        pass

    def get_audio_out_stream(self):
        pass

    def get_audio_in_stream(self):
        pass

    def watch_door_bell_ring(self, callback):
        # watch the pin
        # callback()
        pass

    def turn_lights_on(self):
        pass


