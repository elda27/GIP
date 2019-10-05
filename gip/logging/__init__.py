import logging
import logging.config
import os
import json
from pathlib import Path

from gip import envs


def initialize():
    app_dir = envs.get_application_local_dir()
    log_dir = envs.get_log_dir()
    if not log_dir.exists():
        log_dir.mkdir(exist_ok=True, parents=True)

    log_config = dict()
    log_config_filename = app_dir / 'log.conf'
    if not log_config_filename.exists():
        log_config = get_default_logging_config(log_dir)
        with open(log_config_filename, 'w+') as fp:
            fp.writelines(json.dumps(log_config))
    else:
        with open(log_config_filename, 'r') as fp:
            try:
                log_config = json.load(fp)
            except json.JSONDecodeError as e:
                print(
                    f'Wrong format log config({log_config_filename})\n'
                    f'{e}')
                raise e

    logging.config.dictConfig(log_config)


def get_logger(name):
    return logging.getLogger('gip.' + name)


def set_level(level):
    get_logger('gip').setLevel(level)


def get_default_logging_config(log_dir):
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            'verbose': {
                'format':
                    '%(levelname)s %(name)s %(asctime)s %(module)s'
                    '%(process)d %(thread)d %(pathname)s(%(lineno)s): '
                    '%(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(name)s %(filename)s(%(lineno)s): '
                          '%(message)s'
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "WARNING",
                "filters": []
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "verbose",
                "filename": str(log_dir / 'runtime_log.txt'),
                "level": "INFO",
                "filters": []
            }
        },
        "root": {
            "handlers": ["console"],
        },
        "gip": {
            "handlers": ["console"],
        },
        "gip.env": {
            "handlers": ["console"],
        },
        "gip.image": {
            "handlers": ["console"],
        },
        "gip.builtin": {
            "handlers": ["console"],
        },
    }
