# HTTP + JSON example in Python

## Prerequisites

### Host dependencies

uvicorn is necessary.

To install it on environments where it is available (e.g. Ubuntu):

```shell
sudo apt install uvicorn uvicorn[standard]
```

### Python virtual environment

Using a virtual environment is optional, but safer.

Go to the project folder.

Install virtual environment:

```shell
python3 -m venv .venv
```

Activate the installed virtual environment in Linux:

```shell
source .venv/bin/activate
```

### Python dependencies

Server dependencies:

```shell
pip install fastapi uvicorn
```

Client dependencies:

```shell
pip install requests
```

## Running

Running server:

```shell
python -m uvicorn server:app --host 127.0.0.1 --port 8000
```

`server` refers to the `server.py` file.
`app` refers to the variable name that contains the FastAPI.

Running client:

```shell
python3 server.py
```
