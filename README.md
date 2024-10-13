# Code Summarization Web App
A Python-based web application that summarizes Python code snippets using **machine learning models**. The web interface allows users to input Python code and receive a concise summary of its functionality. The project is built using **Flask** for the backend, with HTML/CSS for the frontend.

## Features
- **Code Summarization**: Users can input Python code, and the app will generate a brief summary of the code.
- **Simple and Interactive UI**: A user-friendly web interface to input code and display the generated summaries.
- **Real-time Summarization**: The application provides code summaries dynamically as users interact with the interface.

## Folder Structure
```
.
├── static/
│   └── styles.css       # CSS for styling the web interface
├── templates/
│   └── index.html       # Front-end HTML file for user interaction
├── app.py               # Main Flask application
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## Installation

### Prerequisites
- **Python 3.x**
- **Flask**

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anushkasrivastava1303/2AIcodeSummarizer.git
   cd 2AIcodeSummarizer
   ```

2. **Install Dependencies**:
   Make sure you have the required Python libraries by installing them using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Once all dependencies are installed, run the Flask app:
   ```bash
   python app.py
   ```

4. **Open the App in Your Browser**:
   After starting the server, open a browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Enter a Python code snippet in the provided text box.
2. Click on the **"Summarize"** button.
3. The app will display a summary of the code below the input box.

### Example

```python
def add(a, b):
    return a + b
```

**Summary**: This function adds two numbers `a` and `b` and returns the result.

## File Descriptions

- **app.py**: The main Flask backend that handles routing and code summarization logic.
- **index.html**: The frontend of the application, allowing users to input Python code and view the summaries.
- **styles.css**: Contains the styling for the web page, making the app more visually appealing.

## Technologies Used

- **Flask**: A lightweight web framework used for building the backend of the application.
- **HTML/CSS**: Frontend technologies used to build the user interface.
- **JavaScript (Fetch API)**: Handles real-time code submission to the backend and dynamically updates the results on the frontend.
- **Python**: For server-side logic and machine learning model integration.

## Future Enhancements

- **Advanced Summarization Models**: Integrate more sophisticated models like **BERT** or **GPT** for improved summarization accuracy.
- **Support for Other Languages**: Extend support to summarize code written in other programming languages like Java, C++, etc.
- **User Authentication**: Add a login system so users can save their summaries for later use.
- **Mobile Responsiveness**: Optimize the UI for better experience on mobile devices.
