import ttkbootstrap as tb

def calcular_valores():
    try:
        valor_fixo = float(entry_fixo.get())
        valor_variavel = float(entry_variavel.get())
        recursos_hidr_agua = float(entry_recursos_agua.get())
        recursos_hidr_esg = float(entry_recursos_esg.get())
        
        total_conta_agua = valor_fixo + valor_variavel + recursos_hidr_agua + recursos_hidr_esg
        valor_fixo_por_apartamento = valor_fixo / 8  # Número fixo de apartamentos
        numero_residentes = sum(distribuicao_residentes.values())
        valor_variavel_por_residente = valor_variavel / numero_residentes if numero_residentes > 0 else 0
        
        listbox_resultados.delete("1.0", "end")
        total_pago = 0

        for apt, res in distribuicao_residentes.items():
            valor_total_apartamento = valor_fixo_por_apartamento + (valor_variavel_por_residente * res)
            total_pago += valor_total_apartamento
            listbox_resultados.insert("end", f"{apt}: R$ {valor_total_apartamento:.2f}\n")
        
        listbox_resultados.insert("end", f"Total arrecadado: R$ {total_pago:.2f}\n")
    except ValueError:
        tb.dialogs.Messagebox.show_error("Erro", "Por favor, insira valores numéricos válidos.")

def atualizar_residentes():
    apt = entry_apartamento.get()
    res = entry_residentes.get()
    if apt and res.isdigit():
        distribuicao_residentes[apt] = int(res)
        tb.dialogs.Messagebox.show_info("Atualizado", f"Apartamento {apt} agora tem {res} moradores.")
    else:
        tb.dialogs.Messagebox.show_error("Erro", "Digite um número válido de moradores.")

distribuicao_residentes = {
    "Apto 01": 3,
    "Apto 02": 3,
    "Apto 101": 2,
    "Apto 102": 2,
    "Apto 201": 3,
    "Apto 202": 2,
    "Apto 301": 1,
    "Apto 302": 2,
}

root = tb.Window(themename="superhero")
root.title("Cálculo de Conta de Água")
root.geometry("750x450")

frame_inputs = tb.Frame(root)
frame_inputs.pack(pady=10)

tb.Label(frame_inputs, text="Abastecimento Água:").grid(row=0, column=0, padx=5)
entry_variavel = tb.Entry(frame_inputs)
entry_variavel.grid(row=0, column=1, padx=5)

tb.Label(frame_inputs, text="Esgoto Dinâmico:").grid(row=0, column=2, padx=5)
entry_fixo = tb.Entry(frame_inputs)
entry_fixo.grid(row=0, column=3, padx=5)

tb.Label(frame_inputs, text="Recursos Hídricos Água:").grid(row=1, column=0, padx=5)
entry_recursos_agua = tb.Entry(frame_inputs)
entry_recursos_agua.grid(row=1, column=1, padx=5)

tb.Label(frame_inputs, text="Recursos Hídricos Esgoto:").grid(row=1, column=2, padx=5)
entry_recursos_esg = tb.Entry(frame_inputs)
entry_recursos_esg.grid(row=1, column=3, padx=5)

tb.Button(root, text="Calcular", bootstyle="success", command=calcular_valores).pack(pady=5)

tb.Label(root, text="Distribuição por Apartamento").pack()
listbox_resultados = tb.ScrolledText(root, height=10)
listbox_resultados.pack()

frame_update = tb.Frame(root)
frame_update.pack(pady=10)

tb.Label(frame_update, text="Apto:").grid(row=0, column=0, padx=5)
entry_apartamento = tb.Entry(frame_update, width=10)
entry_apartamento.grid(row=0, column=1, padx=5)

tb.Label(frame_update, text="Residentes:").grid(row=0, column=2, padx=5)
entry_residentes = tb.Entry(frame_update, width=10)
entry_residentes.grid(row=0, column=3, padx=5)

tb.Button(frame_update, text="Atualizar", bootstyle="info", command=atualizar_residentes).grid(row=0, column=4, padx=5)

root.mainloop()
