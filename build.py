import sys


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    print(sys.executable)
    from ruff.__main__ import find_ruff_bin
    raise RuntimeError(find_ruff_bin())



def build_wheel(wheel_directory, config_settings=None, metadata_directory=None): ...
def build_sdist(sdist_directory, config_settings=None): ...
