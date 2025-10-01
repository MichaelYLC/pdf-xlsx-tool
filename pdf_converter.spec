# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['pdf_to_excel.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('pdf_converter_tools', 'pdf_converter_tools'),
        ('converted_examples', 'converted_examples'),
        ('15100堆高機操作(程式檔)-中+印+越+英.xlsx', '.'),
    ],
    hiddenimports=[
        'pandas',
        'PyPDF2',
        'pdfplumber',
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
