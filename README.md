# HNG12_Stage_0
A public API that returns the following information in JSON format:
- Email address (used to register on the HNG12 Slack workspace).
- The current datetime as an ISO 8601 formatted timestamp.
- The GitHub URL of the project's codebase.


## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/casey216/HNG12_Stage_0.git
   cd HNG12_Stage_0
   ```

2. **Create and Activate Virtual Environment**

   ```sh
   python -m venv venv
   # Activate virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```sh
   python app.py
   ```

   The server should start at `http://127.0.0.1:5000/`

### API Documentation

#### GET /

Retrieves an example message.

**Request:**

```sh
curl -X GET "http://127.0.0.1:5000/"
```

**Example Successful Response:**

```json
{
  "message": "Hello, John!"
}
```
**Response Codes:**

- `200 OK` – Successful response
- `404 Not Found` – Resource not found
- `500 Internal Server Error` – Server encountered an issue

### Hire a Developer

Click [Here] to hire a python developer(https://hng.tech/hire/python-developers)

### License

This project is licensed under the [MIT License](LICENSE).

