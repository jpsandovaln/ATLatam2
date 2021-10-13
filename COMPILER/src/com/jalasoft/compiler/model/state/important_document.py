from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState
from src.com.jalasoft.compiler.model.state.init_state import InitState


class ImportantDocument:
    def __init__(self, title, filePath):
        self._title = title
        self._filePath = filePath
        self._currentState: IDocState = InitState()

    def set_state(self, state: IDocState):
        self._currentState = state

    def display_state(self):
        self._currentState.display_state()
