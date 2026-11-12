<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&size=25&duration=2400&pause=900&center=true&vCenter=true&width=760&color=00F5FF&lines=PYTHON+DEVELOPMENT;AUTOMATION+%26+TOOLS;BUILDING+BY+PRACTICE" alt="Python development header"/>
</p>

<p align="center">
  <a href="https://github.com/tzayadet"><img src="https://img.shields.io/badge/GitHub-tzayadet-181717?style=for-the-badge&logo=github" alt="GitHub"/></a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Focus-Development%20%26%20Automation-00A6A6?style=for-the-badge" alt="Development and automation"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-7928CA?style=for-the-badge" alt="MIT License"/></a>
</p>

# Python Projects

[![Python CI](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml/badge.svg)](https://github.com/tzayadet/Python/actions/workflows/python-checks.yml)

Repositorio personal de aprendizaje y desarrollo en Python. Reúne ejercicios, scripts, automatizaciones, utilidades y aplicaciones creadas durante distintas etapas de formación y práctica.

## Áreas de trabajo

| Área | Contenido |
|---|---|
| **Fundamentos** | Sintaxis, estructuras de datos, funciones, módulos y resolución de problemas. |
| **Programación orientada a objetos** | Clases, composición, herencia y organización del código. |
| **Automatización** | Scripts para procesamiento de archivos, tareas repetitivas e integración con herramientas. |
| **Aplicaciones** | Utilidades de escritorio, interfaces gráficas y pequeñas aplicaciones web. |
| **Datos** | Procesamiento, consultas, ficheros y generación de informes. |
| **Experimentación** | Prototipos y pruebas de concepto independientes. |

## Aplicaciones y utilidades destacadas

| Proyecto | Descripción | Estado |
|---|---|---|
| [Comparador de documentos](comparador_documentos.py) | Compara TXT, DOCX, RTF y PDF; genera un informe HTML con diferencias y métricas. | CLI con pruebas unitarias |
| [Conversor Python a EXE](python_to_exe_gui.py) | Interfaz Tkinter para empaquetar scripts con PyInstaller; ejecuta el proceso en segundo plano, mantiene la interfaz en el hilo principal y evita sobrescribir ejecutables con nombres repetidos. | Utilidad de escritorio |
| [Automatización de KPI de RR. HH.](HR_ETL_KPI_scripting.py) | Procesamiento de datos Excel y generación de indicadores e informes. | Script dependiente de libro de entrada |

### Comparador de documentos

Instala las dependencias:

```bash
python -m pip install -r requirements-comparador-documentos.txt
```

Para comparar dos documentos:

```bash
python comparador_documentos.py contrato_v1.docx contrato_v2.docx
```

Para elegir la ruta del informe:

```bash
python comparador_documentos.py documento_a.pdf documento_b.pdf --output diferencias.html
```

Los formatos PDF, DOCX y RTF requieren sus dependencias Python. Para documentos DOC antiguos también hace falta Pandoc instalado en el sistema. El comparador no sobrescribe documentos de entrada y exige `--force` para sustituir un informe HTML existente.

## Entorno de desarrollo

Se recomienda Python 3 y un entorno virtual por proyecto:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Instala únicamente las dependencias indicadas por cada proyecto y ejecuta el script correspondiente:

```bash
python nombre_del_script.py
```

## Organización y madurez

Este repositorio funciona como espacio de trabajo y archivo de prácticas. Los proyectos pueden tener dependencias, requisitos y niveles de madurez distintos. Los materiales históricos no ejecutables se conservan en `archive/` y quedan fuera de la validación de código. No todos los scripts son aplicaciones listas para producción; revisa el README específico y el código antes de utilizarlos.

## Tecnologías

- Python 3
- Tkinter y CustomTkinter
- Scripting y automatización
- Procesamiento de archivos y datos
- APIs y servicios web
- Testing y control de versiones

## Licencia

MIT. Consulta [LICENSE](LICENSE).

## Project showcase

[Open the GitHub Pages showcase](https://tzayadet.github.io/Python/) · [Showcase source](docs/index.html)

The page is a curated index of selected source files; it does not execute Python or Java in the browser. To publish it, select **Settings → Pages → Build and deployment → Source → GitHub Actions** and set the repository Actions variable `ENABLE_PAGES=true` under **Settings → Secrets and variables → Actions → Variables**. The workflow remains skipped until that variable is enabled.
