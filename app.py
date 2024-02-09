import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from classify import classify_image
from upload import upload_and_classify

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = '/Users/harshil/Development/ComputerVisionAPP_Harshil/static/uploads'
    app.secret_key = '123'  # Essential for session management and flash messages
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            # This assumes the form on your upload.html submits to '/upload'
            # and not to '/', hence might not be directly called unless form action is updated
            return redirect(url_for('upload'))
        return render_template('upload.html')

    @app.route('/upload', methods=['POST'])
    def upload():
        # Assuming 'upload_and_classify' handles file upload, classification, and redirection
        response = upload_and_classify()
        # You can add any additional processing here if needed
        return response


    @app.route('/result')
    def result():
        class_name = request.args.get('class_name', "Unknown")
        confidence_str = request.args.get('confidence', "0")  # Received as string
        confidence = float(confidence_str)  # Convert to float for rounding
    
        return render_template('results.html', label=class_name, confidence=confidence)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)