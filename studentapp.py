from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Dummy student data
students = [
    {"id": 1, "name": "Roshan", "age": 20, "major": "Computer Science"},
    {"id": 2, "name": "Ridi", "age": 22, "major": "AI"},
    {"id": 3, "name": "Kushi", "age": 21, "major": "BCA"}
]

# API to get all students
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

# API to get a specific student by ID
@app.route('/api/student/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

# Home route that serves an HTML page
@app.route('/')
def home():
    html_content = '''
    <html>
        <head><title>Home Page</title></head>
        <body>
            <h1>Welcome to the Student Portal</h1>
            <p>This is the home page.</p>
            <a href="/about">Go to About Page</a>
        </body>
    </html>
    '''
    return render_template_string(html_content)

# About route that serves another HTML page
@app.route('/about')
def about():
    html_content = '''
    <html>
        <head><title>About Us</title></head>
        <body>
            <h1>About Our Application</h1>
            <p>This app provides information about students in our database.</p>
            <a href="/">Go to Home Page</a>
        </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
