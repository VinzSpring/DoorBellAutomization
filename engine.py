import datetime
from threading import Thread, Timer

from door_bell_controls import DoorBellControls
from tokens import TokenManager
from time import sleep, time

DEFAULT_TIME_FOR_RING_AND_OPEN = 30  # seconds
DEFAULT_EXPIRE_TIME_TOKENS = 20  # minutes


class Engine:

    def __init__(self, door_bell_controls):
        self.door_bell_controls = door_bell_controls
        self.on_bell_rung_notification = None
        self.on_opened_door_notification = None
        self.open_always = False
        self.token_manager = TokenManager()
        self.timer = None
        pass

    def start(self):
        self.door_bell_controls.watch_door_bell_ring(self.on_ring)
        pass

    def insert_token(self, token=None):
        expire_time = DEFAULT_EXPIRE_TIME_TOKENS*1000
        if token:
            self.token_manager.insert_token(token, expire_time)
            return token
        else:
            return self.token_manager.insert_random_token(expire_time)

    def activate_token(self, token):
        if self.token_manager.token_is_valid(token):
            self.token_manager.delete_token(token)
            self.open_always = True
            self.reset_timer_for_token()
        else:
            print("Access denied: Token was not valid or expired")

    def disable_always_open(self):
        self.open_always = False

    def reset_timer_for_token(self):
        # cancel timer if exist
        if self.timer:
            self.timer.cancel()

        # start timer and after that
        self.timer = Timer(DEFAULT_TIME_FOR_RING_AND_OPEN, self.disable_always_open)
        self.timer.start()
        pass

    def on_ring(self):
        if self.on_bell_rung_notification:
            self.on_bell_rung_notification()

        if self.open_always:
            self.open_door()
            if self.on_opened_door_notification:
                self.on_opened_door_notification()
        pass

    def open_door(self):
        self.door_bell_controls.open_door()
        if self.light_is_needed():
            self.door_bell_controls.turn_lights_on()
        pass

    def set_on_bell_rung_notification(self, callback):
        self.on_bell_rung_notification = callback
        pass

    def set_on_opened_door_notification(self, callback):
        self.on_opened_door_notification = callback
        pass

    @staticmethod
    def light_is_needed():
        return False





# EXAMPLE PROGRAM
def simulate_guest(pw):
    engine.activate_token(pw)
    activate_to_ring_delay = Timer(5, lambda: dbc.on_ring())
    activate_to_ring_delay.start()


if __name__ == '__main__':
    dbc = DoorBellControls()
    engine = Engine(dbc)
    engine.set_on_opened_door_notification(lambda: print("NOTIFICATION: Opened the door"))
    engine.set_on_bell_rung_notification(lambda: print("NOTIFICATION: It rings"))
    engine.start()

    pw = "pass"
    engine.insert_token(pw)
    activate_after_token_delay = Timer(5, simulate_guest, args=[pw])
    activate_after_token_delay.start()
    pass






