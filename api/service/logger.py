from nameko.rpc import rpc


class Logger(object):
    """
    Logger Service that will run on a container. RPC call will call the log
    function from the outside to make the container log some data.
    """
    name = "logger"

    @rpc
    def log_data(self, data):
        with open('data.log', 'a') as f:
            f.write(data + "\n")
        print("logged")
