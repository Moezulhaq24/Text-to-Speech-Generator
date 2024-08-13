# Text-to-Speech Generator

This project provides a simple web application for converting text to speech using a pre-trained model. The application is built with Streamlit and leverages the VITS model from Hugging Face's Transformers library to generate speech from text input.

## Features

- **Text-to-Speech Conversion:** Input text and generate speech using a state-of-the-art model.
- **Audio Playback:** Listen to the generated speech directly in your browser.
- **User-Friendly Interface:** Simple and intuitive interface built with Streamlit.

## Prerequisites

Before running the application, make sure you have the following:

- **Python 3.x**
- **Required Python Packages:** Install the dependencies listed in `requirements.txt`.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**

   ```bash
   streamlit run your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the Python script that contains your Streamlit app.

## Usage

1. **Open the Web App:**

   After running the application, open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

2. **Generate Speech:**

   - Enter the text you want to convert to speech in the text input field.
   - Click the "Generate Speech" button to produce the audio.
   - Listen to the generated speech directly on the page.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository.
