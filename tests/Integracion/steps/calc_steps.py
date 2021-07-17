from behave import *
from fastapi import testclient
import api
from fastapi.testclient import TestClient

@given("que deseo sumar dos numeros")
def step_implementation(context):
    context.app =  TestClient(api.app)
    
@when('yo ingrese los numeros {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/sumar?num1={num1}&num2={num2}')
    print(context.api_response.status_code)
    assert 200 == context.api_response.status_code

@then('El resultado {result} debe ser la suma de ambos')
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))


@given("que yo deseo restar dos numeros")
def step_implementation(context):
    context.app =  TestClient(api.app)
    
@when('yo inserte los numeros {num1} y {num2} para restar')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/restar?num1={num1}&num2={num2}')
    print(context.api_response.status_code)
    assert 200 == context.api_response.status_code

@then('El resultado {result} debe ser la diferencia de ambos')
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))


@given("deseo multiplicar dos numeros")
def step_implementation(context):
    context.app =  TestClient(api.app)
    
@when('yo provea los numeros {num1} y {num2} para multiplicar')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/multiplicar?num1={num1}&num2={num2}')
    print(context.api_response.status_code)
    assert 200 == context.api_response.status_code

@then('El resultado {result} debe ser la multiplicacion de ambos')
def step_implementation(context, result):
    assert str(result) == str(context.api_response.json().get('total'))
