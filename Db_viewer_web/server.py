from flask import Flask, render_template
import threading
import webbrowser
import random
import time
from database import get_recipe_data  # Import the function from database.py

# Initialise Flask app
app = Flask(__name__)

@app.route("/")
def index():
    recipe_data = get_recipe_data()  # Fetch data from database.py
    return render_template("index.html", recipe_data=recipe_data)

def run_server():
    """Starts Flask server and opens browser"""
    PORT = random.randint(1024, 65535)  # Random available port

    # Start Flask in a separate thread
    def start_flask():
        app.run(host="127.0.0.1", port=PORT, debug=False, use_reloader=False)
    
    server_thread = threading.Thread(target=start_flask)
    server_thread.daemon = True
    server_thread.start()

    # Wait for Flask to start
    time.sleep(1)
    webbrowser.open(f"http://127.0.0.1:{PORT}")

    try:
        input("Press Enter to stop the server...\n")
    except KeyboardInterrupt:
        print("\nShutting down...")

    print("Server stopped.")

if __name__ == "__main__":
    run_server()