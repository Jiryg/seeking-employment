import logging


class BaseTestCase(object):
    logging.basicConfig()
    _logger = logging.getLogger("boss")
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    _logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    _logger.addHandler(ch)

    @property
    def logger(self):
        return self._logger