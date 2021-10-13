from src.com.jalasoft.compiler.model.compiler_facade import CompilerFacade
from src.com.jalasoft.compiler.model.state.complete_state import CompleteState
from src.com.jalasoft.compiler.model.state.document import Document
from src.com.jalasoft.compiler.model.state.finish_state import FinishState
from src.com.jalasoft.compiler.model.state.important_document import ImportantDocument
from src.com.jalasoft.compiler.model.state.progress_state import ProgressState
from src.com.jalasoft.compiler.model.state.review_state import ReviewState

if __name__ == '__main__':
    print('hello')
    # CompilerFacade.compile('java', 'D:/code/EjemploJava8.java', 'D:/code/ ', 'C:/"Program Files"/Java/jdk1.8.0_251/bin/')
    # CompilerFacade.compile('python', 'D:/Hello.py', '', 'C:/python39/')

    """document = Document("doc1", "d:/files/doce1.pdf")
    document.display_state()

    document.set_state("review")
    document.display_state()

    document.set_state("progress")
    document.display_state() """

    doc = ImportantDocument("doc1", "d:/files/doce1.pdf")
    doc.display_state()

    doc.set_state(ReviewState())
    doc.display_state()

    doc.set_state(ProgressState())
    doc.display_state()

    doc.set_state(CompleteState())
    doc.display_state()

    doc.set_state(FinishState())
    doc.display_state()
