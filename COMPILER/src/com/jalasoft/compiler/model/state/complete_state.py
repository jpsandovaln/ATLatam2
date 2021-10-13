from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState


class CompleteState(IDocState):
    def display_state(self) -> str:
        print("Complete state")
