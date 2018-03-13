# -*- mode: python -*-

block_cipher = None


a = Analysis(['icon=C:\\Users\\DavidSoden\\Documents\\GitHub\\Learning-Project\\Tic.ico', 'C:\\Users\\DavidSoden\\Documents\\GitHub\\Learning-Project\\tic-tac-toe.py'],
             pathex=['C:\\Users\\DavidSoden\\Documents\\GitHub\\Learning-Project'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Tic',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Tic')
