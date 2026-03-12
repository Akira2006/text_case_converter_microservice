
# Text Case Converter Microservice

## Overview
This microservice converts text into different case formats such as uppercase, lowercase, and title case. It is built using Python and Flask and exposes an HTTP API that other programs can use to convert text automatically.

The project demonstrates basic microservice architecture where a client program sends requests to a server and receives responses through HTTP instead of calling functions directly.

The repository also includes a small client program that demonstrates how another program can interact with the microservice.

---

## Features

- Convert text to **uppercase**
- Convert text to **lowercase**
- Convert text to **title case**
- Simple **HTTP API endpoint**
- Demonstrates **microservice communication using HTTP requests and responses**
- Includes a **test client program**

---

## Tech Stack

- Python 3
- Flask
- Requests

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Akira2006/text_case_converter_microservice
cd text_case_converter_microservice
````

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install Flask requests
```

---

## Running the Microservice

Start the Flask server:

```bash
python app.py
```

The server will start on:

```
http://localhost:5002
```

---

## Running the Test Client

Open another terminal and run:

```bash
python test_client.py
```

Example output:

```
Response:
{'result': 'HELLO WORLD'}
```

---

## API Documentation

### Endpoint

```
POST /convert
```

### Request Body

```json
{
  "text": "hello world",
  "case": "upper"
}
```

Supported values for **case**:

* upper
* lower
* title

---

### Response Example

```json
{
  "result": "HELLO WORLD"
}
```

---

## Example Request (cURL)

```bash
curl -X POST http://localhost:5002/convert \
-H "Content-Type: application/json" \
-d '{"text": "hello world", "case": "upper"}'
```

---

## Project Structure

```
text_case_converter_microservice
│
├── app.py
├── test_client.py
├── requirements.txt
└── README.md
```

* **app.py** – Flask server that runs the microservice and processes requests
* **test_client.py** – example client that sends HTTP requests to the service
* **requirements.txt** – Python dependencies required for the project

---

## Workflow

1. The client sends an HTTP POST request to `/convert`.
2. The request contains the text and the desired case format.
3. The Flask microservice processes the request.
4. The converted text is returned as a JSON response.
5. The client receives the response and prints the result.

This demonstrates how microservices communicate through HTTP requests and responses instead of direct function calls.

---

## Author

Akira2006
[https://github.com/Akira2006](https://github.com/Akira2006)
