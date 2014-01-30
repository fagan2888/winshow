# -*- mode: python -*-
a = Analysis(['src/winshow.pyw'],
             pathex=['./scripts'],
             hiddenimports=[],
             hookspath=['./scripts/hooks'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='winshow.exe',
          debug=False,
          strip=None,
          upx=False,
          console=False )
