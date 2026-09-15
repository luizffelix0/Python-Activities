from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
# ==========================================
# FUNÇÕES
# ==========================================
 
def salvar_cliente():
 
    try:
 
        nome = txt_nome.get()
        email = txt_email.get()
        telefone = txt_telefone.get()
        cidade = txt_cidade.get()
        cpf = txt_cpf.get()
 
        # VALIDAÇÃO
        if nome == "":
            raise ValueError("O campo nome está vazio!")
 
        # ABRIR ARQUIVO
        arquivo = open("clientes.txt", "a", encoding="utf-8")
 
        # SALVAR DADOS
        arquivo.write(
            f"{nome};{email};{telefone};{cidade};{cpf}\n"
        )
 
        arquivo.close()
 
        messagebox.showinfo(
            "Sucesso",
            "Cliente salvo com sucesso!"
        )
 
        limpar_campos()
 
    except ValueError as erro:
        messagebox.showwarning(
            "Atenção",
            str(erro)
        )
 
    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao salvar cliente:\n{erro}"
        )
 
 
def consultar_clientes():
 
    try:
 
        lista_clientes.delete(0, END)
 
        arquivo = open("clientes.txt", "r", encoding="utf-8")
 
        clientes = arquivo.readlines()
 
        arquivo.close()
 
        for cliente in clientes:
 
            dados = cliente.strip().split(";")
 
            texto = (
                f"Nome: {dados[0]} | "
                f"E-mail: {dados[1]} | "
                f"Telefone: {dados[2]} | "
                f"Cidade: {dados[3]} | "
                f"CPF: {dados[4]}"
            )
 
            lista_clientes.insert(END, texto)
 
    except FileNotFoundError:
        messagebox.showwarning(
            "Arquivo não encontrado",
            "Nenhum cliente foi cadastrado ainda."
        )
 
    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao consultar clientes:\n{erro}"
        )
 
 
def limpar_campos():
 
    txt_nome.delete(0, END)
    txt_email.delete(0, END)
    txt_telefone.delete(0, END)
    txt_cidade.delete(0, END)
    txt_cpf.delete(0, END)
 
 
# ==========================================
# JANELA
# ==========================================
 
janela = Tk()
 
janela.title("Cadastro de Clientes")
janela.geometry("800x600")
janela.config(bg="#EAEAEA")
 
# ==========================================
# TÍTULO
# ==========================================
 
frame_topo = Frame(
    janela,
    bg="#0078D7",
    height=200
)
 
frame_topo.pack(fill=X)
 
titulo = Label(
    frame_topo,
    text="Cadastro de Clientes",
    bg="#0078D7",
    fg="white",
    font=("Arial", 24, "bold")
)
 
titulo.pack(pady=20)
 
# ==========================================
# FORMULÁRIO
# ==========================================
 
frame_form = Frame(
    janela,
    bg="#EAEAEA"
)
 
frame_form.pack(pady=20)
 
# NOME
Label(
    frame_form,
    text="Nome:",
    bg="#EAEAEA",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10, sticky=W)
 
txt_nome = Entry(
    frame_form,
    width=40,
    font=("Arial", 12)
)
 
txt_nome.grid(row=0, column=1)
 
# EMAIL
Label(
    frame_form,
    text="E-mail:",
    bg="#EAEAEA",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10, sticky=W)
 
txt_email = Entry(
    frame_form,
    width=40,
    font=("Arial", 12)
)
 
txt_email.grid(row=1, column=1)
 
# TELEFONE
Label(
    frame_form,
    text="Telefone:",
    bg="#EAEAEA",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=10, sticky=W)
 
txt_telefone = Entry(
    frame_form,
    width=40,
    font=("Arial", 12)
)
 
txt_telefone.grid(row=2, column=1)
 
# CIDADE
Label(
    frame_form,
    text="Cidade:",
    bg="#EAEAEA",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=10, sticky=W)
 
txt_cidade = Entry(
    frame_form,
    width=40,
    font=("Arial", 12)
)
 
txt_cidade.grid(row=3, column=1)
 
# CPF
Label(
    frame_form,
    text="CPF:",
    bg="#EAEAEA",
    font=("Arial", 12)
).grid(row=4, column=0, padx=10, pady=10, sticky=W)
 
txt_cpf = Entry(
    frame_form,
    width=40,
    font=("Arial", 12)
)
 
txt_cpf.grid(row=4, column=1)
 
# ==========================================
# BOTÕES
# ==========================================
 
frame_botoes = Frame(
    janela,
    bg="#EAEAEA"
)
 
frame_botoes.pack(pady=20)
 
btn_salvar = Button(
    frame_botoes,
    text="Salvar",
    width=15,
    bg="#0078D7",
    fg="white",
    font=("Arial", 12, "bold"),
    command=salvar_cliente
)
 
btn_salvar.grid(row=0, column=0, padx=10)
 
btn_consultar = Button(
    frame_botoes,
    text="Consultar",
    width=15,
    bg="#0078D7",
    fg="white",
    font=("Arial", 12, "bold"),
    command=consultar_clientes
)
 
btn_consultar.grid(row=0, column=1, padx=10)
 
btn_limpar = Button(
    frame_botoes,
    text="Limpar",
    width=15,
    bg="#0078D7",
    fg="white",
    font=("Arial", 12, "bold"),
    command=limpar_campos
)
 
btn_limpar.grid(row=0, column=2, padx=10)
 
# ==========================================
# LISTA DE CLIENTES
# ==========================================
 
frame_lista = Frame(
    janela,
    bg="#EAEAEA"
)
 
frame_lista.pack(pady=20)
 
Label(
    frame_lista,
    text="Clientes Cadastrados",
    bg="#EAEAEA",
    font=("Arial", 14, "bold")
).pack()
 
lista_clientes = Listbox(
    frame_lista,
    width=100,
    height=10,
    font=("Arial", 10)
)
 
lista_clientes.pack(pady=10)
 
# ==========================================
# EXECUTAR
# ==========================================
 
janela.mainloop()
 