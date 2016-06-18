from flask_restful import Resource, reqparse
from nameko.standalone.rpc import ClusterRpcProxy
from user import auth

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


class DumpAPI(Resource):
    """API resource for the dumping of data."""

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data', required=True, help="Enter some data")
        args = parser.parse_args()
        data = args['data']
        msg = "Data received, going to log it"
        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.receiver.received.async(data)
            return msg, 200
