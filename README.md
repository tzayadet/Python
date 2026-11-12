# Python Projects

A personal workspace for Python practice and development. It brings together scripts, automation, desktop utilities and small applications built across different stages of learning and experimentation.

<p align="center">
  <a href="https://github.com/tzayadet/Python"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source"></a>
</p>

[![Python CI](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml/badge.svg)](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml)

## Areas of work

| Area | Contents |
|---|---|
| Fundamentals | Syntax, data structures, functions, modules and problem solving |
| Object-oriented programming | Classes, composition, inheritance and code organisation |
| Automation | File processing, repetitive tasks and tool integration |
| Applications | Desktop utilities, graphical interfaces and small web applications |
| Data | Processing, queries, files and report generation |
| Experiments | Independent prototypes and proof-of-concept work |

## Selected utilities

| Project | Description | Status |
|---|---|---|
| [Document comparator](comparador_documentos.py) | Compares TXT, DOCX, RTF and PDF documents and generates an HTML differences report. | CLI with unit tests |
| [Python to EXE](python_to_exe_gui.py) | Tkinter interface for packaging scripts with PyInstaller. | Desktop utility |
| [HR KPI automation](HR_ETL_KPI_scripting.py) | Processes Excel data and generates HR indicators and reports. | Requires an input workbook |

## Document comparator

Install the dependencies:

```bash
python -m pip install -r requirements-comparador-documentos.txt
```

Compare two documents:

```bash
python comparador_documentos.py contract_v1.docx contract_v2.docx
python comparador_documentos.py document_a.pdf document_b.pdf --output differences.html
```

PDF, DOCX and RTF support requires the relevant Python packages. Legacy DOC files also require Pandoc. Existing reports are not overwritten unless `--force` is supplied.

## Development environment

Use a virtual environment for each project:

```bash
python -m venv .venv
```

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install only the dependencies declared for the project you intend to run. Not every script in this repository shares the same requirements.

## Project maturity

This repository is a working collection rather than a single installable Python package. Projects have different dependencies and maturity levels; historical material and standalone scripts are retained for reference. Review the relevant source and requirements before execution.

## Validation

The repository includes GitHub Actions checks for selected Python components. A passing workflow does not imply that every historical script has been tested.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
