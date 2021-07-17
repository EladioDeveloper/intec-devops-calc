Feature: Restar dos numeros

    Scenario Outline: Restar
        Given que yo deseo restar dos numeros
        When yo ingrese los numeros <num1> y <num2>
        Then el resultado  <result> debe ser la diferencia de ambos
        
        Examples: Restar de Numeros
        | num1 | num2 | result  |
        | 2    | 2    | 0       |
        | 5    | 3    | 2       |
        | 1000 | 500  | 500     |
        | 0    | 0    | 0       |
        | 1    | -2   | Invalid |