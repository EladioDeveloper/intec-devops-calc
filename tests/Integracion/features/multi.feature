Feature: Multiplicar dos numeros

    Scenario Outline: Multiplicar
        Given deseo multiplicar dos numeros
        When yo ingrese los numeros  <num1> y <num2>
        Then el resultado <result> debe ser la multiplicacion de ambos
        
        Examples: multiplicar de Numeros
        | num1 | num2 | result  |
        | 2    | 2    | 4       |
        | 1    | 12   | 12      |
        | 100  | 1000 | 100000  |
        | 0    | 0    | 0       |
        | 1    | -1   | Invalid |