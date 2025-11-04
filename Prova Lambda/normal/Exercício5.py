import time

def valorPagamento(valor, atraso):
    """Calcula o valor a ser pago considerando multa e juros por atraso."""
    if atraso > 0:
        multa = valor * 0.03
        juros = valor * 0.001 * atraso
        return valor + multa + juros
    else:
        return valor
    
total_pago = 0

while True:
    try:
        valor = float(input("\nDigite o valor da prestação (ou 0 para sair): "))
        if valor == 0:
            print(f"\nTotal pago em todas as prestações: R$ {total_pago:.2f}")
            print("Saindo...")
            time.sleep(1)
            break
        atraso = int(input("Digite o número de dias em atraso: "))
        valor_final = valorPagamento(valor, atraso)
        total_pago += valor_final
        print(f"Valor a ser pago: R$ {valor_final:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")