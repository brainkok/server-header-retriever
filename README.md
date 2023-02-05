Server header retriever
=====
This script is designed to retrieve the server header with a version number of websites stored in a text file. The script ignores both SSL errors and "connection refused" errors when retrieving the server header. 

Requirements:
~~~
Python 3.x
http.client module
ssl module
~~~

Usage:
Create a text file with the websites for which you want to retrieve the server header, each website on a new line.
Run the script in the terminal and pass the text file as an argument:
~~~
python3 server-header-retriever.py <filename>.txt
~~~
The script will then retrieve the server header with version number for each website in the text file and print it to the terminal. If it is not possible to connect to a website or the header does not contain a version number, the header will not be printed.

Note:
The script removes "http://" or "https://" from the URL before connecting to the server.
The script has been tested and works in Python 3.x.
The script is intended for educational purposes and should not be used for unauthorized purposes.
