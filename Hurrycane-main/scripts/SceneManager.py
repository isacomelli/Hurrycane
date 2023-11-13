class SceneManager:
    def __init__(self, current_state):
        self.current_state = current_state
        self.previous_state = None

    def set_state(self, state):
        self.previous_state = self.current_state
        self.current_state = state

    def get_state(self):
        return self.current_state

    def get_previous_state(self):
        return self.previous_state