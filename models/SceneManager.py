class SceneManager:
    def __init__(self, currentState):
        self.currenteState = currentState
    def get_state(self):
        return self.currenteState
    def set_state(self, state):
        self.currenteState = state
