import logging
import os
import sys

import coloredlogs

# __all__ = ["SomeClassOrMethod"]


log_level = logging.INFO

logger = logging.getLogger("app")
logger.setLevel(log_level)
format_string = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"

if "COLOREDLOGS_LEVEL_STYLES" not in os.environ:
    coloredlogs.DEFAULT_LEVEL_STYLES = {
        **coloredlogs.DEFAULT_LEVEL_STYLES,
        "trace": {"color": 246},
        "critical": {"background": "red"},
        "debug": coloredlogs.DEFAULT_LEVEL_STYLES["info"],
    }

if "COLOREDLOGS_LOG_FORMAT" not in os.environ:
    coloredlogs.DEFAULT_LOG_FORMAT = format_string

if "COLOREDLOGS_LOG_LEVEL" not in os.environ:
    coloredlogs.DEFAULT_LOG_LEVEL = log_level

coloredlogs.install(logger=logger, stream=sys.stdout)
