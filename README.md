# **Number Classification API**

A simple **Django-based API** that classifies numbers by heir mathematiical properties and provides a fun fact about the number.

## **Description**
This API accepts a number as a query parameter and returns the following information:
- **is_prime**: Whether the number is prime.
- **is_perfect**: Whether the number is a perfect number.
- **properties**: Mathematical properties such as Armstrong, odd, or even.
- **digit_sum**: Sum of the digits of the number.
- **fun_fact**: A fun fact about the number, fetched from the Numbers API.

# **API Endpoint**

### Endpoint:
`GET /api/classify-number?number=<number>`

- **URL**: `https://<your-deployed-app-url>/api/classify-number?number=<number>
- **Method**: `GET`
- **Query Parameter**: `number` (Required, must be an integer)

### Example of a Sucessful REsponse (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an armstong number becayse 3^3 + 7^3 + 1^3 = 37"
}

### Example of an Error REsponse (400 Bad Request):
```json
{
    "number": "alphabet",
    "error": true
}

### Backlinks
- [HNG Hire Python Developers](https://hng.tech/hire/python-developers)

### **Deployment**
The API is deployed to Render. The following steps can be followed to deploy the API:
1. Push the project to GitHub.
2. Connect the GitHub repository to Render.


### **Technologies USed**
- **Django**: Framework for building API.
- **Requests**: For making external HTTP requests to the Numbers API.
- **CORS**: To handle Cross-Origin Resourcse SHaring (CORS).
- **Python 3.x: Programming language used for development.

