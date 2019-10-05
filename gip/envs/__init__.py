import os
from pathlib import Path


def get_application_local_dir():
    """Get directory to save application config etc.

    Returns:
        Path
    """
    if os.name == 'nt':
        return Path(os.environ.get('LOCALAPPDATA')) / 'cip'
    else:
        return Path(os.environ.get('HOME') / '.gip')


def get_log_dir():
    """Get log directory

    Returns:
        Path: 
    """
    return Path(get_application_local_dir() / 'log')
