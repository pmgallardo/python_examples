import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run(name: str = "") -> None:
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        resp = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        print("Response:", resp.message)


if __name__ == "__main__":
    run("Alice")
