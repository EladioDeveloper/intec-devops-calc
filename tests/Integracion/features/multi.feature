Feature: Multiplicar dos numeros

    Scenario Outline: Multiplicar
        Given deseo multiplicar dos numeros
        When yo ingrese los numeros  <num1> y <num2>
        Then el resultado <result> debe ser la multiplicacion de ambos
        
        Examples: multiplicar de Numeros
        | num1 | num2 | result  |
        | 2    | 1    | 2       |
        | 8    | 8    | 64      |
        | 3    | 100  | 300     |
        | 0    | 0    | 0       |
        | 1    | -2   | Invalid |