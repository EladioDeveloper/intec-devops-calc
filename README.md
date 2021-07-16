# Calculadora API

## Funcionalidades

    * Suma de 2 numeros.
    * Resta de 2 numeros.
    * Multiplicacion de 3 numeros.
    * Division de 2 numeros.

## Requirements

    * Docker
    * Python 3

## Tests

Run unittests + Coverage

```
    coverage run my-unittest.py
    coverage report -m --fail-under=89 #falla sino llegamos al 80%
```

## Run Integration Tests

```
behave tests/Integracion/
```
