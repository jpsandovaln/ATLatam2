from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState


class InitState(IDocState):
    def display_state(self) -> str:
        print("Init state")
