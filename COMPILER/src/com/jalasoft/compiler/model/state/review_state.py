from src.com.jalasoft.compiler.model.state.doc_state_interface import IDocState


class ReviewState(IDocState):
    def display_state(self) -> str:
        print("Review state")
