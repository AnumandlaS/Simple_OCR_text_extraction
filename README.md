# Simple_OCR_text_extraction
This project aims to extract text from the images user inputs, a small step towards building Optical Character Recognition Models. I have used pytesseract a vey beginner friendly library for OCR. This project aims to provide users with an efficient tool to convert images containing text into editable and searchable text formats, supporting both English and Hindi languages.
# Note:
I have tried a lot to complete this task using ColPali (Byaldi library) + Huggingface transformers for Qwen2-VL, but I couldn't do it. Transformers require quite a good knowledge and RAM. I couldn't pull it off this time, but I will try to, some other time.
# Technical Stack
Frontend: Streamlit for building the web interface.
Backend: Python with OpenCV for image processing and Tesseract for OCR.
Libraries:
OpenCV for image manipulation and preprocessing.
Pytesseract for text extraction from images.
PIL (Pillow) for image handling.
# Key Features:
Image Upload: Users can upload images in 3 formats (PNG, JPG, JPEG) that contain printed text.
Multilingual Support: The application supports text extraction in 2 languages, English and Hindi.
Text Extraction: Utilizing the Tesseract OCR engine, the application processes the uploaded images and extracts the text, providing accurate results based on the specified language.
Text Highlighting: Users can search for specific words within the extracted text. The application highlights the searched words.
Responsive Design: The application features a user-friendly interface.
