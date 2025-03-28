import http.server
import socketserver
import webbrowser
import threading
import random
import os
import time

def run_server():
    """Starts a local HTTP server, opens a browser, and waits for user input to stop."""
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            return  # Suppresses request logging in the console
    
    def start_server(httpd):
        print(f"Serving on port {httpd.server_address[1]}")
        httpd.serve_forever()

    def open_browser(port):
        webbrowser.open(f'http://localhost:{port}')

    # Generate a random available port
    PORT = random.randint(1024, 65535)

    # Ensure the current directory is set correctly
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Create and start the server, binding it to localhost
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        # Start server in a separate thread
        server_thread = threading.Thread(target=start_server, args=(httpd,))
        server_thread.daemon = True
        server_thread.start()

        # Small delay to ensure server starts before opening browser
        time.sleep(1)
        open_browser(PORT)

        try:
            input("Press Enter to stop the server...\n")
        except KeyboardInterrupt:
            print("\nServer shutting down...")

        # Shutdown server properly
        httpd.shutdown()
        httpd.server_close()
        print("Server stopped.")

if __name__ == "__main__":
    run_server()