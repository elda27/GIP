import os
from pathlib import Path


def get_application_local_dir() -> Path:
    """Get directory to save application config etc.
    """
    if os.name == 'nt':
        return Path(os.environ.get('LOCALAPPDATA')) / 'cip'
    else:
        return Path(os.environ.get('HOME')) / '.gip'


def get_log_dir() -> Path:
    """Get log directory
    """
    return get_application_local_dir() / 'log'
