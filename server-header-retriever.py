import http.client
import ssl
import sys

def get_server_header(file):
    with open(file) as f:
        websites = [line.strip() for line in f.readlines()]

    for website in websites:
        website = website.replace("http://", "").replace("https://", "")
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        try:
            conn = http.client.HTTPSConnection(website, context=context)
            conn.request("GET", "/")
            res = conn.getresponse()
            print(f"Server header from {website}: {res.getheader('Server')}")
        except:
            print(f"Cannot connect to {website}")

file = sys.argv[1]
get_server_header(file)
