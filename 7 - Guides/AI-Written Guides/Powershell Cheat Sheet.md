# PowerShell File Navigation Cheat Sheet

## Where am I?

```powershell
pwd
```

or:

```powershell
Get-Location
```

---

## List files

```powershell
ls
```

Full command:

```powershell
Get-ChildItem
```

Common variants:

```powershell
ls -Force
```

Show hidden files.

```powershell
ls -Recurse
```

Show files recursively.

```powershell
ls *.py
```

Show only Python files.

```powershell
ls -Directory
```

Show only folders.

```powershell
ls -File
```

Show only files.

---

## Move around

```powershell
cd path\to\folder
```

```powershell
cd ..
```

```powershell
cd ~
```

```powershell
cd C:\Users\SeanS\Documents
```

Previous location:

```powershell
cd -
```

---

## Create folders and files

```powershell
mkdir python_lab
```

```powershell
New-Item notes.txt
```

```powershell
New-Item approx_integs.py
```

Create nested folders:

```powershell
mkdir python_lab\math\calc
```

---

## Open files/folders

Open current folder in Explorer:

```powershell
explorer .
```

Open VS Code:

```powershell
code .
```

Open a file with default app:

```powershell
ii notes.txt
```

`ii` means `Invoke-Item`.

---

## Copy, move, rename, delete

```powershell
Copy-Item old.txt new.txt
```

```powershell
Move-Item old.txt folder\
```

```powershell
Rename-Item old.txt new.txt
```

```powershell
Remove-Item old.txt
```

Delete folder recursively:

```powershell
Remove-Item foldername -Recurse
```

Safer version:

```powershell
Remove-Item foldername -Recurse -WhatIf
```

`-WhatIf` previews what would happen.

---

## Inspect files

Print file:

```powershell
Get-Content notes.txt
```

Short alias:

```powershell
cat notes.txt
```

First 20 lines:

```powershell
Get-Content notes.txt -TotalCount 20
```

Last 20 lines:

```powershell
Get-Content notes.txt -Tail 20
```

Watch a log/file live:

```powershell
Get-Content output.log -Wait
```

Search inside files:

```powershell
Select-String "Simpson" *.py
```

Recursive search:

```powershell
Get-ChildItem -Recurse *.py | Select-String "midpoint"
```

---

# Useful Chained Commands

## Find all Python files

```powershell
ls -Recurse -Filter *.py
```

---

## Find large files

```powershell
ls -Recurse -File | Sort-Object Length -Descending | Select-Object -First 20 Name, Length, FullName
```

---

## Find recently modified files

```powershell
ls -Recurse -File | Sort-Object LastWriteTime -Descending | Select-Object -First 20 LastWriteTime, FullName
```

---

## Search all Python files for a function name

```powershell
ls -Recurse -Filter *.py | Select-String "def simpsons_rule"
```

---

## Show folder sizes

```powershell
ls -Directory | ForEach-Object {
    $size = (ls $_.FullName -Recurse -File | Measure-Object Length -Sum).Sum
    [PSCustomObject]@{
        Folder = $_.Name
        MB = [math]::Round($size / 1MB, 2)
    }
}
```

---

## Count files by extension

```powershell
ls -Recurse -File |
    Group-Object Extension |
    Sort-Object Count -Descending |
    Select-Object Count, Name
```

---

## Find empty folders

```powershell
ls -Recurse -Directory |
    Where-Object { -not (ls $_.FullName -Force) }
```

---

## Preview delete command safely

```powershell
ls -Recurse -Filter *.tmp | Remove-Item -WhatIf
```

Then actually delete:

```powershell
ls -Recurse -Filter *.tmp | Remove-Item
```

---

# Python/Jupyter-Specific Commands

## Check Python location

```powershell
where.exe python
```

```powershell
python --version
```

---

## Create virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Deactivate:

```powershell
deactivate
```

---

## Install packages

```powershell
pip install jupyterlab numpy matplotlib sympy
```

Better:

```powershell
python -m pip install jupyterlab numpy matplotlib sympy
```

---

## Start JupyterLab

```powershell
jupyter lab
```

or:

```powershell
python -m jupyter lab
```

---

## Freeze dependencies

```powershell
python -m pip freeze > requirements.txt
```

Install from requirements:

```powershell
python -m pip install -r requirements.txt
```

---

# Recommended Scripts to Add Later

## `jl.ps1`

Launch JupyterLab from the current folder.

```powershell
python -m jupyter lab
```

Usage:

```powershell
jl
```

---

## `mkpyproj.ps1`

Create a basic Python project structure.

```powershell
param(
    [string]$Name
)

mkdir $Name
mkdir "$Name\src"
mkdir "$Name\notebooks"
mkdir "$Name\tests"

New-Item "$Name\README.md"
New-Item "$Name\requirements.txt"
New-Item "$Name\.gitignore"

Set-Content "$Name\.gitignore" @"
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
"@
```

Usage:

```powershell
mkpyproj python_lab
```

---

## `venv.ps1`

Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Usage:

```powershell
venv
```

---

## `treepy.ps1`

Show a cleaner project tree excluding noisy folders.

```powershell
Get-ChildItem -Recurse |
    Where-Object {
        $_.FullName -notmatch "\\.venv\\" -and
        $_.FullName -notmatch "__pycache__" -and
        $_.FullName -notmatch ".git"
    } |
    Select-Object FullName
```

Usage:

```powershell
treepy
```

---

# Most Important Habits

Use these constantly:

```powershell
pwd
ls
cd
mkdir
code .
explorer .
Get-Content
Select-String
where.exe python
python -m pip
```

And whenever deleting or moving many files, use:

```powershell
-WhatIf
```

That one flag can save you from a disaster.