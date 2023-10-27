mensagem = "Olá querida pessoa, vamos calcular o seu IMC. Será que posso tentar fazer o cálculo do seu IMC :) ?"
print(mensagem)
resposta = input("Digite 'Sim' ou 'Não': ")

if resposta.lower() == "sim":
    print("Você escolheu 'Sim', vamos calcular o seu IMC.")
    altura = input('Digite sua altura em metros: ')

    try:
        altura = float(altura)
    except ValueError:
        print("Por favor, insira um valor numérico válido para altura.")
        exit(1)

    peso = input('Digite seu peso em quilogramas: ')
    while True:
        try:
            peso = float(peso)
            if peso <= 0:
                print("Por favor, insira um peso positivo.")
                peso = input('Digite seu peso em quilogramas novamente: ')
            else:
                break
        except ValueError:
            print("Por favor, insira um valor numérico válido para peso.")
            peso = input('Digite seu peso em quilogramas novamente: ')

    def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        return imc

    imc = calcular_imc(peso, altura)

    def classificar_imc(imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade Grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade Grau 2"

    print(
        f"Seu IMC é {imc:.2f}, o que é classificado como '{classificar_imc(imc)}'.")

elif resposta.lower() == "não":
    print("Você escolheu 'Não', obrigado por usar nosso aplicativo.")
