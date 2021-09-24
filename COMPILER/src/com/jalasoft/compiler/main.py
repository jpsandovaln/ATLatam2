from src.com.jalasoft.compiler.model.compiler_facade import CompilerFacade


if __name__ == '__main__':
    print('hello')
    CompilerFacade.compile('java', 'D:/code/EjemploJava8.java', 'D:/code/ ', 'C:/"Program Files"/Java/jdk1.8.0_251/bin/')
    CompilerFacade.compile('python', 'D:/Hello.py', '', 'C:/python39/')
