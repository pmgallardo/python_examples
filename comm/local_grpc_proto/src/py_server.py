from concurrent import futures
import grpc

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        name = request.name.strip()
        msg = "Hello world" if not name else f"Hello {name}"
        return helloworld_pb2.HelloReply(message=msg)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    print("Python gRPC server listening on 127.0.0.1:50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

