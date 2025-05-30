clientes = [1,1,0,1,1,1,1,0,1,1]

satisfeitos = sum(clientes)
total = len(clientes)
porcentagem = satisfeitos/total *100

print(f"{porcentagem:.1f}% dos clientes estão satisfeitos.")

if porcentagem > 80:
    print("conclusão indutiva: a maioria dos clientes estão satisfeitos")

else: 
    print("Conclusão indutiva: há indícios de insatisfação")