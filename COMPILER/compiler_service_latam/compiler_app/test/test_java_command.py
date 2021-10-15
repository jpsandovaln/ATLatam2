from unittest import TestCase
from ..model.parameter import Parameter
from ..model.java_command import JavaCommand
from ..exception.command_exception import CommandException
from ..exception.parameter_exception import ParameterException


class TestJavaCommand(TestCase):
    """def test_build(self):
        param = Parameter("d:/code/test.java", "d:/code/ ", "d:/binary/bin/")
        command = JavaCommand()
        current = command.build(param)
        expected = "d:/binary/bin/javac d:/code/test.java && d:/binary/bin/java -cp d:/code/ EjemploJava8"
        self.assertEqual(current, expected)"""

    def test_build_none_parameter(self):
        with self.assertRaises(CommandException):
            command = JavaCommand()
            command.build(None)

    def test_build_invalid_parameter(self):
        with self.assertRaises(ParameterException):
            param = Parameter("", "", "")
            command = JavaCommand()
            current = command.build(param)

    def test_build_empty_parameter(self):
        with self.assertRaises(CommandException):
            command = JavaCommand()
            command.build("")
