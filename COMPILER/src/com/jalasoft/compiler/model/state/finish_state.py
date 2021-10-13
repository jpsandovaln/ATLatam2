from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState


class FinishState(IDocState):
    def display_state(self) -> str:
        print("Finish state")
