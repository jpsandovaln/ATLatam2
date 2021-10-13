from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState


class ProgressState(IDocState):
    def display_state(self) -> str:
        print("Progress state")
