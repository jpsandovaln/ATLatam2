INIT_STATE = "init"
REVIEW_STATE = "review"
PROGRESS_STATE = "progress"
COMPLETE_STATE = "complete"
FINISH_STATE = "finish"


class Document:
    def __init__(self, title, filePath):
        self._title = title
        self._filePath = filePath
        self._currentState = INIT_STATE

    def set_state(self, state: str):
        self._currentState = state

    def display_state(self):
        if INIT_STATE == self._currentState:
            print("init state")
        if REVIEW_STATE == self._currentState:
            print("review state")
        if COMPLETE_STATE == self._currentState:
            print("complete state")
        if PROGRESS_STATE == self._currentState:
            print("progress state")
