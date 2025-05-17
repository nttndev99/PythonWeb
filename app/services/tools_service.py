import base64
import difflib
import hashlib
from io import BytesIO
import random
import string
from typing import Counter
from PIL import Image

# --------------------------
def generate_random_string(length=8, use_upper=True, use_digits=True, use_symbols=False):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# --------------------------
def hash_string(input_string, algorithm):
    encoded_string = input_string.encode()
    if algorithm == 'md5':
        return hashlib.md5(encoded_string).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(encoded_string).hexdigest()
    elif algorithm == 'sha3_224':
        return hashlib.sha3_224(encoded_string).hexdigest()    
    elif algorithm == 'sha3_256':
        return hashlib.sha3_256(encoded_string).hexdigest()    
    elif algorithm == 'sha3_384':
        return hashlib.sha3_384(encoded_string).hexdigest()    
    elif algorithm == 'sha3_512':
        return hashlib.sha3_512(encoded_string).hexdigest()
    else:
        return "Unsupported algorithm"
 
 # --------------------------   
def analyze_text(text):
    words = text.split()
    characters = len(text)
    lines = text.strip().split('\n')
    word_freq = Counter(words)
    return {
        'word_count': len(words),
        'char_count': characters,
        'line_count': len(lines),
        'word_frequency': word_freq
    }
    
# --------------------------
def generate_diff(text1, text2):
    lines1 = text1.strip().splitlines()
    lines2 = text2.strip().splitlines()

    matcher = difflib.SequenceMatcher(None, lines1, lines2)
    diff_rows = []
    line_num = 1

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        max_len = max(i2 - i1, j2 - j1)
        for i in range(max_len):
            line1 = lines1[i1 + i] if i1 + i < i2 else ''
            line2 = lines2[j1 + i] if j1 + i < j2 else ''

            diff_rows.append({
                'tag': tag,
                'left': line1,
                'right': line2,
                'line_no': line_num
            })
            line_num += 1

    return diff_rows

# --------------------------
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def find_duplicate_lines(text):
    return find_duplicates(text.strip().splitlines())

def find_duplicate_chars(text):
    from collections import Counter
    text = text.replace(" ", "").lower()
    counts = Counter(text)
    return [char for char, count in counts.items() if count > 1]

def find_word_duplicates(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    return find_duplicates(words)

# --------------------------
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ': '/'  
}
def text_to_morse_service(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)

# --------------------------
def convert_number(value: str, from_base: int, to_base: int) -> str:
    try:
        number = int(value, from_base)

        if to_base == 2:
            return bin(number)[2:]
        elif to_base == 8:
            return oct(number)[2:]
        elif to_base == 10:
            return str(number)
        elif to_base == 16:
            return hex(number)[2:].upper()
        else:
            return f"Unsupported base: {to_base}"
    except ValueError:
        return "Invalid input number"
    
# --------------------------
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_image(file):
    try:
        img = Image.open(file)
        img.verify()  
        file.seek(0)  
        return True
    except Exception:
        return False
    
def resize_image(file, max_width=None, max_height=None, output_format='JPEG'):
    phi = 1.618

    img = Image.open(file)

    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGB')

    width, height = img.size

    if max_width and not max_height:
        max_height = int(max_width / phi)
    elif max_height and not max_width:
        max_width = int(max_height * phi)
    elif not max_width and not max_height:
        max_width = 300
        max_height = int(max_width / phi)

    scale = min(max_width / width, max_height / height)
    resized_width = int(width * scale)
    resized_height = int(height * scale)

    resized_img = img.resize((resized_width, resized_height))

    img_io = BytesIO()
    output_format = output_format.upper()

    if output_format == 'JPG': 
        output_format = 'JPEG'

    if output_format == 'JPEG' and resized_img.mode != 'RGB':
        resized_img = resized_img.convert('RGB')

    resized_img.save(img_io, format=output_format, quality=85)
    img_io.seek(0)

    mime_type = f'image/{output_format.lower()}'
    if output_format == 'JPEG':
        mime_type = 'image/jpeg'

    base64_img = base64.b64encode(img_io.read()).decode('ascii')
    return base64_img, mime_type, output_format.lower()

def image_file_to_base64(file):
    file.seek(0)
    img = Image.open(file)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality=85)
    img_io.seek(0)

    base64_img = base64.b64encode(img_io.read()).decode('ascii')
    return base64_img