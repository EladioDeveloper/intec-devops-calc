Feature: Dividir dos numeros

    Scenario Outline: Dividir
        Given que yo deseo dividir dos numeros
        When yo ingrese los numeros  <num1> y <num2>
        Then el resultado <result> debe ser la division de ambos
        
        Examples: dividir de Numeros
        | num1 | num2 | result  |
        | 2    | 2    | 1.0     |
        | 12   | 1    | 12.0    |
        | 1000 | 100  | 10.0    |
        | 0    | 0    | 0.0     |   
        | 2    | -2   | Invalid |
