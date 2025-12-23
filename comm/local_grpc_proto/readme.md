# Local gRPC + protobuf example in Python 

## Description

The `proto/` folder contains a `.proto` file that contains the objects used by a client and a server that run locally.

## How to setup virtual environment

In Linux:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install grpcio grpcio-tools protobuf
```

In Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install grpcio grpcio-tools protobuf
```

## How to run it

Create the Python files for 

```shell
python -m grpc_tools.protoc \
  -I src/proto \
  --python_out=src \
  --grpc_python_out=src \
  src/proto/helloworld.proto
```

Run the server:
  
python src/py_server.py

Run the client

python src/py_client.py

