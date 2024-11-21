Mini Local Web App Documentation

Overview

This mini app runs a local web server on your device, serving a simple HTML page that fetches and displays data from a JSON file. The setup is entirely offline, leveraging Python, HTML, JavaScript, and JSON to provide a complete web-like experience.

File Structure

Your folder should include:

server_script.py: The Python script to start the local server.

index.html: The main HTML page displayed in the browser.

scriptlog.json: A JSON file storing data accessed by the HTML page.


Components and Logic

1. Python Local Server (server_script.py):

Starts a local server using Python’s built-in http.server module.

Serves files from the current directory on a random port each time.

Opens a browser window/tab pointing to localhost:<PORT> where the app runs.

The server only accepts connections from the device itself (localhost), so it remains offline and secure.



2. HTML File (index.html):

Acts as the main interface for the app, structured with basic HTML.

Contains an element (<h1 id="ran_in">) that initially displays "Fetching data..." as a placeholder.



3. JavaScript Logic (inside index.html):

Uses JavaScript’s fetch API to load data from scriptlog.json.

Parses the JSON data and dynamically updates the HTML to show relevant information.

For example, it reads the ran_in value for a specific date in the JSON and displays it by updating the <h1 id="ran_in"> element.

Includes error handling: if scriptlog.json can’t be accessed or is empty, it logs an error to the console and updates the <h1> element to show "Error fetching data."



4. Data Source (scriptlog.json):

This JSON file acts as the data source for the app.

Contains key-value pairs with information that the HTML and JavaScript will display.

Example JSON structure:

{
    "2024-10-20": {
        "ran_in": "Python Server"
    }
}

The JavaScript reads ran_in under the specified date and displays it on the page.




Usage

1. Place index.html and scriptlog.json in the same folder as server_script.py.


2. Run server_script.py: This starts a server and opens index.html in your browser.


3. View the Result: The HTML page fetches data from scriptlog.json, showing dynamic content based on the JSON values.



Notes

Offline Operation: This app is fully offline. The server only runs locally on your device and doesn’t use the internet.

Privacy and Security: Since it only runs on localhost, it is isolated and secure, with no risk of exposure to outside networks.


Dependencies

Python 3 (for running the local server)


Example Commands

To start the server, open a terminal, navigate to the folder, and run:

python server_script.py
