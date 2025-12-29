import requests

def main() -> None:
    # Set payload
    text_to_send = "Hello"

    # Set connection data
    host = "http://127.0.0.1"
    port = 8000
    
    # Connection URL construction
    url = host + ":" + str(port) + "/echo"

    dto = {"text": text_to_send}
    resp = requests.post(url, json=dto, timeout=5)
    resp.raise_for_status()

    # Takes response
    data = resp.json()
    # Display received message on screen
    print(data["text"])

if __name__ == "__main__":
    main()
