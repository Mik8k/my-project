import requests
import time
from datetime import datetime

# ==========================================
# SISTEMA DE PREVISÃO DO TEMPO
# ==========================================

print("=" * 50)
print("        🌦️ PREVISÃO DO TEMPO 🌦️")
print("=" * 50)

time.sleep(1)

# Dicionário com algumas cidades
cidades = {
    "volta redonda": (-22.5231, -44.1042),
    "rio de janeiro": (-22.9068, -43.1729),
    "sao paulo": (-23.5505, -46.6333),
    "belo horizonte": (-19.9167, -43.9345),
    "brasilia": (-15.7939, -47.8828),
    "curitiba": (-25.4284, -49.2733),
    "salvador": (-12.9777, -38.5016),
    "recife": (-8.0476, -34.8770),
    "fortaleza": (-3.7319, -38.5267)
}

cidade = input("Digite o nome da cidade: ").lower().strip()

# Verifica se a cidade está cadastrada
if cidade not in cidades:
    print("\n❌ Cidade não encontrada!")
    time.sleep(0.5)

    print("Cidades disponíveis:")
    time.sleep(0.5)

    for nome in cidades:
        print("-", nome.title())
        time.sleep(0.2)

else:
    latitude, longitude = cidades[cidade]

    print("\n🔎 Buscando informações...")
    time.sleep(1)

    print("Cidade:", cidade.title())
    time.sleep(0.4)

    print("Latitude:", latitude)
    time.sleep(0.4)

    print("Longitude:", longitude)
    time.sleep(0.7)

    # URL da API
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=" + str(latitude) +
        "&longitude=" + str(longitude) +
        "&current=temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "wind_speed_10m,"
        "weather_code"
        "&daily=temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_probability_max,"
        "weather_code"
        "&timezone=auto"
    )

    try:
        print("\n🌐 Conectando ao servidor...")
        time.sleep(1)

        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 200:

            print("✅ Dados recebidos com sucesso!")
            time.sleep(0.8)

            dados = resposta.json()

            # -------------------------------
            # TEMPO ATUAL
            # -------------------------------

            atual = dados["current"]

            temperatura = atual["temperature_2m"]
            sensacao = atual["apparent_temperature"]
            umidade = atual["relative_humidity_2m"]
            vento = atual["wind_speed_10m"]
            codigo = atual["weather_code"]

            print("\n" + "=" * 50)
            print("🌡️ TEMPO AGORA")
            print("=" * 50)

            time.sleep(0.7)

            print("Temperatura:", temperatura, "°C")
            time.sleep(0.4)


            print("Velocidade do vento:", vento, "km/h")
            time.sleep(0.6)

            # -------------------------------
            # DESCRIÇÃO DO TEMPO
            # -------------------------------

            descricoes = {
                0: "☀️ Céu limpo",
                1: "🌤️ Principalmente limpo",
                2: "⛅ Parcialmente nublado",
                3: "☁️ Nublado",
                45: "🌫️ Neblina",
                48: "🌫️ Neblina com geada",
                51: "🌦️ Garoa fraca",
                53: "🌦️ Garoa moderada",
                55: "🌧️ Garoa forte",
                61: "🌧️ Chuva fraca",
                63: "🌧️ Chuva moderada",
                65: "🌧️ Chuva forte",
                71: "❄️ Neve fraca",
                73: "❄️ Neve moderada",
                75: "❄️ Neve forte",
                80: "🌦️ Pancadas de chuva",
                81: "🌧️ Pancadas moderadas",
                82: "⛈️ Pancadas fortes",
                95: "⛈️ Tempestade",
                96: "⛈️ Tempestade com granizo",
                99: "⛈️ Tempestade forte com granizo"
            }

            descricao = descricoes.get(
                codigo,
                "🌥️ Condição desconhecida"
            )

            print("Condição:", descricao)
            time.sleep(1)

            # -------------------------------
            # PREVISÃO DOS PRÓXIMOS 3 DIAS
            # -------------------------------

            diario = dados["daily"]

            datas = diario["time"]
            temperaturas_max = diario["temperature_2m_max"]
            temperaturas_min = diario["temperature_2m_min"]
            chuvas = diario["precipitation_probability_max"]
            codigos = diario["weather_code"]

            print("\n" + "=" * 50)
            print("📅 PREVISÃO DOS PRÓXIMOS 3 DIAS")
            print("=" * 50)

            time.sleep(1)

            # Mostra somente os 3 primeiros dias
            for i in range(3):

                data = datetime.strptime(
                    datas[i],
                    "%Y-%m-%d"
                )

                data_formatada = data.strftime("%d/%m/%Y")

                condicao = descricoes.get(
                    codigos[i],
                    "🌥️ Condição desconhecida"
                )

                print("\n📆", data_formatada)
                time.sleep(0.4)

                print("Condição:", condicao)
                time.sleep(0.4)

                print(
                    "🌡️ Máxima:",
                    temperaturas_max[i],
                    "°C"
                )
                time.sleep(0.4)

                print(
                    "🥶 Mínima:",
                    temperaturas_min[i],
                    "°C"
                )
                time.sleep(0.4)

                print(
                    "🌧️ Chance de chuva:",
                    chuvas[i],
                    "%"
                )

                time.sleep(0.8)

            # -------------------------------
            # AVISOS
            # -------------------------------

            print("\n" + "=" * 50)
            print("⚠️ AVISOS")
            print("=" * 50)

            time.sleep(0.8)

            if temperatura >= 35:
                print("🔥 Cuidado! Temperatura muito alta.")

            elif temperatura >= 30:
                print("☀️ Está bastante quente hoje.")

            elif temperatura <= 10:
                print("🥶 Está muito frio hoje.")

            else:
                print("👍 Temperatura dentro de uma faixa agradável.")

            time.sleep(0.7)

            if umidade >= 80:
                print("💧 Umidade do ar está alta.")

            elif umidade <= 30:
                print("🏜️ Umidade do ar está baixa.")

            time.sleep(0.7)

            if vento >= 40:
                print("💨 Atenção: ventos fortes!")

            time.sleep(0.8)

            # -------------------------------
            # FINAL
            # -------------------------------

            print("\n" + "=" * 50)
            time.sleep(0.5)

            print("✅ Consulta finalizada!")
            time.sleep(0.7)

            print("Obrigado por usar o sistema! 🌦️")
            time.sleep(0.7)

            print("=" * 50)

        else:
            print("\n❌ Não foi possível acessar a previsão.")
            time.sleep(0.5)

            print("Código de erro:", resposta.status_code)

    except requests.exceptions.Timeout:
        print("\n⏱️ A conexão demorou muito.")
        time.sleep(0.5)

        print("Verifique sua internet e tente novamente.")

    except requests.exceptions.ConnectionError:
        print("\n📡 Não foi possível conectar à internet.")
        time.sleep(0.5)

    except Exception as erro:
        print("\n❌ Ocorreu um erro:")
        time.sleep(0.5)

        print(erro)