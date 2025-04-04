vendas2022 = float(input("📅 Digite a quantidade de vendas em 2022: "))
vendas2023 = float(input("📅 Digite a quantidade de vendas em 2023: "))

variacao = (vendas2023 - vendas2022) / vendas2022 * 100

print(f"\n📊 Variação: {variacao:.2f}%")

if variacao > 20:
    print("💰 Bonificação para o time de vendas!")
elif 2 < variacao <= 20:
    print("🎉 Pequena bonificação para time de vendas.")
elif -10 <= variacao <= 2:
    print("🧠 Hora de pensar em políticas de incentivo às vendas.")
else:
    print("✂️ Corte de gastos... é hora de reavaliar!")
