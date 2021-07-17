Feature: Restar dos numeros

    Scenario Outline: Restar
        Given que yo deseo restar dos numeros
        When yo inserte los numeros <num1> y <num2> para restar
        Then el resultado <result> debe ser la diferencia de ambos
        
        Examples: Restar de Numeros
        | num1 | num2 | result  |
        | 2    | 2    | 0       |
        | 12   | 1    | 11      |
        | 1000 | 100  | 900     |
        | 0    | 0    | 0       |
        | 1    | -1   | Invalid |