# from hardware_watcher import ImportWatcher


class DoorBellControls:

    def __init__(self):
        # self.hooked_pins = ImportWatcher()
        self.hooked_pins = None
        self.on_ring_callback = None

    def open_door(self):
        print("Opening the door...")
        pass

    def toggle_bell_tone(self, enabled):
        print("Setting bell tone to " + enabled)
        pass

    def send_audio(self, audio):
        pass

    def get_audio_out_stream(self):
        pass

    def get_audio_in_stream(self):
        pass

    def watch_door_bell_ring(self, callback):
        self.on_ring_callback = callback
        # watch the pin
        # callback()
        pass

    def on_ring(self):
        if self.on_ring_callback:
            self.on_ring_callback()

    def turn_lights_on(self):
        print("Turning the lights on")
        pass


