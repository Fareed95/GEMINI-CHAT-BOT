# bot_image.py

import PIL.Image
import textwrap
import google.generativeai as genai

def bot_gemini(text, *image_paths):
    images = []
    for path in image_paths:
        if path:
            img = PIL.Image.open(path)
            images.append(img)
        else:
            images.append(None)

    def to_markdown(text):
        text = text.replace('•', '  *')
        return textwrap.indent(text, '> ', predicate=lambda _: True)

    GOOGLE_API_KEY = 'AIzaSyDLW0ZzUp32rgwCYVMsnTGNwuhn1ZOTels'

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content([text, *images], stream=True)
    response.resolve()
    content = response.candidates[0].content.parts[0].text

    return to_markdown(content)
