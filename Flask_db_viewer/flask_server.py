import webbrowser
import threading
from flask import Flask, render_template, session, redirect, url_for
from waitress import serve
from db_queries import *

#note for GPT - this stack uses lists of dctionaries as best practice"

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session storage

#Key part of the script - run the server locally
def run_server(host="127.0.0.1", port=5000):
    """Starts the Flask server using Waitress and opens the browser."""
    def start_server():
        serve(app, host=host, port=port)

    webbrowser.open(f"http://{host}:{port}/")

    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    input("Press Enter to stop the server...\n")
    print("Shutting down server...")

@app.route("/")
def home():
    """Display all recipes on the homepage."""
    recipes = get_all_recipes()  # Now returns list of dictionaries
    return render_template("table.html", recipes=recipes)

@app.route("/<int:recipe_id>")
def recipe_details(recipe_id):
    recipe = get_recipe_details_by_id(recipe_id)
    print(recipe)
    
    if recipe is None:
        return "Recipe not found", 404  # Handle missing recipes gracefully
    
    return render_template("recipe_details.html", recipe=recipe)

@app.route("/<int:recipe_id>/clock")
def clock_page(recipe_id):
    recipe = get_recipe_details_by_id(recipe_id)
    
    if recipe is None:
        return "Recipe not found", 404

    return render_template("clock.html", recipe_name=recipe["name"], recipe_id=recipe["id"])  # Now it renders the correct template

@app.route("/<int:recipe_id>/diary")
def diary_page(recipe_id):
    return render_template("diary.html", recipe_id=recipe_id)

if __name__ == '__main__':
    run_server()
    
