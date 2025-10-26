from PyInstaller.utils.hooks import collect_all

# This function tells PyInstaller what files to include when 'playsound' is imported.
def hook(hook_api):
    # 1. Force hidden imports for core playsound dependencies
    hiddenimports = [
        'playsound',
        'pydub',
        'pydub.utils',
        'pydub.exceptions',
        'os',
        'winsound' # The Windows audio module
    ]

    # 2. Collect any external files (like libraries for audio playback)
    # Note: On Windows, playsound often relies on the operating system for playback.
    # We include pydub here just in case.
    
    # 3. Use collect_all to automatically find and include all related files/submodules
    return collect_all(
        'playsound',
        hiddenimports=hiddenimports
    )