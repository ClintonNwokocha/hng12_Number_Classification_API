from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import requests
import math

# Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# check if number is perfect
def is_perfect(n):
    divisor_sum = sum(i for i in range(1, abs(n)) if n% i == 0)
    return divisor_sum == abs(n)

# check if a number is armstrong
def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == abs(n)

# calculate the sum of digits
def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

# fetch the fun fact from Numbers API
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}?json")
        if response.status_code == 200:
            return response.json().get('text', 'Fun fact not available')
    except requests.exceptions.Timeout:
        return "Fun fact not available due to timeout"
    except requests.exceptions.RequestException as e:
        return "Fun fact not available due to an error"
    return 'Fun fact not available'

# view to classify the number
@csrf_exempt
def classify_number(request):
    number = request.GET.get('number')

    # if no number is provided, return number: null
    if not number:
        return JsonResponse({
            "number": "",
            "error": True,
            "is_prime": False,
            "is_perfect": False,
            "properties": [],
            "digit_sum": 0,
            "fun_fact": "Fun Fact not available"
            }, status=400)

    # check if the number is a valid integer (allow negative sign)
    if not number.lstrip('_').isdigit():
        return JsonResponse({
            "number": number,
            "error": True,
            "is_prime": False,
            "is_perfect": False,
            "properties": [],
            "digit_sum": 0,
            "fun_fact": "Fun fact not available"
            }, status=400)
    
    number = int(number)

    # Reject negative numbers with appropraite message
    if number < 0:
        properties = ["armstrong", "odd"] if is_armstrong(number) else ["odd"]
        return JsonResponse({
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": get_fun_fact(number)
            })


    # Check properties of the number
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
 
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # prepare response data
    data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
        }
    
    return JsonResponse(data, json_dumps_params={'indent':4})
