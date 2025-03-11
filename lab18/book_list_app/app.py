from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)


@app.route('/')
def index():
    # Sample data list: each book is represented as a dictionary with a title and an author
    books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "1984", "author": "George Orwell"},
        {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]

    # Pass the list and a title string to the template
    return render_template("index.html", books=books, title="Book List")


if __name__ == '__main__':
    app.run(debug=True)
