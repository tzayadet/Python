# Recordatorio: compilar un script Python con PyInstaller

Ejemplo de uso en Windows PowerShell:

```powershell
Set-Location "$HOME\Downloads"
pyinstaller --onefile .\x.py
```

Sustituye `x.py` por el nombre real del script. Ejecuta PyInstaller desde el entorno virtual del proyecto para mantener controladas las dependencias.
