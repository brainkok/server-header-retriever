Server header retriever
=====
This script retrieves the HTTP headers for websites listed in a text file. The headers include the Server header and the X-Powered-By header. The script uses the Python http.client and ssl modules to connect to websites over HTTPS.

Requirements:
~~~
Python 3.x
http.client module
ssl module
~~~

Usage:
1. Create a text file with the websites for which you want to retrieve the server and x-powered-by header, each website on a new line.
2. Run the script, execute the following command in a terminal:
~~~
python script.py <filename>.txt [--version-only]
~~~
Where <filename>.txt is the name of the text file containing a list of websites, and --version-only is an optional argument that determines whether only the version of the server software should be displayed in the output.

Note:
The script removes "http://" or "https://" from the URL before connecting to the server.
The script has been tested and works in Python 3.x.
The script is intended for educational purposes and should not be used for unauthorized purposes.
