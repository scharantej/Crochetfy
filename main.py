
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

@app.route('/purchase')
def purchase():
    """Handles the purchase process."""
    # Implement the purchase process here
    return render_template('purchase.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
