import base64
import io
from flask import Blueprint, render_template, request

from app.services.tools_service import *

tools_bp = Blueprint('tools', __name__)

# -------------------------------------------------
@tools_bp.route('/random-string-generator',methods=['GET', 'POST'])
def random_string_generator():
    random_string = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_upper = 'use_upper' in request.form
        use_digits = 'use_digits' in request.form
        use_symbols = 'use_symbols' in request.form

        random_string = generate_random_string(length, use_upper, use_digits, use_symbols)

    return render_template('tools_templates/random_string_generator.html', random_string=random_string)
# -------------------------------------------------
@tools_bp.route('/hash-generator',methods=['GET', 'POST'])
def hash_generator():
    original_text = ''
    hashed_text = ''
    algorithm = 'md5'

    if request.method == 'POST':
        original_text = request.form.get('text', '')
        algorithm = request.form.get('algorithm', 'md5')
        hashed_text = hash_string(original_text, algorithm)

    return render_template('tools_templates/hash_generator.html', text=original_text, hash_result=hashed_text, algorithm=algorithm)
# -------------------------------------------------
@tools_bp.route('/word-counter',methods=['GET', 'POST'])
def word_counter():
    text = ''
    result = {}
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = analyze_text(text)
    return render_template('tools_templates/word_counter.html', text=text, result=result)
# -------------------------------------------------
@tools_bp.route('/text-diff-checker', methods=['GET', 'POST'])
def text_diff_checker():
    text1 = ''
    text2 = ''
    diff_rows = []

    if request.method == 'POST':
        text1 = request.form.get('text1', '')
        text2 = request.form.get('text2', '')
        diff_rows = generate_diff(text1, text2)

    return render_template('tools_templates/text_diff_checker.html', text1=text1, text2=text2, diff_rows=diff_rows)
# -------------------------------------------------
@tools_bp.route('/find_duplicates', methods=['GET', 'POST'])
def find_duplicates():
    input_text = ''
    line_dups = []
    char_dups = []
    word_dups = []

    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        check_lines = request.form.get('check_lines')
        check_chars = request.form.get('check_chars')
        check_words = request.form.get('check_words')

        if check_lines:
            line_dups = find_duplicate_lines(input_text)
        if check_chars:
            char_dups = find_duplicate_chars(input_text)
        if check_words:
            word_dups = find_word_duplicates(input_text)
            
    return render_template('tools_templates/find_duplicates.html',  
                            input_text=input_text,
                            line_dups=line_dups,
                            char_dups=char_dups,
                            word_dups=word_dups)
# -------------------------------------------------
@tools_bp.route('/text-to-morse', methods=['GET', 'POST'])
def text_to_morse():
    input_text = ''
    morse_result = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        morse_result = text_to_morse_service(input_text)           
    return render_template('tools_templates/text_to_morse.html', input_text=input_text, morse_result=morse_result)
# -------------------------------------------------
@tools_bp.route('/number-converter', methods=['GET', 'POST'])
def number_converter():
    input_value = ''
    from_base = '10'
    to_base = '2'
    result = ''

    if request.method == 'POST':
        input_value = request.form.get('input_value', '').strip()
        from_base = int(request.form.get('from_base', '10'))
        to_base = int(request.form.get('to_base', '2'))
        result = convert_number(input_value, from_base, to_base)

    return render_template('tools_templates/number_converter.html',
                           input_value=input_value,
                           from_base=from_base,
                           to_base=to_base,
                           result=result)
# -------------------------------------------------
@tools_bp.route('/images-converter', methods=['GET', 'POST'])
def images_converter():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file to upload"
        file = request.files['image']
        if file.filename == '':
            return "No file selected"
        if not allowed_file(file.filename):
            return "Only valid image files are allowed"
        if not is_image(file):
            return "File is not a valid image"

        output_format = request.form.get('format') or 'JPEG'

        max_width = request.form.get('max_width')
        max_height = request.form.get('max_height')

        max_width = int(max_width) if max_width and max_width.isdigit() else None
        max_height = int(max_height) if max_height and max_height.isdigit() else None

        original_img = image_file_to_base64(file)
        file.seek(0)

        resized_img, mime_type, extension = resize_image(
            file, max_width=max_width, max_height=max_height, output_format=output_format
        )

        return render_template('tools_templates/images_convert.html',  
                               original_img=original_img,
                               resized_img=resized_img,
                               mime_type=mime_type,
                               extension=extension)

    return render_template('tools_templates/images_convert.html', original_img=None, resized_img=None)