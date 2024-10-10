# Flask App README

## Overview

This is a simple Flask application that allows users to submit their name through a form. The app then displays the submitted name back to the user.

## Prerequisites

- Python 3.x
- Flask library

## Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Flask**:
   ```bash
   pip install Flask
   ```

## File Structure

Make sure your project directory contains the following files:

```
/your-project-directory
│
├── app.py             # Main Flask application
├── templates
│   └── index.html     # HTML template for user input
```

## Running the Application

1. **Start the Flask server**:
   Navigate to your project directory and run:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open a web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. You'll see a form asking for your name.
2. Enter your name in the text box and click "Ok."
3. The page will refresh and display your name. If no valid name is provided, it will display "invalid."

## Customization

- You can modify the HTML in `index.html` to change the appearance or functionality of the form.
- The Flask app logic in `app.py` can be modified to include additional routes or features as needed.

## Notes

- The app runs in debug mode for development purposes. For production use, make sure to configure the server appropriately.
- Ensure that the Flask version is compatible with your Python version.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Troubleshooting

If you encounter any issues, please ensure that:
- Flask is correctly installed.
- You are in the correct directory when running the app.
- The server is running and accessible via the specified URL.
