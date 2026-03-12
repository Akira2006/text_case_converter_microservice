# Text Case Converter Microservice

A Python microservice built with Flask that converts text into different case formats through an HTTP API. This project demonstrates microservice architecture principles by enabling programmatic text transformation across distributed systems.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Future Improvements](#future-improvements)

## Features

- **Multiple Case Conversions**: Convert text to uppercase, lowercase, or title case
- **HTTP API**: RESTful endpoint for seamless integration with other services
- **Microservice Architecture**: Lightweight and independent service for text transformation
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

### Using the Test Client

Open a new terminal and run:
```bash
python test_client.py
```

Example output:
```
Response:
{'result': 'HELLO WORLD'}
```

## API Documentation

### Endpoints

#### Convert Text to Uppercase
- **URL**: `/uppercase`
- **Method**: `POST`
- **Request Body**:
```json
{
  "text": "hello world"
}
```
- **Response**:
```json
{
  "result": "HELLO WORLD"
}
```

#### Convert Text to Lowercase
- **URL**: `/lowercase`
- **Method**: `POST`
- **Request Body**:
```json
{
  "text": "HELLO WORLD"
}
```
- **Response**:
```json
{
  "result": "hello world"
}
```

#### Convert Text to Title Case
- **URL**: `/titlecase`
- **Method**: `POST`
- **Request Body**:
```json
{
  "text": "hello world"
}
```
- **Response**:
```json
{
  "result": "Hello World"
}
```

### Example Usage with cURL

```bash
curl -X POST http://localhost:5002/uppercase \
  -H "Content-Type: application/json" \
  -d '{"text": "hello world"}'
```

### Example Usage with Python Requests

```python
import requests

response = requests.post(
    'http://localhost:5002/uppercase',
    json={'text': 'hello world'}
)
print(response.json())
```

## Project Structure

```
text_case_converter_microservice/
├── app.py                 # Flask microservice application
├── test_client.py         # Client program for testing the service
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

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

You should see successful responses with converted text.

## Future Improvements

- Add support for additional case formats (camelCase, snake_case)
- Implement input validation and error messages
- Add logging for debugging and monitoring
- Create unit tests for API endpoints
- Deploy to a cloud platform (AWS, Heroku, etc.)
- Add Docker support for containerization

## Learning Outcomes

This project demonstrates:
- Building microservices with Flask
- Creating REST APIs
- Client-server communication using HTTP
- Separation of concerns in software architecture
- Python best practices

## License

This project is open source and available for educational purposes.

## Author

**Akira2006**  
GitHub: [@Akira2006](https://github.com/Akira2006)

---

*Last Updated: 2026-03-12 10:59:14*