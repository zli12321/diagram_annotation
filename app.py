from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import jsonify
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set to a unique and secret value

@app.route('/')
def index():
    # Pass the necessary parameters to the template
    # Your text content
    text_content_1 = "Contribution/Novelty of the paper : New Dataset/Method/Analysis of existing approaches"
    text_content_2 = '''Suggested Slide Titles: (We will also provide the slides in existing doc2slides dataset for help)
    Title 1 (User can edit/modify)
    Title 2
    Title 3
    '''
    return render_template('index.html',
                           text_content_1=text_content_1,
                           text_content_2=text_content_2,
                           pdf_filename='paper1.pdf')

@app.route('/pdf/<path:filename>')
def serve_pdf(filename):
    # Send the PDF file from within the static directory
    return send_from_directory('static/pdfs', filename)

@app.route('/save-text', methods=['POST'])
def save_text():
    user_input = request.form['user-input']
    # Here you would handle saving the user input to the backend
    print(user_input)  # for debugging, replace with your save logic
    # Redirect to the second page instead of the index
    return redirect(url_for('page2'))

@app.route('/page2')
def page2():
    pdf_filename = 'paper1.pdf'  # replace with your actual PDF file name or a variable
    description = "Intent or description of the diagram"
    editable_content = '''(LLM generates questions in front of the user and users can change/edit)
Model-generated clarification questions (subject to change by the users- edit/add/delete):
Ques1 (What)
Ques2 (What)
Ques3 (How)
Ques4 (How)
Ques5 (What)
Ques6 (How)
Ques7 (How)
'''
    return render_template('page2.html', pdf_filename=pdf_filename,
                           description=description, editable_content=editable_content)

@app.route('/handle_editable_content', methods=['POST'])
def handle_editable_content():
    content = request.form['editable-content']
    # Process and save the content
    print(content)  # Replace with your save logic

    # TODO: Save the content as needed here

    # After saving, redirect to page3
    return redirect(url_for('page3'))


@app.route('/page3')
def page3():
    pdf_filename = 'paper1.pdf'  # The same PDF as before
    description = "Intent or description of the diagram"
    # Presumably the LLM has generated some answers that you want to display
    answer1 = "Answer 1"
    answer2 = "Answer 2"
    answer5 = "Answer 5"
    # A list of questions for which you want user input
    questions = ['Question 3', 'Question 4', 'Question 6', 'Question 7']
    
    return render_template('page3.html', pdf_filename=pdf_filename,
                           description=description, answer1=answer1,
                           answer2=answer2, answer5=answer5,
                           questions=questions)

@app.route('/handle_answers', methods=['POST'])
def handle_answers():
    # Process each question's answer
    answers = {key: request.form[key] for key in request.form.keys()}
    # TODO: Save or process answers as needed here

    print(answers)  # For debugging, replace with your save logic

    # After saving, redirect to page4
    return redirect(url_for('page4'))


@app.route('/page4')
def page4():
    pdf_filename = 'paper1.pdf'
    textual_description = "LLM extracted data for generating diagram"
    code_content = "# Your generated Python code here\nprint('Hello, world!')"
    image_path = 'images/logo.png'  # Relative path within the static directory

    # Pass the variables to the template
    return render_template('page4.html', 
                           pdf_filename=pdf_filename,
                           textual_description=textual_description,
                           code_content=code_content,
                           image_path=image_path)


@app.route('/handle_feedback', methods=['POST'])
def handle_feedback():
    # Extract feedback from the form
    correctness_feedback = request.form.get('correctness')
    completeness_feedback = request.form.get('completeness')
    layout_feedback = request.form.get('layout')
    action = request.form.get('action')

    # Retrieve old data from session or initialize if not present
    old_textual_description = session.get('textual_description', "LLM extracted data for generating diagram")
    old_code_content = session.get('code_content', "# Your generated Python code here\nprint('Hello, world!')")
    old_image_path = session.get('image_path', 'images/logo.png')

    if action == 'save':
        # Logic to save the feedback
        # This is where you would implement your saving logic, for example, saving to a file or database

        # After saving, redirect to the index route
        return redirect(url_for('index'))
    elif action == 'regenerate':
        # Logic to regenerate the diagram based on feedback
        # Regenerate logic

        # Assume a function to regenerate and return the new code and image path
        new_code = "# New generated code\nprint('Hello again!')"
        new_image_path = 'images/logo1.png'

        # Update session with new generated data
        session['code_content'] = new_code
        session['image_path'] = new_image_path

    # Render the template with both old and updated new data
    return render_template('page4.html',
                           pdf_filename=session.get('pdf_filename', 'paper1.pdf'),
                           textual_description=old_textual_description,
                           code_content=session.get('code_content', old_code_content),
                           image_path=session.get('image_path', old_image_path))


if __name__ == '__main__':
    app.run(debug=True)
