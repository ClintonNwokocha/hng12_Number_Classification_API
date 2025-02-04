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
    divisor_sum = sum(i for i in range(1, n) if n% i == 0)
    return divisor_sum == n

# check if a number is armstrong
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == n

# calculate the sum of digits
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# fetch the fun fact from Numbers API
def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}?json")
    if response.status_code == 200:
        return response.json().get('text', 'No fun fact available')
    return 'No fun fact available'

@csrf_exempt
def classify_number(request):
    number = request.GET.get('number')

    # check if the number is an integer
    if not number or not number.isdigit():
        return JsonResponse({
            "number": number,
            "error": True
            }, status=400)
    
    number = int(number)

    # Check properties of the number
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")

    if is_prime(number):
        properties.append("prime")
    
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
