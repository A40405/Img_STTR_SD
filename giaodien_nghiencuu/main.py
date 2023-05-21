from flask import Flask, render_template, request, redirect, send_from_directory
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__, template_folder='.')



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/style_images')
def style_images_web():
    return render_template('style_images.html')
@app.route('/text_to_images')
def text_to_images_web():
    return render_template('text_to_images.html')
@app.route('/image_to_image')
def image_to_image_web():
    return render_template('image_to_image.html')


@app.route('/style_images', methods=['GET', 'POST'])
def style_images():
    if request.method == 'POST':
        output_dir = 'image_output1'
        # if os.path.exists(output_dir):
        #     os.remove(output_dir)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        content_images = request.files.getlist('content_images')
        style_images = request.files.getlist('style_images')

        error_message = None # Danh sách thông báo lỗi

        for content_image in content_images:
            if content_image.filename == '':
                error_message= "Content Image are empty pictures."
            else:
                content_image.save(os.path.join(output_dir, content_image.filename))

        for style_image in style_images:
            if style_image.filename == '':
                if error_message:
                    error_message+= "Style Image are empty pictures."
                else: error_message= "Style Image are empty pictures."
            else:
                style_image.save(os.path.join(output_dir, style_image.filename))

        if error_message:
            return render_template('style_images.html', errors=error_message)
        # Xử lý tạo ảnh từ ảnh ở đây (chưa được triển khai)
        
        success = True
        return render_template('style_images.html', success=success)
    
    return redirect('/')
@app.route('/text_to_images', methods=['GET', 'POST'])
def text_to_images():
    if request.method == 'POST':
        text = request.form['text']
        
        error_message = None 
        
        if text == '':
            error_message = "Text is empty."
        elif not text.isascii():
            error_message = "Enter text in English."
        
        if error_message:
            return render_template('text_to_images.html', errors=error_message)
        # Xử lý tạo ảnh từ văn bản ở đây (chưa được triển khai)
        
        
        success = True
        return render_template('text_to_images.html', success=success)
    return redirect('/')

@app.route('/image_to_image', methods=['GET', 'POST'])
def image_to_image():
    if request.method == 'POST':
        output_dir = 'image_output3'
        # if os.path.exists(output_dir):
        #     os.remove(output_dir)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        files = request.files.getlist('images')
        
        error_message = None  # Danh sách thông báo lỗi

        for file in files:
            if file.filename == '':
                error_message = "One or more images are empty."
            else:
                file.save(os.path.join(output_dir, file.filename))
        
        # Kiểm tra nếu có thông báo lỗi, trả về template với danh sách thông báo lỗi
        if error_message:
            return render_template('image_to_image.html', errors=error_message)
        
        text = request.form['text']
        strength = float(request.form['strength'])
        print(strength)
        # Xử lý tạo ảnh từ ảnh ở đây (chưa được triển khai)
        
        
        
        success = True
        return render_template('image_to_image.html', success=success)

    return redirect('/')

@app.route('/download_images1')
def download_images1():
    directory = 'image_output1'
    zip_file = 'images.zip'
    
    if os.path.exists(zip_file):
        os.remove(zip_file)
        
    os.system(f'zip -r {zip_file} {directory}')
    return send_from_directory('.', zip_file, as_attachment=True)

@app.route('/download_images2')
def download_images2():
    directory = 'image_output'
    zip_file = 'images.zip'
    if os.path.exists(zip_file):
        os.remove(zip_file)

    os.system(f'zip -r {zip_file} {directory}')
    return send_from_directory('.', zip_file, as_attachment=True)

@app.route('/download_images3')
def download_images3():
    directory = 'image_output3'
    zip_file = 'images.zip'
    if os.path.exists(zip_file):
        os.remove(zip_file)
        
    os.system(f'zip -r {zip_file} {directory}')
    return send_from_directory('.', zip_file, as_attachment=True)

if __name__ == '__main__':
    app.run()