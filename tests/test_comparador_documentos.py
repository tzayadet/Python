import tempfile
import unittest
from pathlib import Path

from comparador_documentos import DocumentComparator, DocumentReader


class DocumentComparatorTests(unittest.TestCase):
    def setUp(self):
        self.comparator = DocumentComparator()

    def test_normalize_text_preserves_nonempty_lines(self):
        result = self.comparator.normalize_text("  Alpha   beta\r\n\r\n Gamma  ")
        self.assertEqual(result, ["Alpha beta", "Gamma"])

    def test_diff_escapes_untrusted_document_content(self):
        diff, stats = self.comparator.generate_html_diff(
            ["<script>alert(1)</script>"],
            ["<img src=x onerror=alert(1)>"],
        )
        self.assertNotIn("<script>", diff)
        self.assertNotIn("<img", diff)
        self.assertIn("&lt;script&gt;", diff)
        self.assertIn("&lt;img", diff)
        self.assertEqual(stats["added_lines"], 1)
        self.assertEqual(stats["removed_lines"], 1)

    def test_read_txt_uses_document_reader(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "sample.txt"
            source.write_text("Primera línea\nSegunda línea", encoding="utf-8")
            self.assertEqual(
                DocumentReader.read_document(str(source)),
                "Primera línea\nSegunda línea",
            )

    def test_report_escapes_file_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_a = Path(tmp) / "original.txt"
            source_b = Path(tmp) / "<script>.txt"
            output = Path(tmp) / "report.html"
            source_a.write_text("versión uno", encoding="utf-8")
            source_b.write_text("versión dos", encoding="utf-8")

            self.comparator.compare_documents(
                str(source_a), str(source_b), str(output)
            )
            report = output.read_text(encoding="utf-8")
            self.assertIn("&lt;script&gt;.txt", report)
            self.assertNotIn("<p><strong>Documento 2:</strong> <script>", report)

    def test_output_cannot_overwrite_an_input_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_a = Path(tmp) / "original.txt"
            source_b = Path(tmp) / "other.txt"
            source_a.write_text("original", encoding="utf-8")
            source_b.write_text("other", encoding="utf-8")

            with self.assertRaises(ValueError):
                self.comparator.compare_documents(
                    str(source_a), str(source_b), str(source_a)
                )

            self.assertEqual(source_a.read_text(encoding="utf-8"), "original")

    def test_existing_report_requires_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_a = Path(tmp) / "a.txt"
            source_b = Path(tmp) / "b.txt"
            output = Path(tmp) / "report.html"
            source_a.write_text("alpha", encoding="utf-8")
            source_b.write_text("beta", encoding="utf-8")
            output.write_text("keep me", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                self.comparator.compare_documents(
                    str(source_a), str(source_b), str(output)
                )
            self.assertEqual(output.read_text(encoding="utf-8"), "keep me")

    def test_force_allows_overwriting_an_existing_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_a = Path(tmp) / "a.txt"
            source_b = Path(tmp) / "b.txt"
            output = Path(tmp) / "report.html"
            source_a.write_text("alpha", encoding="utf-8")
            source_b.write_text("beta", encoding="utf-8")
            output.write_text("old report", encoding="utf-8")

            self.comparator.compare_documents(
                str(source_a), str(source_b), str(output), overwrite=True
            )
            self.assertIn("Comparación de Documentos", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
