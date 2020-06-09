import logging


class BaseTestCase(object):
    logging.basicConfig()
    _logger = logging.getLogger("gongzuo")
    _logger.setLevel(level=logging.DEBUG)

    @property
    def logger(self):
        return self._logger


