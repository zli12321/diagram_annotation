from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


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
    slide_title = "Slide 1 Title"  # Example text content from the backend
    content1 = "Content 1"
    content2 = "Content 2"
    diagram_description = "Diagram 1 Description"
    new_content = "New content explanation"
    # Add more variables as needed for other text content

    return render_template('page2.html', pdf_filename=pdf_filename,
                           slide_title=slide_title, content1=content1,
                           content2=content2, diagram_description=diagram_description,
                           new_content=new_content)



@app.route('/save-text-page2', methods=['POST'])
def save_text_page2():
    input_detail = request.form['input-detail']
    input_specs = request.form['input-specs']
    # Handle the input from the second page form here
    print(input_detail, input_specs)  # for debugging
    # Redirect to a new page or back to page 2, depending on your flow
    return redirect(url_for('page2'))  # or some other page


if __name__ == '__main__':
    app.run(debug=True)
