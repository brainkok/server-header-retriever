#!/usr/bin/python3
import http.client
import ssl

def retrieve_headers(filename, show_version_only=True):
    with open(filename) as f:
        websites = [line.strip() for line in f.readlines()]

    for website in websites:
        url = website.replace("https://", "").replace("http://", "")
        try:
            conn = http.client.HTTPSConnection(url, context=ssl._create_unverified_context())
            conn.request("GET", "/")
            res = conn.getresponse()
            server = res.getheader('Server')
            x_powered_by = res.getheader('X-Powered-By')
            if show_version_only or (server and any(char.isdigit() for char in server)):
                print(f"Server header of {website}: {server}")
            if show_version_only or (x_powered_by and any(char.isdigit() for char in x_powered_by)):
                print(f"X-Powered-By header of {website}: {x_powered_by}")
        except Exception as e:
            pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) not in (2, 3):
        print("Usage: python3 server-header-retriever.py <filename>.txt [--version-only]")
        sys.exit()

    filename = sys.argv[1]
    show_version_only = len(sys.argv) == 2 or sys.argv[2] != "--version-only"
    retrieve_headers(filename, show_version_only)
