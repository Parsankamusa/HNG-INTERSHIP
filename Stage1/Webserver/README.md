# IP Location and Temperature API

This is a simple Flask API that returns a greeting message with the visitor's IP address, location, and the current temperature in that location.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
   ```git clone https://github.com/Parsankamusa/HNG-INTERSHIP.git```

3. Navigate to the project directory: 
 ```cd HNG-INTERSHIP/Stage1/Webserver```
4. Install the required dependencies:
pip install -r requirements.txt

### Running the API

To run the API, execute the following command: python app.py


The API will be accessible at `http://localhost:5000/api/hello`.

## Usage

The API provides a single endpoint `/api/hello` that accepts an optional `visitor_name` query parameter.

### Example Request

GET /api/hello?visitor_name=John


### Example Response

```json
{
    "client_ip": "127.0.0.1",
    "location": "Nairobi",
    "greeting": "Hello, John!, the temperature is 20 degrees Celsius in Nairobi"
}
```
If no visitor_name is provided, the API will use the default "Visitor" in the greeting message.

### Implementation Details
The get_location_and_temperature function is a mock implementation that returns hardcoded data for demonstration purposes. In a real-world application, this function would make calls to a geolocation and weather API to retrieve the actual location and temperature data based on the visitor's IP address.

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License.

This README provides an overview of the project, instructions for getting started, usage examples, implementation details, and information about contributing and licensing.


