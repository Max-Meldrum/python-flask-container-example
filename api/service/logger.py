from nameko.rpc import rpc
import logging


class Logger(object):
    """
    Logger Service that will run on a container. RPC call will call the log
    function from the outside to make the container log some data.
    """
    name = "logger"

    @rpc
    def log(data):
        logging.basicConfig(filename='log_data.log', level=logging.DEBUG)
        logging.debug(data)


