import cx_Freeze

executables = [cx_Freeze.Executable('Automation.py', icon='criptomoeda.ico')]

cx_Freeze.setup(
    name="Robotic - Criptos",
    options={'build_exe': {'packages': ['selenium', 'openpyxl', 'datetime'],
                           'include_files': ['Data Base.xlsx']}},
    executables=executables
)
