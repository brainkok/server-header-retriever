import http.client
import ssl

def retrieve_server_header(filename):
    with open(filename) as f:
        websites = [line.strip() for line in f.readlines()]

    for website in websites:
        url = website.replace("https://", "").replace("http://", "")
        try:
            conn = http.client.HTTPSConnection(url, context=ssl._create_unverified_context())
            conn.request("GET", "/")
            res = conn.getresponse()
            server = res.getheader('Server')
            if server and any(char.isdigit() for char in server):
                print(f"Server header of {website}: {server}")
        except Exception as e:
            pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>.txt")
        sys.exit()

    filename = sys.argv[1]
    retrieve_server_header(filename)
