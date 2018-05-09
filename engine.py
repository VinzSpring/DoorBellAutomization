from tokens import TokenManager


class Engine:

    def __init__(self, door_bell_controller):
        self.door_bell_controller = door_bell_controller
        self.on_ringed_notification = None
        self.on_opened_door_notification = None
        self.open_always = False
        self.token_manager = TokenManager()
        pass

    def start(self):
        self.door_bell_controller.watch_door_bell_ring(self.on_ring())
        pass

    def activate_token(self, token):
        if self.token_manager.token_is_valid(token):
            self.token_manager.delete_token(token)
            self.reset_timer_for_token()

    def reset_timer_for_token(self):
        self.open_always = True
        # start timer and after that
        self.open_always = False
        pass

    def on_ring(self):
        if self.on_ringed_notification:
            self.on_ringed_notification()

        if self.open_always:
            self.open_door()
            if self.on_opened_door_notification:
                self.on_opened_door_notification()
        pass

    def open_door(self):
        self.door_bell_controller.open_door()
        if light_is_needed():
            self.door_bell_controller.turn_lights_on()
        pass

    def set_on_ringed_notification(self, callback):
        self.on_ringed_notification = callback
        pass

    def set_on_opened_door_notification(self, callback):
        self.on_opened_door_notification = callback
        pass


def light_is_needed():
    return False
