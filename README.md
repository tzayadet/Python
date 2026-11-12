<p align="center">
  <img src="https://img.shields.io/badge/DEVELOPMENT-PYTHON_WORKSPACE-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Python workspace"/>
  <img src="https://img.shields.io/badge/AUTOMATION-DESKTOP-101010?style=for-the-badge&logo=python&logoColor=00FF41" alt="Python"/>
</p>

# Python Projects

A working collection of Python exercises, scripts, automation workflows and desktop utilities. Projects are kept independent because they do not share one dependency set or release cycle.

<p align="center">
  <a href="https://tzayadet.github.io/Python/"><strong>PROJECT SHOWCASE ↗</strong></a> ·
  <a href="https://github.com/tzayadet/Python"><strong>SOURCE CODE</strong></a>
</p>

[![Python CI](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml/badge.svg)](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml)

## Selected projects

| Project | Description | Execution |
|---|---|---|
| [Document comparator](comparador_documentos.py) | Compares TXT, DOCX, RTF and PDF documents and generates an HTML differences report. | CLI · unit tests |
| [Python to EXE](python_to_exe_gui.py) | Tkinter interface for packaging scripts with PyInstaller. | Desktop |
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

## Development setup

Create a virtual environment for the component you intend to run:

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

Install only that component's dependencies. Scripts in this repository are not one installable package and may require different libraries.

## Project layout and maturity

This repository is a working collection, not a single application. It contains independent utilities, learning exercises and historical experiments at different stages of completion. Review each script and its requirements before execution.

## Validation

GitHub Actions checks selected Python components. A passing workflow does not imply that every historical script has been tested.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
