import ast
import unittest
from pathlib import Path


class PythonToExeGuiStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = Path(__file__).resolve().parents[1] / "python_to_exe_gui.py"
        cls.tree = ast.parse(source.read_text(encoding="utf-8"))
        cls.app_class = next(
            node for node in cls.tree.body
            if isinstance(node, ast.ClassDef) and node.name == "PythonToExeConverter"
        )

    def test_event_handlers_are_defined_once(self):
        methods = [
            node.name for node in self.app_class.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        for name in (
            "browse_output_folder",
            "log_message",
            "start_conversion",
            "convert_files",
        ):
            with self.subTest(method=name):
                self.assertEqual(methods.count(name), 1)

    def test_conversion_worker_does_not_read_tk_widgets(self):
        worker = next(
            node for node in self.app_class.body
            if isinstance(node, ast.FunctionDef) and node.name == "convert_files"
        )
        forbidden = {
            "onefile_var", "noconsole_var", "selected_files", "output_dir",
            "progress", "convert_button", "log_text", "root",
        }
        references = {
            node.attr for node in ast.walk(worker)
            if isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "self"
        }
        self.assertFalse(forbidden.intersection(references))

    def test_pyinstaller_uses_unique_output_name_and_noninteractive_mode(self):
        source = Path(__file__).resolve().parents[1] / "python_to_exe_gui.py"
        text = source.read_text(encoding="utf-8")
        self.assertIn('"--name", output_name', text)
        self.assertIn('"--noconfirm"', text)
        self.assertIn('output_name = f"{source.stem}_{suffix}"', text)


if __name__ == "__main__":
    unittest.main()
