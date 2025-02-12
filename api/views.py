import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
import math

# function to check if a number is prime or not
def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# function to check if a number is perfect or not
def is_perfect(n):
    n = abs(n)
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# function to calculate the sum of digits of a number
def digit_sum(n):
    n = abs(n)
    return sum([int(i) for i in str(n)])

# function to check if a number is Armstrong
def is_armstrong(n):
    n = abs(n)
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum(d**power for d in digits)

# Function to determine number properties
def check_number_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

# API view to classify the number
@api_view(['GET'])
def classify_number(request):
    # Validate that 'number' exists in query params
    number_param = request.query_params.get('number', None)

    # if no number is provided, return and error repsonse
    if not number_param:
        return JsonResponse({
            "number": "",
            "error": True
            }, status=400)

    # Check if the number is a valid integer
    try:
        number = int(number_param)
    except ValueError:
        return JsonResponse({
            "number": number_param,
            "error": True
            }, status=400)

    # Calculate numbr properties
    is_prime_result = is_prime(number)
    is_perfect_result = is_perfect(number)
    properties = check_number_properties(number)
    digit_sum_result = digit_sum(number)

    # Fetch fun fact about the number

    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{number}/math", timeout=5)
        if fun_fact_response.status_code == 200:
            fun_fact = fun_fact_response.text
        else:
            fun_fact = "Fun fact not available"
    except requess.exceptions.RequestException as e:
        fun_fact = f"Fun fact not available due to error: {str(e)}"

    # Prepare the response
    response = {
            "number": number,
            "is_prime": is_prime_result,
            "is_perfect": is_perfect_result,
            "properties": properties,
            "digit_sum": digit_sum_result,
            "fun_fact": fun_fact
            }
    return JsonResponse(response, status=200)
