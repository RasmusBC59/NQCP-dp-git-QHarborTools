import logging
import qhabortools._version


__version__ = qhabortools._version.__version__


logger = logging.getLogger(__name__)
logger.info(f"Imported qhabortoolsversion: {__version__}")
