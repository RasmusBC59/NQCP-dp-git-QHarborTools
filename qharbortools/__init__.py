import logging
import qharbortools._version


__version__ = qharbortools._version.__version__


logger = logging.getLogger(__name__)
logger.info(f"Imported qharbortoolsversion: {__version__}")
