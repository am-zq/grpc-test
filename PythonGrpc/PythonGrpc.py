import os
import grpc

# Added proto dir to VS Search Paths to get it to find these modules
import greet_pb2_grpc
from greet_pb2 import HelloRequest

# For debugging:
#os.environ['GRPC_TRACE'] = 'all'
#os.environ['GRPC_VERBOSITY'] = 'DEBUG'

address = 'localhost:5000'
channel = grpc.insecure_channel(address)
stub = greet_pb2_grpc.GreeterStub(channel)

try:
    request = HelloRequest()
    request.name = "Bob"
    response = stub.SayHello(request)

    print(response.message)

except grpc._channel._InactiveRpcError as e:
    print(e)
    if e.code() == grpc.StatusCode.UNAVAILABLE:
        print(f'Could not connect to {address}')
