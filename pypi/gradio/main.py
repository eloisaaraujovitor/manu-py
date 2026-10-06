import gradio as gr

def analisar_texto(texto, operacao, caixa_alta):
    """
    Função principal que processa o texto com base nas opções escolhidas.
    """
    if not texto.strip():
        return "Por favor, digite algum texto para analisar.", 0, 0

    # Contagem de palavras e caracteres
    num_palavras = len(texto.split())
    num_caracteres = len(texto)

    # Aplicação do efeito de caixa alta se selecionado
    if caixa_alta:
        texto = texto.upper()

    # Processamento da operação selecionada
    if operacao == "Inverter Texto":
        resultado = texto[::-1]
    elif operacao == "Contar Palavras":
        resultado = f"O texto possui {num_palavras} palavra(s) e {num_caracteres} caractere(s)."
    elif operacao == "Substituir Espaços por Traços":
        resultado = texto.replace(" ", "-")
    else:
        resultado = texto

    return resultado, num_palavras, num_caracteres

# Criando a interface com Gradio
interface = gr.Interface(
    fn=analisar_texto,
    inputs=[
        gr.Textbox(lines=4, placeholder="Digite ou cole seu texto aqui...", label="Texto de Entrada"),
        gr.Dropdown(
            choices=["Nenhuma", "Inverter Texto", "Contar Palavras", "Substituir Espaços por Traços"],
            value="Nenhuma",
            label="Escolha uma Operação"
        ),
        gr.Checkbox(label="Transformar em MAIÚSCULAS")
    ],
    outputs=[
        gr.Textbox(label="Resultado"),
        gr.Number(label="Total de Palavras"),
        gr.Number(label="Total de Caracteres")
    ],
    title="⚡ Processador e Analisador de Texto",
    description="Uma interface simples construída com **Gradio** para manipular e analisar textos em tempo real.",
    theme="soft"
)

# Executa o aplicativo
if __name__ == "__main__":
    interface.launch()