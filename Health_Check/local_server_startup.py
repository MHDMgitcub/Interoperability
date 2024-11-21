import http.server
import socketserver
import webbrowser
import threading
import random
import os

# Define the handler
Handler = http.server.SimpleHTTPRequestHandler

def start_server(httpd):
    print(f"Serving on port {httpd.server_address[1]}")
    httpd.serve_forever()

# Open browser automatically
def open_browser(port):
    webbrowser.open(f'http://localhost:{port}')

# Generate a random port between 1024 and 65535
PORT = random.randint(1024, 65535)

# Ensure we are serving files from the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create and start the server, bind it to localhost (127.0.0.1) only
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    # Start server in a separate thread
    server_thread = threading.Thread(target=start_server, args=(httpd,))
    server_thread.daemon = True  # Allows the program to exit even if the server is still running
    server_thread.start()

    # Open the browser
    open_browser(PORT)

    # Wait for user input to close the server
    input("Press Enter to stop the server...\n")

    # Shutdown the server properly
    httpd.shutdown()
    httpd.server_close()
    print("Server stopped.")
    