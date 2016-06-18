from nameko.rpc import rpc, RpcProxy
import datetime
import time


class Receiver(object):
    """This class receive some data and call the rpc function to
    log down the data.
    """
    name = "receiver"
    receiver = RpcProxy('logger')

    @rpc
    def received(self, data):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.receiver.log_data.async(st + " " + data)
        return "Received data, will log it"
