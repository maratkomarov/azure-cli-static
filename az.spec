# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_all, copy_metadata

block_cipher = None


datas, binaries, hiddenimports = [], [], []

# Only limited set of commands: profile, extension
for mod in ('azure.cli.core',
            'azure.cli.command_modules.profile',
            'azure.cli.command_modules.extension'):
    d, b, h = collect_all(mod)
    datas += d
    binaries += b
    hiddenimports += h

# `azure graph` is distributed as extension
datas += [
    ('/usr/local/lib/python3.6/site-packages/azure-cli-extensions',
    'lib/python3.6/site-packages/azure-cli-extensions')
]


a = Analysis(
    [os.path.join(HOMEPATH, 'azure/cli/__main__.py')],
    pathex=['/src'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    runtime_hooks=[],
    excludes=['pycrypto', 'PyInstaller'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='az',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True
)


