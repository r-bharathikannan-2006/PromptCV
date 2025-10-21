
# PromptCV: AI-Powered CV Generator

PromptCV is a dynamic web application built with Django that leverages the power of Google's Gemini AI to automatically generate professional CVs from a single text prompt. Users can input their professional details in a free-form text area, select a template, and receive a downloadable, well-formatted CV in `.docx` format.

## Live Demo

Check out the live version of PromptCV hosted on Render: https://promptcv-ai.onrender.com/

## Key Features

-   **AI-Powered Content Parsing:** Utilizes the Gemini API to intelligently parse unstructured text and structure it into a professional CV format.
    
-   **Template Selection:** Offers a variety of modern and professional CV templates to choose from.
    
-   **User-Friendly Interface:** A simple, intuitive web interface that guides the user through the CV generation process.
    
-   **Instant Downloads:** Generated CVs are available for immediate download as `.docx` files.
    
-   **Powered by Django:** Built on a robust and scalable Django backend.
    

## How It Works

1.  **Select a Template:** The user is presented with a selection of CV templates.
    
2.  **Enter Your Details:** The user enters their professional information into a single text prompt. This can include their name, contact information, work experience, education, skills, and more.
    
3.  **Generate CV:** With a click of a button, the application sends the user's text prompt and the chosen template's instructions to the Gemini API.
    
4.  **AI Processing:** The Gemini API processes the text, extracts the relevant information, and structures it according to the template's requirements.
    
5.  **Download Your CV:** The application then populates a `.docx` template with the AI-generated content and makes it available for the user to download.
    

## Project Structure

```
PromptCV/
├── PromptCV2/            # Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                 # Django app for core functionality
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── Templates/            # HTML templates
│   ├── main_page.html
│   ├── template_selection.html
│   └── build_page.html
├── media/                # User-uploaded files (templates, thumbnails)
├── manage.py
└── requirements.txt

```

## Technical Details

-   **Backend:** Django
    
-   **AI Model:** Google Gemini API
    
-   **Frontend:** HTML, CSS, JavaScript
    
-   **Database:** SQLite (for development)
    
-   **Dependencies:** `django`, `requests`, `python-docx`, `docxtpl`
    

## Setup and Installation

1.  **Clone the repository:**
    
    ```
    git clone [https://github.com/r-bharathikannan-2006/PromptCV.git](https://github.com/r-bharathikannan-2006/PromptCV.git)
    
    ```
    
2.  **Create and activate a virtual environment:**
    
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    
    ```
    
3.  **Install the dependencies:**
    
    ```
    pip install -r requirements.txt
    
    ```
    
4.  **Set up your environment variables:**
    
    To use the Gemini API, you need an API key. Follow these steps to get one:
    
    -   Go to [Google AI Studio](https://aistudio.google.com/ "null").
        
    -   Sign in with your Google account.
        
    -   Click on the "**Get API key**" button in the top left corner.
        
    -   If you don't have a project yet, a pop-up will prompt you to create one. Follow the instructions.
        
    -   Once your project is set up, you will see a screen with your API keys. Click "**Create API key**".
        
    -   Copy the generated API key.
        
    
    Now, create a `.env` file in the root directory of the project and add your copied Gemini API key:
    
    ```
    GEMINI_KEY="YOUR_API_KEY"
    
    ```
    
5.  **Run the database migrations:**
    
    ```
    python manage.py migrate
    
    ```
    
6.  **Run the development server:**
    
    ```
    python manage.py runserver
    
    ```
    

The application will be available at `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
