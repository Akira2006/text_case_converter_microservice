# Text Case Converter Microservice

A Python microservice built with Flask that converts text into different case formats through an HTTP API. This project demonstrates microservice architecture principles by enabling programmatic text transformation across distributed systems through HTTP requests and responses.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Architecture](#architecture)

## Features

- **Text Case Conversion**: Convert text to uppercase, lowercase, or title case via HTTP API
- **Microservice Architecture**: Independent service communicating through HTTP requests and responses
- **Single Endpoint Design**: Unified `/convert` endpoint with flexible case parameter
- **Test Client**: Included demo client showing how to integrate with the microservice
- **Error Handling**: Graceful handling of invalid requests

## Tech Stack

- **Language**: Python 3.x
- **Framework**: Flask
- **HTTP Client**: Requests
- **Architecture**: Microservice (HTTP API)

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Akira2006/text_case_converter_microservice
cd text_case_converter_microservice
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install Flask requests
```

## Usage

### Starting the Microservice

Run the Flask server:
```bash
python app.py
```

The server will start on:
```
http://localhost:5002
```

You should see output indicating the Flask server is running on `http://localhost:5002`.

### Using the Test Client

Open a new terminal and run:
```bash
python test_client.py
```

The test client will send a POST request to the microservice and display the converted result. Example output:
```
Response:
{'result': 'HELLO WORLD'}
```

## API Documentation

### Endpoint

#### Convert Text Case
- **URL**: `/convert`
- **Method**: `POST`
- **Port**: `5002`

### Request Body

```json
{
  "text": "hello world",
  "case": "upper"
}
```

**Parameters:**
- `text` (string, required): The text to be converted
- `case` (string, required): The target case format. Valid values are:
  - "upper" - Convert to UPPERCASE
  - "lower" - Convert to lowercase
  - "title" - Convert to Title Case

### Response Format

```json
{
  "result": "CONVERTED TEXT"
}
```

### Example Requests

#### Convert to Uppercase

Using cURL:
```bash
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "hello world", "case": "upper"}'
```

Using Python Requests:
```python
import requests

response = requests.post(
    'http://localhost:5002/convert',
    json={'text': 'hello world', 'case': 'upper'}
)
print(response.json())
# Output: {'result': 'HELLO WORLD'}
```

#### Convert to Lowercase

Using cURL:
```bash
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "HELLO WORLD", "case": "lower"}'
```

#### Convert to Title Case

Using cURL:
```bash
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "hello world", "case": "title"}'
```

## Project Structure

```
text_case_converter_microservice/
├── app.py                 # Flask microservice application
├── test_client.py         # Test client for the microservice
├── requirements.txt       # Python dependencies (Flask, requests)
└── README.md             # Project documentation
```

### File Descriptions

- **app.py**: Contains the Flask server that runs on port 5002 and exposes the `/convert` endpoint
- **test_client.py**: Demonstrates how to communicate with the microservice by sending HTTP POST requests to the `/convert` endpoint using the requests library
- **requirements.txt**: Lists all Python dependencies needed to run the microservice and test client

## Testing

To verify the microservice is working correctly:

1. Start the server in one terminal:
```bash
python app.py
```

2. Run the test client in another terminal:
```bash
python test_client.py
```

You should see a successful response with the converted text.

### Manual Testing

You can also test the API manually using cURL or any HTTP client:

```bash
# Test uppercase conversion
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "test", "case": "upper"}'

# Test lowercase conversion
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "TEST", "case": "lower"}'

# Test title case conversion
curl -X POST http://localhost:5002/convert \
  -H "Content-Type: application/json" \
  -d '{"text": "hello world", "case": "title"}'
```

## Architecture

This microservice demonstrates a **client-server architecture** where:

1. **Server (app.py)**: A Flask application that runs on `http://localhost:5002` and provides the `/convert` endpoint
2. **Client (test_client.py)**: A Python script that communicates with the server using HTTP POST requests

### Communication Flow

```
test_client.py
    ↓
HTTP POST Request to /convert endpoint
    ↓
app.py (Flask Server on port 5002)
    ↓
Process request & convert text
    ↓
HTTP Response with JSON result
    ↓
test_client.py receives and displays result
```

The client and server communicate entirely through HTTP requests and responses, not through direct function calls. This separation demonstrates true microservice architecture principles.

## Learning Outcomes

This project demonstrates:
- Building microservices with Flask
- Creating REST APIs
- Client-server communication using HTTP requests and responses
- Separation of concerns in software architecture
- JSON request/response handling
- Microservice architectural patterns
- Python best practices

## Future Improvements

- Add support for additional case formats (camelCase, snake_case, kebab-case)
- Implement comprehensive input validation and error messages
- Add logging for debugging and monitoring
- Create unit tests for API endpoints
- Deploy to a cloud platform (AWS, Heroku, etc.)
- Add Docker support for containerization
- Implement request rate limiting
- Add API documentation with Swagger/OpenAPI

## License

This project is open source and available for educational purposes.

## Author

**Akira2006**  
GitHub: [@Akira2006](https://github.com/Akira2006)

---

*Last Updated: 2026-03-12*