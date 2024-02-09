import os
from werkzeug.utils import secure_filename
from flask import current_app, flash, redirect, url_for, request
from classify import classify_image  # Ensure this import works as expected.

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def upload_and_classify():
    """Handles the uploading and classification of an image."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Classify the image
        class_name, confidence = classify_image(filepath)

        # Redirect to the results page with classification info
        # Here we use 'url_for' with the name of the result view function and pass the classification results as query parameters
        return redirect(url_for('result', class_name=class_name, confidence="{:.2f}".format(confidence)))
    else:
        flash('Allowed file types are: png, jpg, jpeg, gif')
        return redirect(request.url)