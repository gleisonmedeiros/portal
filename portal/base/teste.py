valor_emprestimo = 18000
restante_pagar = valor_emprestimo
juros = 5
debito_mensal = 0
mes = 1
juros_do_mes = 0
valor_debitado = 0
total_juros = 0


while restante_pagar > 0 :
    print(f'mes: {mes} - Restante: {restante_pagar:.2f} | Pago: {debito_mensal:.2f} | Abatido: {valor_debitado:.2f}| Juros: {juros_do_mes:.2f} ')
    debito_mensal = 1500
    juros_do_mes = restante_pagar/100*juros
    valor_debitado = debito_mensal - juros_do_mes
    restante_pagar = restante_pagar - valor_debitado
    mes = mes + 1
    if (restante_pagar < debito_mensal):
        juros_do_mes = restante_pagar/100*juros
        debito_mensal = restante_pagar + juros_do_mes
    total_juros = total_juros + juros_do_mes

print(f'\n\nJuros total: {total_juros:.2f}')










