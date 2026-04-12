# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['pdf_to_excel.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('pdf_xlsx_tool', 'pdf_xlsx_tool'),
        ('examples', 'examples'),
    ],
    hiddenimports=[
        'pdfplumber',
        'pdf_xlsx_tool',
        'pdf_xlsx_tool.converter',
        'openpyxl',
        'openpyxl.workbook',
        'openpyxl.worksheet',
        'openpyxl.styles',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PDF_to_Excel_Converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
