
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox as MessageBox
from tkinter.ttk import Progressbar

import mysql.connector as mysql

from PIL import Image, ImageTk
#INICIALIZAÇÃO
def start():
        global root,e_name,e_senha, nomefra, texto, l_nome, l_pass, insert, senha_esquecida, senha_criar, statusbd, l_status, frame_fundo_senhaesquecida,texto_fundo_senhaesquecida, frame_fundo_senhaesquecida,paginasenhaesquecida, imvericonta, l_vericonta, texto_senha_esquecida, texto_email_senhaesquecida, e_senha_esquecida, e_email_senhaesquecida,botao_senha_esquecida,btn_senha_esquecida_volta,cadastro_fundo,texto_fundo_cadastro,paginacadastro,cpf1,nome1,email1,telefone1,usuario1,senha1,e_cpf,e_nome,e_email,e_telefone,e_usuario,e_cria_senha,btn_cada,btn_cada_volta,titulo_sms_cadastro,texto_fundo_sms_cadastro,telefio_cadastro,im_cada_sms,l_cada_sms,texto_sms_cadastro,texto_sms_cadastro,texto_sms_status_cadastro,codi_sms_cadastro,botao_verificar_sms__cadastro,botao_enviar_sms_cadastro,linha_sms_cadastro,style,bar2,titulo,texto_fundo_sms,telefio,imsms,l_sms,texto_sms,texto_sms_fundo,texto_sms_cadastro_fundo,texto_sms_status,codi_sms,botao_verificar,botao_enviar,linha,bar,fundo_nova_senha,textofundo_nova_senha,principal_nova_senha,imeditpass,l_editpass,texto_edit_texto_nova_senha,texto_nova_senha,texto2_nova_senha,texto_novasenha_status,codi_nova_senha,codi2_nova_senha,botao_verificar_nova_senha,linha_nova_senha,bar1
        

        #-----------------------------------------------
        #CONFIG TELA PARA CARREGAR
        #-----------------------------------------------
        root = Tk()
        #root.geometry("750x550");
        root.title("Login e SMS")
        root.iconbitmap("images/login.ico")

        window_height = 550
        window_width = 750

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/1.8))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        #-----------------------------------------------
        #FRAME PRINCIPAL
        #-----------------------------------------------
        #FUNDO LOGIN
        #-----------------------------------------------
        nomefra = Frame(root,bg='#3b3b3b')
        #-----------------------------------------------
        #TITULO PAGINA
        #-----------------------------------------------
        texto = Label(root, text="Login ", font=('bold',40),bg='#3b3b3b',fg='#feffff')
        #-----------------------------------------------
        #CRIA IMAGEM USUARIO
        #-----------------------------------------------
        imnome = Image.open('images/username.png')
        imnome = imnome.resize((30,30))
        imnome = ImageTk.PhotoImage(imnome)
        #-----------------------------------------------
        #CARREGA IMAGEM USUARIO
        #-----------------------------------------------
        l_nome = Label(root, image=imnome, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        #-----------------------------------------------
        #CRIA IMAGEM SENHA
        #-----------------------------------------------
        impass = Image.open('images/password.png')
        impass = impass.resize((30,30))
        impass = ImageTk.PhotoImage(impass)
        #-----------------------------------------------
        #CARREGA IMAGEM SENHA
        #-----------------------------------------------
        l_pass = Label(root, image=impass, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
        #-----------------------------------------------
        #CAMPOS
        #-----------------------------------------------
        e_name = Entry(root,font=(10),width=33)
        e_senha = Entry(root,font=(10),width=33,show='*')
        #-----------------------------------------------
        #BOTAO
        #-----------------------------------------------
        insert = Button(root, text="Logar", font=("italic", 11), command=logar, width=30,height=2,bg='#3b3b3b',fg='#feffff',activebackground="#abaaaa", overrelief=RIDGE,bd=0)

        senha_esquecida = Button(root, text="Esqueceu a senha ?" ,fg="black" ,bd = 0, activeforeground="#3b3b3b", command=senhaesque)#senhaesque

        senha_criar = Button(root, text="Criar uma Conta" ,fg="black" ,bd = 0, activeforeground="#3b3b3b", command=cadastro)




        #-----------------------------------------------
        #FRAME ESQUECEU A SENHA - FAZER
        #-----------------------------------------------
        #FUNDO TITULO
        #-----------------------------------------------
        frame_fundo_senhaesquecida = Frame(root,bg='#3b3b3b')
        #TEXTO PARA O FUNDO
        #-----------------------------------------------
        texto_fundo_senhaesquecida = Label(frame_fundo_senhaesquecida, text="Verificar Conta",font=("bold",30) ,bg="#3b3b3b", fg="#feffff")
        #-----------------------------------------------
        paginasenhaesquecida = Frame(root)
        #-----------------------------------------------
        #-----------------------------------------------
        #CRIA IMAGEM VERIFICAR CONTA
        #-----------------------------------------------
        imvericonta = Image.open('images/vericonta.png')
        imvericonta = imvericonta.resize((80,80))
        imvericonta = ImageTk.PhotoImage(imvericonta)
        #-----------------------------------------------
        #CARREGA IMAGEM VERIFICAR CONTA
        #-----------------------------------------------
        l_vericonta = Label(paginasenhaesquecida, image=imvericonta, compound=LEFT, anchor='nw')
        #-----------------------------------------------
        #TEXTO DO CAMPO
        texto_senha_esquecida = Label(paginasenhaesquecida, text="CPF",font =('Arial Black', 9))
        texto_email_senhaesquecida = Label(paginasenhaesquecida, text="E-mail",font =('Arial Black', 9))
        #-----------------------------------------------
        #CAMPO
        e_senha_esquecida = Entry(paginasenhaesquecida,font=(20),width=32)
        e_email_senhaesquecida = Entry(paginasenhaesquecida,font=(20),width=32)
        #-----------------------------------------------
        #BOTAO

        botao_senha_esquecida = Button(paginasenhaesquecida, text="Confirmar", font=("italic", 11), command=confirmar_user_senha, width=30,height=2,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")
        btn_senha_esquecida_volta = Button(paginasenhaesquecida, text="Voltar", font=("italic", 11), command=inicio, width=30,height=2,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")

        #-----------------------------------------------
        #-----------------------------------------------





        #-----------------------------------------------
        #FRAME CADASTRAR
        #-----------------------------------------------
        #FUNDO TITULO
        #-----------------------------------------------
        cadastro_fundo = Frame(root, bg='#3b3b3b')
        #-----------------------------------------------
        #TEXTO PARA O FUNDO
        #-----------------------------------------------
        texto_fundo_cadastro = Label(cadastro_fundo, text="Criar uma Conta",font=("bold",35) ,bg="#3b3b3b", fg="#feffff")
        #-----------------------------------------------
        #FRAME 2 PAGINA CADASTRO - ONDE FICA TODOS OS CAMPOS
        #-----------------------------------------------
        paginacadastro = Frame(root)
        #-----------------------------------------------
        #TEXTOS PARA OS CAMPOS
        #-----------------------------------------------
        cpf1 = Label(paginacadastro, text="CPF",font=('Arial Black', 9))
        nome1 = Label(paginacadastro, text="Nome",font=('Arial Black', 9))
        email1 = Label(paginacadastro, text="E-mail",font=('Arial Black', 9))
        telefone1 = Label(paginacadastro, text="Telefone",font=('Arial Black', 9))
        usuario1 = Label(paginacadastro, text="Usuário",font=('Arial Black', 9))
        senha1 = Label(paginacadastro, text="Senha",font=('Arial Black', 9))
        #-----------------------------------------------
        #CAMPOS
        #-----------------------------------------------
        e_cpf = Entry(paginacadastro, font=(20),width=28)
        e_nome = Entry(paginacadastro,font=(20),width=28)
        e_email = Entry(paginacadastro,font=(20),width=28)
        e_telefone = Entry(paginacadastro,font=(20),width=28,show='x')
        e_usuario = Entry(paginacadastro,font=(20),width=28)
        e_cria_senha = Entry(paginacadastro,font=(20),width=28,show='*')
        #-----------------------------------------------
        #BOTAO
        #-----------------------------------------------
        btn_cada = Button(paginacadastro, text="Cadastrar", font=("italic", 11), command=fazer_cadastro, width=30,height=2,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")
        btn_cada_volta = Button(paginacadastro, text="Voltar", font=("italic", 11), command=inicio, width=30,height=2,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")
        #-----------------------------------------------





       
        #-----------------------------------------------
        #FRAME PAGINA SMS- CADASTRO
        #-----------------------------------------------
        #FUNDO TITULO
        #-----------------------------------------------
        titulo_sms_cadastro = Frame(root, bg="#3b3b3b")
        #-----------------------------------------------
        #TEXTO PARA O FUNDO
        #-----------------------------------------------
        texto_fundo_sms_cadastro = Label(titulo_sms_cadastro, text="CONFIRMAR SMS ",bg="#3b3b3b", fg="white",font=("bold",30))

        #-----------------------------------------------
        #FRAME 2 PAGINA CADASTRO - ONDE FICA TODOS OS CAMPOS
        #-----------------------------------------------
        telefio_cadastro = Frame(root)
        #-----------------------------------------------
        #TEXTO DO CAMPO
        #-----------------------------------------------
        #-----------------------------------------------
        #CRIA IMAGEM SMS
        #-----------------------------------------------
        im_cada_sms = Image.open('images/sms.png')
        im_cada_sms = im_cada_sms.resize((80,80))
        im_cada_sms = ImageTk.PhotoImage(im_cada_sms)
        #-----------------------------------------------
        #CARREGA IMAGEM SMS
        #-----------------------------------------------
        l_cada_sms= Label(telefio_cadastro, image=im_cada_sms, compound=LEFT, anchor='nw')

        #-----------------------------------------------
        texto_sms_cadastro = Label(telefio_cadastro, text="Codigo: ",font=('Arial Black', 9))

        texto_sms_cadastro_fundo = Label(telefio_cadastro, text="Insira o código SMS enviado para seu celular", wraplength=250, font =('Arial Black', 13))

        texto_sms_status_cadastro = Label(telefio_cadastro, text="Quase Lá!", font =('Arial Black', 13))
        #-----------------------------------------------
        #CAMPO
        #-----------------------------------------------

        codi_sms_cadastro = Entry(telefio_cadastro, text=" ",font=(20),width=32)

        #-----------------------------------------------
        #BOTAO
        #-----------------------------------------------
        botao_verificar_sms__cadastro = Button(telefio_cadastro, text=" Verificar",font=("italic", 11),command=verificar,width=10,height=1,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa" )


        botao_enviar_sms_cadastro = Button(telefio_cadastro,text=" Não recebeu o SMS ? ",bd=0,command=enviar_codigo,activebackground="#abaaaa" )#ver

        #-----------------------------------------------
        #LINHA
        #-----------------------------------------------
        #Criando uma linha horizontal
        linha_sms_cadastro = ttk.Separator(telefio_cadastro, orient=HORIZONTAL)

        #-----------------------------------------------
        #-----------------------------------------------
        #CRIA CARREGAMENTO NOVA SENHA

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background="black")
        style.configure("TProgressbar", thickness=10)
        bar2 = Progressbar(telefio_cadastro , length=190,style='black.Horizontal.TProgressbar')
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------



        #-----------------------------------------------
        #FRAME PAGINA SMS
        #-----------------------------------------------
        #FUNDO TITULO
        #-----------------------------------------------
        titulo = Frame(root, bg="#3b3b3b")
        #-----------------------------------------------
        #TEXTO PARA O FUNDO
        #-----------------------------------------------
        texto_fundo_sms = Label(titulo, text="CONFIRMAR SMS ",bg="#3b3b3b", fg="white",font=("bold",30))

        #-----------------------------------------------
        #FRAME 2 PAGINA CADASTRO - ONDE FICA TODOS OS CAMPOS
        #-----------------------------------------------
        telefio = Frame(root)
        #-----------------------------------------------
        #-----------------------------------------------
        #CRIA IMAGEM SMS
        #-----------------------------------------------
        imsms = Image.open('images/sms.png')
        imsms = imsms.resize((80,80))
        imsms = ImageTk.PhotoImage(imsms)
        #-----------------------------------------------
        #CARREGA IMAGEM SMS
        #-----------------------------------------------
        l_sms= Label(telefio, image=imsms, compound=LEFT, anchor='nw')

        #-----------------------------------------------
        #TEXTO DO CAMPO
        #-----------------------------------------------
        texto_sms = Label(telefio, text="Código: ",font=('Arial Black', 9))

        texto_sms_fundo = Label(telefio, text="Insira o código SMS enviado para seu celular", wraplength=250, font =('Arial Black', 13))

        texto_sms_status = Label(telefio, text="Quase Lá!", font =('Arial Black', 13))


        #-----------------------------------------------
        #CAMPO
        #-----------------------------------------------
        codi_sms = Entry(telefio, text=" ",font=(20),width=32)

        #-----------------------------------------------
        #BOTAO
        #-----------------------------------------------
        botao_verificar = Button(telefio, text="Verificar", font=("italic", 11), command=verificar_sms, width=10,height=1,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")
        #botao_verificar = Button(telefio, text=" Verificar",command=verificar_sms )


        botao_enviar = Button(telefio,text=" Não recebeu o SMS ? ",bd=0,command=enviar_codigo_senha )

        #-----------------------------------------------
        #LINHA
        #-----------------------------------------------
        #Criando uma linha horizontal
        linha = ttk.Separator(telefio, orient=HORIZONTAL)
        #-----------------------------------------------
        #CRIA CARREGAMENTO 
        #-----------------------------------------------
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background="black")
        style.configure("TProgressbar", thickness=10)
        bar = Progressbar(telefio, length=190,style='black.Horizontal.TProgressbar')
        #-----------------------------------------------


        
        #-----------------------------------------------
        #FRAME PAGINA NOVA_SENHA
        #-----------------------------------------------
        #FUNDO TITULO NOVA_SENHA
        #-----------------------------------------------
        fundo_nova_senha = Frame(root, bg="#3b3b3b")
        #-----------------------------------------------
        #TEXTO PARA O FUNDO
        #-----------------------------------------------
        textofundo_nova_senha = Label(fundo_nova_senha, text="Nova Senha ",bg="#3b3b3b", fg="white",font=("bold",30))

        #-----------------------------------------------
        #FRAME 2 PAGINA NOVA_SENHA - ONDE FICA TODOS OS CAMPOS
        #-----------------------------------------------
        principal_nova_senha = Frame(root)
        #-----------------------------------------------
        #-----------------------------------------------
        #CRIA IMAGEM EDITARSENHA
        #-----------------------------------------------
        imeditpass = Image.open('images/editpassword.png')
        imeditpass = imeditpass.resize((80,80))
        imeditpass = ImageTk.PhotoImage(imeditpass)
        #-----------------------------------------------
        #CARREGA IMAGEM EDITARSENHA
        #-----------------------------------------------
        l_editpass = Label(principal_nova_senha, image=imeditpass, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')

        texto_edit_texto_nova_senha = Label(principal_nova_senha, text="Insira um nova senha nos campos abaixo", wraplength=250, font =('Arial Black', 13))
        #-----------------------------------------------
        #TEXTO DO CAMPO
        #-----------------------------------------------
        texto_nova_senha = Label(principal_nova_senha, text="Nova Senha ",font=('Arial Black', 9))
        texto2_nova_senha = Label(principal_nova_senha, text="Repetir Senha ",font=('Arial Black', 9))
        texto_novasenha_status = Label(principal_nova_senha, text="Só mudar a senha!", font =('Arial Black', 13))

        #-----------------------------------------------
        #CAMPO
        #-----------------------------------------------
        codi_nova_senha = Entry(principal_nova_senha,font=(20),width=32, show='*')
        codi2_nova_senha = Entry(principal_nova_senha,font=(20),width=32, show='*')

        #-----------------------------------------------
        #BOTAO
        #-----------------------------------------------

        botao_verificar_nova_senha = Button(principal_nova_senha, text="Alterar Senha", font=("italic", 11), command=mudar_senha, width=30,height=2,bg='#3b3b3b',fg='#feffff',relief=RAISED, overrelief=RIDGE,activebackground="#abaaaa")



        #LINHA
        #-----------------------------------------------
        #Criando uma linha horizontal
        linha_nova_senha = ttk.Separator(principal_nova_senha, orient=HORIZONTAL)

        #-----------------------------------------------
        #CRIA CARREGAMENTO NOVA SENHA

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background="black")
        style.configure("TProgressbar", thickness=10)
        bar1 = Progressbar(principal_nova_senha , length=190,style='black.Horizontal.TProgressbar')
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------
        #-----------------------------------------------




        #IMAGEM STATUS BANCO DE DADOS
        l_status = Label(root, image="", compound=LEFT, font=('Ivy 10 bold'), anchor='nw')

        statusbd = Image.open('images/databaseoff.png')
        statusbd = statusbd.resize((50,50))
        statusbd = ImageTk.PhotoImage(statusbd)
        l_status['image'] = statusbd

        contagem()
        inicio()
        root.mainloop()

        
#-----------------------------------------------
#FRAMES
#-----------------------------------------------
#FRAME PRINCIPAL
#PAGINA - LOGIN
def inicio():
    #Após confirmar, apaga as linhas
    e_name.delete(0, 'end')
    e_senha.delete(0, 'end')
    root.bind('<Return>', logar)
    #global e_name, e_senha, nomefra, insert, senha_esquecida, senha_criar, l_nome, l_pass, texto
    #--------------------------------------------------------------------
    #-----------------------------------------------
    #REMOVE FRAME PAGINA NOVA_SENHA
    #-----------------------------------------------
    fundo_nova_senha.place_forget()  
    textofundo_nova_senha.place_forget()
    principal_nova_senha.place_forget()
    l_editpass.place_forget()
    texto_nova_senha.place_forget()
    texto2_nova_senha.place_forget()
    codi_nova_senha.place_forget()
    codi2_nova_senha.place_forget()
    botao_verificar_nova_senha.place_forget()
    linha_nova_senha.place_forget()
    bar1.place_forget()
    #-----------------------------------------------
    #REMOVE PAGINA SMS
    #-----------------------------------------------
    titulo.place_forget()
    texto_fundo_sms.place_forget()
    telefio.place_forget()
    l_sms.place_forget()
    texto_sms.place_forget()
    texto_sms_fundo.place_forget()
    texto_sms_status.place_forget()
    codi_sms.place_forget()
    botao_verificar.place_forget()   
    botao_enviar.place_forget()
    linha.place_forget()
    bar.place_forget()
    #-----------------------------------------------
    #REMOVE PAGINA SENHA ESQUECIDA
    #-----------------------------------------------
    frame_fundo_senhaesquecida.place_forget()
    texto_fundo_senhaesquecida.place_forget()
    paginasenhaesquecida.place_forget()
    l_vericonta.place_forget()
    texto_senha_esquecida.place_forget()
    texto_email_senhaesquecida.place_forget()
    e_senha_esquecida.place_forget()
    e_email_senhaesquecida.place_forget()
    botao_senha_esquecida.place_forget()
    btn_senha_esquecida_volta.place_forget()
    #-----------------------------------------------
    #REMOVE CADASTRO
    #-----------------------------------------------
    paginacadastro.place_forget()
    cadastro_fundo.place_forget()
    texto_fundo_cadastro.place_forget()
    cpf1.place_forget()
    nome1.place_forget()
    email1.place_forget()
    telefone1.place_forget()
    usuario1.place_forget()
    senha1.place_forget()
    e_cpf.place_forget()
    e_nome.place_forget()
    e_email.place_forget()
    e_telefone.place_forget()
    e_usuario.place_forget()
    e_cria_senha.place_forget()
    btn_cada.place_forget()
    btn_cada_volta.place_forget()
    #--------------------------------------------------------------------
    #-----------------------------------------------
    #REMOVE PAGINA SMS_CADASTRO 
    #-----------------------------------------------
    titulo_sms_cadastro.place_forget()
    texto_fundo_sms_cadastro.place_forget()
    telefio_cadastro.place_forget()
    texto_sms_cadastro.place_forget()
    codi_sms_cadastro.place_forget()
    botao_verificar_sms__cadastro.place_forget()
    botao_enviar_sms_cadastro.place_forget()
    linha_sms_cadastro.place_forget()
    l_cada_sms.place_forget()
    texto_sms_cadastro_fundo.place_forget()
    texto_sms_status_cadastro.place_forget()

    #-----------------------------------------------
    #CARREGA INICIO
    #-----------------------------------------------
    #CONFIG TELA PRINCIPAL
    #-----------------------------------------------
    nomefra.place(y=50,width=750,height=90)
    texto.place(x=320, y=50)
    #-----------------------------------------------
    #TEXTO DOS CAMPOS
    #-----------------------------------------------
    e_name.place(x=250, y=200,height=27)
    e_senha.place(x=250, y=260,height=27)
    #-----------------------------------------------
    #IMAGEM
    #-----------------------------------------------
    l_nome.place(x=180,y=195)
    l_pass.place(x=180,y=255)
    #-----------------------------------------------
    #BOTAO
    #-----------------------------------------------
    insert.place(x=250, y=340)
    senha_esquecida.place(x=250,y=430)
    senha_criar.place(x=250,y=460)
    #-----------------------------------------------
    #Conta Pessoas
    #pessoas.place(x=500,y=520);
    #list1.place(x=570,y=520, height=18, width=20)


def contagem():
      
     try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
        #cursor = con.cursor()
        #------------------------------------
        #comando para contar quantos tem no mysql
        #cursor.execute("select count(*) from login")
        #const = cursor.fetchall()
        #Para deleletar a contagem depois que foi mostrada
        #list1.delete(0, list1.size())
        #--------------------------------------
        #------------------------------------
        #for co in const:
            #num = ' '+str(co[0])+''
            #list1.insert(list1.size()+1, num)
            
        con.close()
        l_status.place_forget()
     except:
           l_status.place(x=650,y=470)


#Pagina Principal   
def logar(event=None):
    global nome_banco
    name = e_name.get()
    senha = e_senha.get()

    if(name =="" or senha==""):
        MessageBox.showinfo("Status", "Todos os campos são requeridos")
    else:
        #VERIFICA SE ESTA ON O BANCO DE DADOS 
      try:
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
        cursor = con.cursor()
        #Decisão se o usuario é cadastrado ou não 
        l_status.place_forget()
        try:
          cursor.execute("select nome,id_cpf from login where nome  = '"+ e_name.get() +"' and senha = '"+ e_senha.get() +"'")
          nome_banco = cursor.fetchall()
          print("-------")
          print(nome_banco[0][0])
          print(nome_banco[0][1])
          print("-------")
          if e_name.get() == (f"{nome_banco[0][0]}"):
            e_name.delete(0, 'end')
            e_senha.delete(0, 'end')
            con.close();
            root.destroy()

            #-----------------------------------------------------------------------------------------------------------------------
            #Janela Adminstrador
            #-----------------------------------------------
            #PASSA O USUARIO PARA A JANELA CLIENTE
            #-----------------------------------------------
            vaijogarusuario =nome_banco[0][0]
            #-----------------------------------------------
            #VERIFICACAO SE O SERVIDOR ESTA ONLINE
            #-----------------------------------------------
            def conexao_cliente():
               try: 
                #Conexão e Entrada de dados no banco
                con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
                cursor = con.cursor()
               except:
                   conexao_remove()
                   MessageBox.showinfo("Status", "Falha de Conexão com o Servidor")
                   admin.destroy()
             #-----------------------------------------------
            



            #-----------------------------------------------
            #REMOVE TODOS FRAMES ANTES DE FECHAR
            #-----------------------------------------------
            def conexao_remove():
                #-----------------------------------------------
                #REMOVE PAGINA PERFIL
                #-----------------------------------------------
                texto_perfil.place_forget()
                pagina_perfil.place_forget()
                texto_perfil_nome.place_forget()
                texto_perfil_cpf.place_forget()
                texto_perfil_email.place_forget()
                texto_perfil_telefone.place_forget()
                texto_perfil_usuario.place_forget()
                texto_perfil_senha.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA CONFIGURACAO
                #-----------------------------------------------
                pagina_config.place_forget()
               
                texto_conf.place_forget()
                texto_conf_idioma.place_forget()
                texto_conf_regiao.place_forget()
                texto_conf_ip.place_forget()
                texto_conf_seguranca.place_forget()
                texto_conf_status.place_forget()
                texto_conf_versao.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGI_DASH
                #-----------------------------------------------
                pagina_dashboard.place_forget()
                l_im_clie_dash.place_forget()
                texto_das.place_forget()
                frame1.place_forget()
                texto_venda.place_forget()
                texto_venda_valor.place_forget()
                frame2.place_forget()
                texto_lucro.place_forget()
                texto_lucro_valor.place_forget()
                l_clie_grafi.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA SOBRE
                pagina_sobre.place_forget()
                texto_sobre.place_forget()
                texto_sobre_1.place_forget()
                texto_sobre_2.place_forget()
                texto_sobre_3.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA AJUDA
                #-----------------------------------------------
                pagina_ajuda.place_forget()
                texto_ajuda.place_forget()
                texto_ajuda_1.place_forget()
                texto_ajuda_2.place_forget()
                texto_ajuda_3.place_forget()
                texto_ajuda_4.place_forget()
                texto_ajuda_5.place_forget()
                texto_ajuda_6.place_forget()
                #-----------------------------------------------



            #-----------------------------------------------
            #-----------------------------------------------
            #CONFIG INICIAL TKINTER
            #-----------------------------------------------
            admin = Tk()
            admin.resizable(True,True)
            admin.state("zoomed")
            admin.iconbitmap("images/login.ico")
            admin.title("Dashboard")
            #-----------------------------------------------
            #-----------------------------------------------
            #FRAMES DAS PAGINAS
            #-----------------------------------------------
            #FRAME PAGINA DASHBOARD
            #-----------------------------------------------
            pagina_dashboard = Frame(admin)
            #-----------------------------------------------
            #-----------------------------------------------
            #PAGINA CONFIGURACAO
            #-----------------------------------------------
            pagina_config = Frame(admin)
            #pagina_config.place(x=250,y=80,height=625,width=1116)
            #-----------------------------------------------
            #PAGINA PERFIL
            #-----------------------------------------------
            pagina_perfil = Frame(admin)
            #-----------------------------------------------
            #-----------------------------------------------
            #PAGINA AJUDA
            #-----------------------------------------------
            pagina_ajuda = Frame(admin)
            #-----------------------------------------------
            #-----------------------------------------------
            #PAGINA SOBRE
            #-----------------------------------------------
            pagina_sobre = Frame(admin)
            #-----------------------------------------------
            #FUNCAO E DEFINICAO DOS FRAMES PAGINAS
            #-----------------------------------------------
            #-----------------------------------------------
            #FUNCAO CARREGA PAGINA INICIO
            #-----------------------------------------------

            def pagi_dash():
                #-----------------------------------------------
                #REMOVE PAGINA PERFIL
                #-----------------------------------------------
                texto_perfil.place_forget()
                pagina_perfil.place_forget()
                texto_perfil_nome.place_forget()
                texto_perfil_cpf.place_forget()
                texto_perfil_email.place_forget()
                texto_perfil_telefone.place_forget()
                texto_perfil_usuario.place_forget()
                texto_perfil_senha.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA CONFIGURACAO
                #-----------------------------------------------
                pagina_config.place_forget()
                
                texto_conf.place_forget()
                texto_conf_idioma.place_forget()
                texto_conf_regiao.place_forget()
                texto_conf_ip.place_forget()
                texto_conf_seguranca.place_forget()
                texto_conf_status.place_forget()
                texto_conf_versao.place_forget()
                #-----------------------------------------------
                #REMOVE PAGINA AJUDA
                #-----------------------------------------------
                pagina_ajuda.place_forget()
                texto_ajuda.place_forget()
                texto_ajuda_1.place_forget()
                texto_ajuda_2.place_forget()
                texto_ajuda_3.place_forget()
                texto_ajuda_4.place_forget()
                texto_ajuda_5.place_forget()
                texto_ajuda_6.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA SOBRE
                pagina_sobre.place_forget()
                texto_sobre.place_forget()
                texto_sobre_1.place_forget()
                texto_sobre_2.place_forget()
                texto_sobre_3.place_forget()
                #-----------------------------------------------
                
                #-----------------------------------------------
                #CRIA PAGINA DASHBOARD
                #-----------------------------------------------
                pagina_dashboard.place(x=250,y=80,height=625,width=1116)
                #-----------------------------------------------
                #dasboard
                #CARREGA IMAGEM dashboard
                #-----------------------------------------------
                l_im_clie_dash.place(x=100,y=20)
                #-----------------------------------------------
                texto_das.place(x=150, y=20)
                #-----------------------------------------------
                #DENTRO DO DASHBOARD
                frame1.place(x=100,y=78)
                texto_venda.place(x=140, y=10)
                texto_venda_valor.place(x=144, y=80)
                #-----------------------------------------------
                #DENTRO DO DASHBOARD
                frame2.place(x=600,y=78)
                texto_lucro.place(x=140, y=10)
                texto_lucro_valor.place(x=144, y=80)
                #-----------------------------------------------
                l_clie_grafi.place(x=100,y=320)
                #-----------------------------------------------
                conexao_cliente()

            #-----------------------------------------------
            #DEFINICAO DASHBOARD
            #CRIA IMAGEM dashboard
            #-----------------------------------------------
            im_clie_dash = Image.open('images/dashboard.png')
            im_clie_dash = im_clie_dash.resize((30,30))
            im_clie_dash = ImageTk.PhotoImage(im_clie_dash)
            #-----------------------------------------------
            #CARREGA IMAGEM dashboard
            #-----------------------------------------------
            l_im_clie_dash= Label(pagina_dashboard, image=im_clie_dash, compound=LEFT, anchor='nw')
            #-----------------------------------------------
            texto_das = Label(pagina_dashboard, text="Dashboard", font=("Arial Black",15),fg="#3b3b3b")
            #-----------------------------------------------
            #DENTRO DO DASHBOARD
            frame1 = Frame(pagina_dashboard, bg="#feffff",height=200,width=400,highlightbackground="#3b3b3b",highlightthickness=1)
            texto_venda = Label(frame1, text="Vendas", font=("Arial Black",20),bg="#feffff",fg="#3b3b3b")
            texto_venda_valor = Label(frame1, text="0%", font=("Arial Black",40),bg="#feffff",fg="#3b3b3b")
            #-----------------------------------------------
            #DENTRO DO DASHBOARD
            frame2 = Frame(pagina_dashboard, bg="#feffff",height=200,width=400,highlightbackground="#3b3b3b",highlightthickness=1)
            texto_lucro = Label(frame2, text="Lucros", font=("Arial Black",20),bg="#feffff",fg="#3b3b3b")
            texto_lucro_valor = Label(frame2, text="0%", font=("Arial Black",40),bg="#feffff",fg="#3b3b3b")
            #-----------------------------------------------
            #CRIA IMAGEM GRAFICO
            #-----------------------------------------------
            im_clie_grafi = Image.open('images/grafico.png')
            im_clie_grafi = im_clie_grafi.resize((900,250))
            im_clie_grafi = ImageTk.PhotoImage(im_clie_grafi)
            #-----------------------------------------------
            #CARREGA IMAGEM GRAFICO
            #-----------------------------------------------
            l_clie_grafi= Label(pagina_dashboard, image=im_clie_grafi, compound=LEFT, anchor='nw', bg="#3b3b3b")
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------



            #-----------------------------------------------
            #PAGINA CONFIGURACAO
            #-----------------------------------------------
            def pagi_conf():
                #-----------------------------------------------
                #REMOVE PAGINA PERFIL
                #-----------------------------------------------
                texto_perfil.place_forget()
                pagina_perfil.place_forget()
                texto_perfil_nome.place_forget()
                texto_perfil_cpf.place_forget()
                texto_perfil_email.place_forget()
                texto_perfil_telefone.place_forget()
                texto_perfil_usuario.place_forget()
                texto_perfil_senha.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA AJUDA
                #-----------------------------------------------
                pagina_ajuda.place_forget()
                texto_ajuda.place_forget()
                texto_ajuda_1.place_forget()
                texto_ajuda_2.place_forget()
                texto_ajuda_3.place_forget()
                texto_ajuda_4.place_forget()
                texto_ajuda_5.place_forget()
                texto_ajuda_6.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA SOBRE
                pagina_sobre.place_forget()
                texto_sobre.place_forget()
                texto_sobre_1.place_forget()
                texto_sobre_2.place_forget()
                texto_sobre_3.place_forget()
                #-----------------------------------------------
                #REMOVE PAGI_DASH
                #-----------------------------------------------
                pagina_dashboard.place_forget()
                l_im_clie_dash.place_forget()
                texto_das.place_forget()
                frame1.place_forget()
                texto_venda.place_forget()
                texto_venda_valor.place_forget()
                frame2.place_forget()
                texto_lucro.place_forget()
                texto_lucro_valor.place_forget()
                l_clie_grafi.place_forget()
                #-----------------------------------------------
                
                #-----------------------------------------------
                #CRIA PAGINA CONFIGURACAO
                pagina_config.place(x=250,y=80,height=625,width=1116)
               
                texto_conf.place(x=396,y=40)
                texto_conf_idioma.place(x=306,y=130)
                texto_conf_regiao.place(x=450,y=200)
                texto_conf_ip.place(x=437,y=270)
                texto_conf_seguranca.place(x=410,y=340)
                texto_conf_status.place(x=434,y=410)
                texto_conf_versao.place(x=406,y=480)
                bar.place(x=680,y=427)
                bar['value'] = 100
                conexao_cliente()
                #-----------------------------------------------




            #-----------------------------------------------
            #-----------------------------------------------
            #DEFINICAO CONFIGURACAO
            #CRIA IMAGEM configuracao
            #-----------------------------------------------
            texto_conf = Label(pagina_config, text="Configurações", font=("Arial Black",30),fg="#3b3b3b")
            #-----------------------------------------------
            #TEXTOS DENTRO DA PAGINA CONFIGURACAO
            #-----------------------------------------------
            texto_conf_idioma = Label(pagina_config, text="Idioma Nativo: Português - Brasil ", font=("Arial Black",20),fg="#3b3b3b")
            texto_conf_regiao = Label(pagina_config, text="Região: Brasil", font=("Arial Black",20),fg="#3b3b3b")
            texto_conf_ip = Label(pagina_config, text="IP: 192.168.20.1", font=("Arial Black",20),fg="#3b3b3b")
            texto_conf_seguranca = Label(pagina_config, text="Segurança: Ativado", font=("Arial Black",20),fg="#3b3b3b")
            texto_conf_status = Label(pagina_config, text="Status Servidor:", font=("Arial Black",20),fg="#3b3b3b")
            texto_conf_versao = Label(pagina_config, text="Versão: 2.07V Alpha", font=("Arial Black",20),fg="#3b3b3b")
            #-----------------------------------------------
            #STATUS SERVIDOR 
            #-----------------------------------------------
            style = ttk.Style()
            style.theme_use('default')
            style.configure("black.Horizontal.TProgressbar", background="#00e676")
            style.configure("TProgressbar", thickness=15)
            bar = Progressbar(pagina_config, length=30,style='black.Horizontal.TProgressbar')
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------



            #-----------------------------------------------
            #PAGINA CONFIGURACAO
            #-----------------------------------------------
            def pagi_perfil():
                #-----------------------------------------------
                #REMOVE PAGINA CONFIGURACAO
                #-----------------------------------------------
                pagina_config.place_forget()
                
                texto_conf.place_forget()
                texto_conf_idioma.place_forget()
                texto_conf_regiao.place_forget()
                texto_conf_ip.place_forget()
                texto_conf_seguranca.place_forget()
                texto_conf_status.place_forget()
                texto_conf_versao.place_forget()
                bar.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA AJUDA
                #-----------------------------------------------
                pagina_ajuda.place_forget()
                texto_ajuda.place_forget()
                texto_ajuda_1.place_forget()
                texto_ajuda_2.place_forget()
                texto_ajuda_3.place_forget()
                texto_ajuda_4.place_forget()
                texto_ajuda_5.place_forget()
                texto_ajuda_6.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA SOBRE
                pagina_sobre.place_forget()
                texto_sobre.place_forget()
                texto_sobre_1.place_forget()
                texto_sobre_2.place_forget()
                texto_sobre_3.place_forget()
                #-----------------------------------------------
                #REMOVE PAGI_DASH
                #-----------------------------------------------
                pagina_dashboard.place_forget()
                l_im_clie_dash.place_forget()
                texto_das.place_forget()
                frame1.place_forget()
                texto_venda.place_forget()
                texto_venda_valor.place_forget()
                frame2.place_forget()
                texto_lucro.place_forget()
                texto_lucro_valor.place_forget()
                l_clie_grafi.place_forget()
                #-----------------------------------------------
               
                #-----------------------------------------------
                #CRIA PAGINA PERFIL
                pagina_perfil.place(x=250,y=80,height=625,width=1116)
                texto_perfil.pack(pady=30)
               
                texto_perfil_nome.pack(pady=10)
                texto_perfil_cpf.pack(pady=10)
                texto_perfil_email.pack(pady=10)
                texto_perfil_telefone.pack(pady=10)
                texto_perfil_usuario.pack(pady=10)
                texto_perfil_senha.pack(pady=10)
                conexao_cliente()

                #-----------------------------------------------




            #-----------------------------------------------
            #Consulta dos dados para a pagina perfil
            vaijogarcpf =nome_banco[0][1]
            #Método
            #-----------------------------------------------          
            #Conexão e Entrada de dados no banco
            con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
            cursor = con.cursor()
            cursor.execute(f"select cpf, nome, email, telefone from cliente where cpf  = {vaijogarcpf }")
            nome_banco1 = cursor.fetchall()
            con.close();

            #-----------------------------------------------
            #DEFINICAO PERFIL

            #TITULO PERFIL
            #-----------------------------------------------
            texto_perfil = Label(pagina_perfil, text="Perfil", font=("Arial Black",30),fg="#3b3b3b")
            #-----------------------------------------------
            #TEXTOS DENTRO DA PAGINA CONFIGURACAO
            #-----------------------------------------------
            texto_perfil_nome = Label(pagina_perfil, text=f"Nome: {nome_banco1[0][1]}", font=("Arial Black",20),fg="#3b3b3b")

            texto_perfil_cpf = Label(pagina_perfil, text=f"CPF: {nome_banco1[0][0]}", font=("Arial Black",20),fg="#3b3b3b")

            texto_perfil_email = Label(pagina_perfil, text=f"Email: {nome_banco1[0][2]}", font=("Arial Black",20),fg="#3b3b3b")

            texto_perfil_telefone = Label(pagina_perfil, text=f"Contato: xxxxxxxxxxx", font=("Arial Black",20),fg="#3b3b3b")

            texto_perfil_usuario = Label(pagina_perfil, text=f"Usuário: {nome_banco[0][0]}", font=("Arial Black",20),fg="#3b3b3b")

            texto_perfil_senha = Label(pagina_perfil, text="Senha: **********", font=("Arial Black",20),fg="#3b3b3b")
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------






            #-----------------------------------------------
            #PAGINA AJUDA
            #-----------------------------------------------
            def pagi_ajuda():
                #-----------------------------------------------
                #REMOVE PAGINA CONFIGURACAO
                #-----------------------------------------------
                pagina_config.place_forget()
                
                texto_conf.place_forget()
                texto_conf_idioma.place_forget()
                texto_conf_regiao.place_forget()
                texto_conf_ip.place_forget()
                texto_conf_seguranca.place_forget()
                texto_conf_status.place_forget()
                texto_conf_versao.place_forget()
                bar.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA PERFIL
                #-----------------------------------------------
                texto_perfil.place_forget()
                pagina_perfil.place_forget()
                texto_perfil_nome.place_forget()
                texto_perfil_cpf.place_forget()
                texto_perfil_email.place_forget()
                texto_perfil_telefone.place_forget()
                texto_perfil_usuario.place_forget()
                texto_perfil_senha.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA SOBRE
                pagina_sobre.place_forget()
                texto_sobre.place_forget()
                texto_sobre_1.place_forget()
                texto_sobre_2.place_forget()
                texto_sobre_3.place_forget()
                #-----------------------------------------------
                #REMOVE PAGI_DASH
                #-----------------------------------------------
                pagina_dashboard.place_forget()
                l_im_clie_dash.place_forget()
                texto_das.place_forget()
                frame1.place_forget()
                texto_venda.place_forget()
                texto_venda_valor.place_forget()
                frame2.place_forget()
                texto_lucro.place_forget()
                texto_lucro_valor.place_forget()
                l_clie_grafi.place_forget()
                #-----------------------------------------------

               
                #-----------------------------------------------
                #CRIA PAGINA AJUDA
                pagina_ajuda.place(x=250,y=80,height=625,width=1116)
                texto_ajuda.pack(pady=30)
               
                texto_ajuda_1.pack(pady=10)
                texto_ajuda_2.pack(pady=10)
                texto_ajuda_3.pack(pady=10)
                texto_ajuda_4.pack(pady=10)
                texto_ajuda_5.pack(pady=10)
                texto_ajuda_6.pack(pady=10)
                conexao_cliente()

                #-----------------------------------------------

            #-----------------------------------------------
            #DEFINICAO AJUDA

            #TITULO AJUDA
            #-----------------------------------------------
            texto_ajuda = Label(pagina_ajuda, text="Ajuda", font=("Arial Black",30),fg="#3b3b3b")
            #-----------------------------------------------
            #TEXTOS DENTRO DA PAGINA AJUDA
            #-----------------------------------------------
            texto_ajuda_1 = Label(pagina_ajuda, text="Não está carregando seus dados ?", font=("Arial Black",25),fg="#3b3b3b")

            texto_ajuda_2  = Label(pagina_ajuda, text="Feche o programa e o abra novamente", font=("Arial Black",20),fg="#3b3b3b")

            texto_ajuda_3  = Label(pagina_ajuda, text="Está Lento ?", font=("Arial Black",25),fg="#3b3b3b")

            texto_ajuda_4 = Label(pagina_ajuda, text="Verifique sua conexão de Internet", font=("Arial Black",20),fg="#3b3b3b")

            texto_ajuda_5 = Label(pagina_ajuda, text="Sua conta foi acessada de outro lugar ?", font=("Arial Black",25),fg="#3b3b3b")

            texto_ajuda_6 = Label(pagina_ajuda, text="Mude sua senha agora!", font=("Arial Black",20),fg="#3b3b3b")
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------







            #-----------------------------------------------
            #PAGINA SOBRE
            #-----------------------------------------------
            def pagi_sobre():
                #-----------------------------------------------
                #REMOVE PAGINA CONFIGURACAO
                #-----------------------------------------------
                pagina_config.place_forget()
                
                texto_conf.place_forget()
                texto_conf_idioma.place_forget()
                texto_conf_regiao.place_forget()
                texto_conf_ip.place_forget()
                texto_conf_seguranca.place_forget()
                texto_conf_status.place_forget()
                texto_conf_versao.place_forget()
                bar.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGINA PERFIL
                #-----------------------------------------------
                texto_perfil.place_forget()
                pagina_perfil.place_forget()
                texto_perfil_nome.place_forget()
                texto_perfil_cpf.place_forget()
                texto_perfil_email.place_forget()
                texto_perfil_telefone.place_forget()
                texto_perfil_usuario.place_forget()
                texto_perfil_senha.place_forget()
                #-----------------------------------------------
                #-----------------------------------------------
                #REMOVE PAGI_DASH
                #-----------------------------------------------
                pagina_dashboard.place_forget()
                l_im_clie_dash.place_forget()
                texto_das.place_forget()
                frame1.place_forget()
                texto_venda.place_forget()
                texto_venda_valor.place_forget()
                frame2.place_forget()
                texto_lucro.place_forget()
                texto_lucro_valor.place_forget()
                l_clie_grafi.place_forget()
                #-----------------------------------------------

               
                #-----------------------------------------------
                #CRIA PAGINA SOBRE
                pagina_sobre.place(x=250,y=80,height=625,width=1116)
                texto_sobre.pack(pady=15)
               
                texto_sobre_1.pack(pady=10)
                texto_sobre_2.pack(pady=10)
                texto_sobre_3.pack(pady=10)
                

                conexao_cliente()

                #-----------------------------------------------

            #-----------------------------------------------
            #DEFINICAO SOBRE

            #TITULO SOBRE
            #-----------------------------------------------
            texto_sobre = Label(pagina_sobre, text="Projeto de Autenticação de Login e SMS", font=("Arial Black",30),fg="#3b3b3b")
            #-----------------------------------------------
            #TEXTOS DENTRO DA PAGINA SOBRE
            #-----------------------------------------------
            texto_sobre_1 = Label(pagina_sobre, text='''Programa na qual Inicia-se com a tela de Login e com opções para criar
            conta e mudar a senha, e com tela principal dashboard, todos os dados 
            inserido são meramente ficticios, a fim de da amostra e estudo''', font=("Arial Black",17),fg="#3b3b3b")

            texto_sobre_2  = Label(pagina_sobre, text="Desenvolvedor em Python", font=("Arial Black",20),fg="#3b3b3b")

            #-----------------------------------------------
            #CRIA IMAGEM QRCODE
            #-----------------------------------------------
            im_clie_qr = Image.open('images/qr.png')
            im_clie_qr = im_clie_qr.resize((300,300))
            im_clie_qr = ImageTk.PhotoImage(im_clie_qr)
            #-----------------------------------------------
            #CARREGA IMAGEM QRCODE
            #-----------------------------------------------
            texto_sobre_3  = Label(pagina_sobre, image=im_clie_qr, compound=LEFT, anchor='nw', bg="#3b3b3b")

            
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------
            #-----------------------------------------------















            #-----------------------------------------------
            #FUNCAO SAIR DA CONTA
            #-----------------------------------------------
            def sair():
                MessageBox.showinfo("Status", "Desconectado!")
                admin.destroy()
                start()
            #-----------------------------------------------


            #-----------------------------------------------
            #FRAMES QUE IRAO APARECER EM TODAS AS TELAS
            #-----------------------------------------------
            #FRAME ICONES - (FOTO DE PERFIL,TEXTO, SAIR)
            #-----------------------------------------------
            barra_icones = Frame(admin,bg="#3b3b3b")
            barra_icones.place(height=80,width=admin.winfo_screenwidth())
            #-----------------------------------------------

            #-----------------------------------------------
            #FRAME MENU VERTICAL - (PAGINAS PARA IR)
            #-----------------------------------------------
            barra_menu = Frame(admin,bg="#3b3b3b")
            barra_menu.place(y=82,height=613,width=250)
            #-----------------------------------------------
            #-----------------------------------------------


            #-----------------------------------------------
            #DENTRO DOS ICONES
            #-----------------------------------------------
            #CRIA IMAGEM USER
            #-----------------------------------------------
            im_clie_user = Image.open('images/user2.png')
            im_clie_user = im_clie_user.resize((60,60))
            im_clie_user = ImageTk.PhotoImage(im_clie_user)
            #-----------------------------------------------
            #CARREGA IMAGEM user
            #-----------------------------------------------
            l_clie_user= Label(barra_icones, image=im_clie_user, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_clie_user.place(x=40,y=7)

            #-----------------------------------------------

            #-----------------------------------------------
            #CRIA IMAGEM sair
            #-----------------------------------------------
            im_clie_sair = Image.open('images/sair.png')
            im_clie_sair = im_clie_sair.resize((55,55))
            im_clie_sair = ImageTk.PhotoImage(im_clie_sair)
            #-----------------------------------------------
            #CARREGA IMAGEM sair
            #-----------------------------------------------
            l_clie_sair= Button(barra_icones, image=im_clie_sair, compound=LEFT, anchor='nw', bg="#3b3b3b",bd=0,activebackground="#3b3b3b",command=sair)
            l_clie_sair.place(x=1260,y=9)

            #-----------------------------------------------  
            #texto icones
            teste1 = Label(barra_icones, text=f"Seja bem vindo {vaijogarusuario}!", font=("Arial Black",17),bg="#3b3b3b",fg="#feffff")
            teste1.place(x=130, y=17)
            #-----------------------------------------------


            #-----------------------------------------------
            #MENU VERTICAL
            #-----------------------------------------------
            teste1 = Label(barra_menu, text="O que deseja fazer?", font=("Arial Black",13),bg="#3b3b3b",fg="#feffff")
            teste1.place(x=25, y=2)
            #-----------------------------------------------
            #CRIA IMAGEM INICIO
            #-----------------------------------------------
            im_menu_home= Image.open('images/home2.png')
            im_menu_home = im_menu_home.resize((30,30))
            im_menu_home = ImageTk.PhotoImage(im_menu_home)
            #-----------------------------------------------
            #CARREGA IMAGEM INICIO
            #-----------------------------------------------
            l_menu_home= Label(barra_menu, image=im_menu_home, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_menu_home.place(x=40,y=75)
            #texto config
            texto_menu_home = Button(barra_menu, text="Início", font=("Arial Black",10),bg="#3b3b3b",fg="#feffff",bd=0,activebackground="#3b3b3b", activeforeground="#ababab",command=pagi_dash)
            texto_menu_home.place(x=80, y=80)
            #-----------------------------------------------
            linha_menu = ttk.Separator(barra_menu, orient=HORIZONTAL)
            linha_menu.place(x=30, y=127,width=185)
            #-----------------------------------------------
            #CRIA IMAGEM config
            #-----------------------------------------------
            im_menu_config = Image.open('images/config.png')
            im_menu_config = im_menu_config.resize((30,30))
            im_menu_config = ImageTk.PhotoImage(im_menu_config)
            #-----------------------------------------------
            #CARREGA IMAGEM config
            #-----------------------------------------------
            l_menu_config= Label(barra_menu, image=im_menu_config, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_menu_config.place(x=40,y=145)
            #texto config
            texto_menu_config = Button(barra_menu, text="Configurações", font=("Arial Black",10),bg="#3b3b3b",fg="#feffff",bd=0,activebackground="#3b3b3b", activeforeground="#ababab",command=pagi_conf)
            texto_menu_config.place(x=80, y=150)
            #-----------------------------------------------
            linha_menu1 = ttk.Separator(barra_menu, orient=HORIZONTAL)
            linha_menu1.place(x=30, y=195,width=185)
            #-----------------------------------------------
            #CRIA IMAGEM perfil
            #-----------------------------------------------
            im_menu_perfil = Image.open('images/perfil.png')
            im_menu_perfil= im_menu_perfil.resize((30,30))
            im_menu_perfil = ImageTk.PhotoImage(im_menu_perfil)
            #-----------------------------------------------
            #CARREGA IMAGEM perfil
            #-----------------------------------------------
            l_menu_perfil= Label(barra_menu, image=im_menu_perfil, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_menu_perfil.place(x=40,y=215)
            #texto perfil
            texto_menu_perfil = Button(barra_menu, text="Perfil", font=("Arial Black",10),bg="#3b3b3b",fg="#feffff",bd=0,activebackground="#3b3b3b", activeforeground="#ababab",command=pagi_perfil)
            texto_menu_perfil.place(x=80, y=220)
            #-----------------------------------------------
            linha_menu2 = ttk.Separator(barra_menu, orient=HORIZONTAL)
            linha_menu2.place(x=30, y=265,width=185)
            #-----------------------------------------------
            #CRIA IMAGEM help
            #-----------------------------------------------
            im_menu_help = Image.open('images/help.png')
            im_menu_help= im_menu_help.resize((30,30))
            im_menu_help = ImageTk.PhotoImage(im_menu_help)
            #-----------------------------------------------
            #CARREGA IMAGEM help
            #-----------------------------------------------
            l_menu_help= Label(barra_menu, image=im_menu_help, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_menu_help.place(x=40,y=285)
            #-----------------------------------------------
            #texto help
            #-----------------------------------------------
            texto_menu_help = Button(barra_menu, text="Ajuda", font=("Arial Black",10),bg="#3b3b3b",fg="#feffff",bd=0,activebackground="#3b3b3b", activeforeground="#ababab", command=pagi_ajuda)
            texto_menu_help.place(x=80, y=290)
            #-----------------------------------------------
            linha_menu3 = ttk.Separator(barra_menu, orient=HORIZONTAL)
            linha_menu3.place(x=30, y=337,width=185)
            #-----------------------------------------------
            #CRIA IMAGEM sobre
            #-----------------------------------------------
            im_menu_sobre = Image.open('images/sobre.png')
            im_menu_sobre= im_menu_sobre.resize((30,30))
            im_menu_sobre = ImageTk.PhotoImage(im_menu_sobre)
            #-----------------------------------------------
            #CARREGA IMAGEM sobre
            #-----------------------------------------------
            l_menu_sobre= Label(barra_menu, image=im_menu_sobre, compound=LEFT, anchor='nw', bg="#3b3b3b")
            l_menu_sobre.place(x=40,y=355)
            #-----------------------------------------------
            #texto sobre
            #-----------------------------------------------
            texto_menu_sobre= Button(barra_menu, text="Sobre", font=("Arial Black",10),bg="#3b3b3b",fg="#feffff",bd=0,activebackground="#3b3b3b", activeforeground="#ababab",command=pagi_sobre)
            texto_menu_sobre.place(x=80, y=360)
            #-----------------------------------------------





            pagi_dash()
            admin.mainloop()

            #-----------------------------------------------------------------------------------------------------------------------
            
          else:
              e_name.delete(0, 'end')
              e_senha.delete(0, 'end')
              MessageBox.showinfo("Status", "Login Inválido")
              
          
        except:
            #------------------------------------
            #Após confirmar, apaga as linhas
            e_name.delete(0, 'end')
            e_senha.delete(0, 'end')
    
            #contagem()
            #-------------------------------
            #Janela, Inserido com sucesso
            MessageBox.showinfo("Status", "Login inválido")
            con.close();
            #------------------------------
    
      except:
            MessageBox.showinfo("Status", "Sem conexão com o servidor")
            e_name.delete(0, 'end')
            e_senha.delete(0, 'end')
            l_status.place(x=650,y=470)


    #contagem()
    return name, senha

#-----------------------------------------------
#FRAME PAGINA SENHA ESQUECIDA - FRAME SE-0
#-----------------------------------------------
#PÁGINA SENHA ESQUECIDA - FRAME SE-0
#-----------------------------------------------
def senhaesque():
  root.bind('<Return>', confirmar_user_senha)
  try:
    #Conexão e Entrada de dados no banco
    con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
    cursor = con.cursor()
    #-----------------------------------------------
    #REMOVE FRAME PAGINA NOVA_SENHA
    #-----------------------------------------------
    fundo_nova_senha.place_forget()  
    textofundo_nova_senha.place_forget()
    principal_nova_senha.place_forget()
    l_editpass.place_forget()
    texto_nova_senha.place_forget()
    texto2_nova_senha.place_forget()
    codi_nova_senha.place_forget()
    codi2_nova_senha.place_forget()
    botao_verificar_nova_senha.place_forget()
    linha_nova_senha.place_forget()
    #-----------------------------------------------
    #REMOVE PAGINA SMS
    #-----------------------------------------------
    titulo.place_forget()
    texto_fundo_sms.place_forget()
    telefio.place_forget()
    texto_sms.place_forget()
    codi_sms.place_forget()
    botao_verificar.place_forget()   
    botao_enviar.place_forget()
    linha.place_forget()
    #-----------------------------------------------
    #REMOVE PAGINA PRINCIPAL
    #-----------------------------------------------
    nomefra.place_forget()
    e_name.place_forget()
    e_senha.place_forget()
    l_nome.place_forget()
    l_pass.place_forget()
    insert.place_forget()
    senha_esquecida.place_forget()
    senha_criar.place_forget()
    texto.place_forget()
    l_status.place_forget()
    #list1.place_forget()
    #-----------------------------------------------
    #CRIA PAGINA SENHA ESQUECIDA
    #-----------------------------------------------
    #CONFIG TELA CADASTRO
    #-----------------------------------------------
    #FRAME TITULO
    #-----------------------------------------------
    frame_fundo_senhaesquecida.place(height=70,width=750)
    #-----------------------------------------------
    #TEXTO DE FUNDO
    #-----------------------------------------------
    texto_fundo_senhaesquecida.place(x=241,y=10)
    
    #FRAME PAGINA SENHA ESQUECIDA ONDE TEM OS CAMPOS
    #-----------------------------------------------
    paginasenhaesquecida.place(y=70,height=480,width=750)
    #-----------------------------------------------
    #IMAGEM VERIFICA CONTA
    l_vericonta.place(x=333,y=30)
    #-----------------------------------------------
    #TEXTO DO CAMPO
    texto_senha_esquecida.place(x=170,y=130)
    texto_email_senhaesquecida.place(x=170,y=190)
    #-----------------------------------------------
    #CAMPO
    e_senha_esquecida.place(x=229,y=130,height=27)
    e_email_senhaesquecida.place(x=229,y=190,height=27)
    #-----------------------------------------------
    #BOTAO
    botao_senha_esquecida.place(x=235,y=280) # - ABRE A FUNC-0, SE CPF E E-MAIL CORRETO
    #-----------------------------------------(EXECUTA A FUNCAO ENVIAR SMS E ABRE A PAGINA CONFIRMAR SMS)
    #-----------------------------------------------
    btn_senha_esquecida_volta.place(x=235,y=350)

    #-----------------------------------------------
  except:
      MessageBox.showinfo("Status", " Sem conexão com o Servidor")
      l_status.place(x=650,y=470)
      inicio()
  #contagem()

#-----------------------------------------------
#FRAME CADASTRO - C-0
#-----------------------------------------------
#PAGINA CADASTRO C-0
#-----------------------------------------------
def cadastro():
   root.bind('<Return>', fazer_cadastro)
   try:
    #Conexão e Entrada de dados no banco
    con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
    cursor = con.cursor()
    #-----------------------------------------------
    #REMOVE FRAME PAGINA NOVA_SENHA
    #-----------------------------------------------
    fundo_nova_senha.place_forget()  
    textofundo_nova_senha.place_forget()
    principal_nova_senha.place_forget()
    l_editpass.place_forget()
    texto_nova_senha.place_forget()
    texto2_nova_senha.place_forget()
    codi_nova_senha.place_forget()
    codi2_nova_senha.place_forget()
    botao_verificar_nova_senha.place_forget()
    linha_nova_senha.place_forget()
    texto_edit_texto_nova_senha.place_forget()
    #-----------------------------------------------
    #-----------------------------------------------
    #REMOVE PAGINA SENHA ESQUECIDA
    #-----------------------------------------------
    frame_fundo_senhaesquecida.place_forget()
    texto_fundo_senhaesquecida.place_forget()
    paginasenhaesquecida.place_forget()
    l_vericonta.place_forget()
    texto_senha_esquecida.place_forget()
    texto_email_senhaesquecida.place_forget()
    e_senha_esquecida.place_forget()
    e_email_senhaesquecida.place_forget()
    botao_senha_esquecida.place_forget()
    btn_senha_esquecida_volta.place_forget()
    #-----------------------------------------------
    #-----------------------------------------------
    #REMOVE PAGINA PRINCIPAL
    #-----------------------------------------------
    nomefra.place_forget()
    e_name.place_forget()
    e_senha.place_forget()
    l_nome.place_forget()
    l_pass.place_forget()
    insert.place_forget()
    senha_esquecida.place_forget()
    senha_criar.place_forget()
    texto.place_forget()
    l_status.place_forget()
    #list1.place_forget()
    #-----------------------------------------------
    #CRIA PAGINA CADASTRO
    #-----------------------------------------------
    #CONFIG TELA CADASTRO
    #-----------------------------------------------
    cadastro_fundo.place(height=70,width=750)
    texto_fundo_cadastro.pack(pady=10)
    paginacadastro.place(y=70,height=480,width=750)
    #-----------------------------------------------
    #TEXTOS DOS CAMPOS
    #-----------------------------------------------
    cpf1.place(x=200,y=50)
    nome1.place(x=200,y=90)
    email1.place(x=200,y=130)
    telefone1.place(x=200,y=170)
    usuario1.place(x=200,y=210)
    senha1.place(x=200,y=250)
    #-----------------------------------------------
    #CAMPOS DA TELA CADASTRO
    #-----------------------------------------------
    e_cpf.place(x=291,y=50,height=23)
    e_nome.place(x=291,y=90,height=23)
    e_email.place(x=291,y=130,height=23)
    e_telefone.place(x=291,y=170,height=23)
    e_usuario.place(x=291,y=210,height=23)
    e_cria_senha.place(x=291,y=250,height=23)
    #-----------------------------------------------
    #BOTAO
    #-----------------------------------------------
    btn_cada.place(x=250, y=325)
    btn_cada_volta.place(x=250, y=395)
    #-----------------------------------------------
   except:
      MessageBox.showinfo("Status", " Sem conexão com o Servidor")
      l_status.place(x=650,y=470)
      inicio()



#-----------------------------------------------
#FRAME CONFIRMAR SMS_CADASTRO FRAME CS-0
#-----------------------------------------------
#FRAME PAGINA CONFIRMAR SMS_CADASTRO CONFIRMAR SMS ENVIADO - FRAME CS-0
#-----------------------------------------------
def sms_cadastro():
    root.bind('<Return>', verificar)
    texto_sms_status_cadastro['text']="Quase Lá!"
    #-----------------------------------------------
    #REMOVE PAGINA PRINCIPAL
    #-----------------------------------------------
    nomefra.place_forget()
    e_name.place_forget()
    e_senha.place_forget()
    l_nome.place_forget()
    l_pass.place_forget()
    insert.place_forget()
    senha_esquecida.place_forget()
    senha_criar.place_forget()
    texto.place_forget()
    #list1.place_forget()
    #-----------------------------------------------
    #-----------------------------------------------
    #REMOVE CADASTRO
    #-----------------------------------------------
    paginacadastro.place_forget()
    cadastro_fundo.place_forget()
    texto_fundo_cadastro.place_forget()
    cpf1.place_forget()
    nome1.place_forget()
    email1.place_forget()
    telefone1.place_forget()
    usuario1.place_forget()
    senha1.place_forget()
    e_cpf.place_forget()
    e_nome.place_forget()
    e_email.place_forget()
    e_telefone.place_forget()
    e_usuario.place_forget()
    e_cria_senha.place_forget()
    btn_cada.place_forget()
    #--------------------------------------------------------------------



    #-----------------------------------------------
    #CRIA PAGINA SMS_CADASTRO 
    #-----------------------------------------------
    #CONFIG TELA SMS_CADASTRO
    #-----------------------------------------------
    titulo_sms_cadastro.place(height=70,width=750)
    #-----------------------------------------------
    #TEXTO PARA O FUNDO
    #-----------------------------------------------
    texto_fundo_sms_cadastro.place(x=200,y=10)

    #-----------------------------------------------
    #FRAME 2 PAGINA SMS_CADASTRO - ONDE FICA TODOS OS CAMPOS
    #-----------------------------------------------
    telefio_cadastro.place(y=70,height=480,width=750)
    #-----------------------------------------------
    #Imagem SMS CADASTRO
    l_cada_sms.place(x=218,y=40)

    texto_sms_cadastro_fundo.place(x=298,y=60)
    #TEXTO DO CAMPO
    #-----------------------------------------------
    texto_sms_cadastro.place(x=130,y=170)
    
    texto_sms_status_cadastro.place(x=325,y=350)
    #-----------------------------------------------
    #CAMPO
    #-----------------------------------------------
    codi_sms_cadastro.place(x=200,y=170,height=27)

    #-----------------------------------------------
    #BOTAO
    #-----------------------------------------------
    botao_verificar_sms__cadastro.place(x=515,y=168)


    botao_enviar_sms_cadastro.place(x=312,y=250)

    #-----------------------------------------------
    #LINHA
    #-----------------------------------------------
    #Criando uma linha horizontal
    linha_sms_cadastro.place(x=85,y=310, width=570)

    #-----------------------------------------------
    #CARREGAMENTO SMS_CADASTRO
    bar2.place(x=280,y=400)
    bar2['value'] = 70
    #-----------------------------------------------



#-----------------------------------------------
#FRAME CONFIRMAR SMS - FRAME SE-1
#-----------------------------------------------
#FRAME PAGINA CONFIRMAR SMS - CONFIRMAR SMS ENVIADO - FRAME SE-1
#-----------------------------------------------
def con_sms():
            root.bind('<Return>', verificar_sms)
            #-----------------------------------------------
            #REMOVE FRAME PAGINA NOVA_SENHA
            #-----------------------------------------------
            fundo_nova_senha.place_forget()  
            textofundo_nova_senha.place_forget()
            principal_nova_senha.place_forget()
            texto_nova_senha.place_forget()
            texto2_nova_senha.place_forget()
            codi_nova_senha.place_forget()
            codi2_nova_senha.place_forget()
            botao_verificar_nova_senha.place_forget()
            linha_nova_senha.place_forget()
            texto_edit_texto_nova_senha.place_forget()
            #-----------------------------------------------
            #REMOVE PAGINA SENHA ESQUECIDA
            #-----------------------------------------------
            frame_fundo_senhaesquecida.place_forget()
            texto_fundo_senhaesquecida.place_forget()
            paginasenhaesquecida.place_forget()
            texto_senha_esquecida.place_forget()
            texto_email_senhaesquecida.place_forget()
            e_senha_esquecida.place_forget()
            e_email_senhaesquecida.place_forget()
            botao_senha_esquecida.place_forget()
            #-----------------------------------------------
            #CRIA O FRAME SMS
            #-----------------------------------------------
            #CRIA A PAGINA SMS
            #-----------------------------------------------
            #FUNDO DO TITULO
            #-----------------------------------------------
            titulo.place(height=70,width=750)
            #TEXTO DO FUNDO
            texto_fundo_sms.place(x=200,y=10)
            #FRAME DOS CAMPOS
            telefio.place(y=70,height=480,width=750)
            #IMAGEM SMS
            l_sms.place(x=218,y=40)
            #TEXTO DO CAMPO
            texto_sms.place(x=130,y=170)
            texto_sms_fundo.place(x=298,y=60)
            texto_sms_status.place(x=325,y=350)

            #CAMPO CODIGO
            codi_sms.place(x=200,y=170,height=27)
            #BOTAO
            botao_verificar.place(x=515,y=168) #EXECUTA A FUNCAO SMS-1, SE CORRETO, ABRE A PAGINA NOVA SENHA
           
            botao_enviar.place(x=312,y=250)

            #Criando uma linha horizontal
            linha.place(x=85,y=310, width=570)
            #cria o carregamento
            #-----------------------------------------------
            #CARREGAMENTO SMS
            bar.place(x=280,y=400)
            bar['value'] = 50
            #-----------------------------------------------




#-----------------------------------------------
#FRAME JANELA ONDE TERA NOVA SENHA PARA COLOCAR FRAME SE-2
#-----------------------------------------------
def nova_senha():
            root.bind('<Return>', mudar_senha)
            texto_novasenha_status['text'] = "Só mudar a senha!"
            #-----------------------------------------------
            #REMOVE O FRAME SMS
            #-----------------------------------------------
            titulo.place_forget()
            texto_fundo_sms.place_forget()
            telefio.place_forget()
            texto_sms.place_forget()
            codi_sms.place_forget()
            botao_verificar.place_forget()
            botao_enviar.place_forget()
            linha.place_forget()
            #-----------------------------------------------
            #-----------------------------------------------
            #REMOVE PAGINA SENHA ESQUECIDA
            #-----------------------------------------------
            frame_fundo_senhaesquecida.place_forget()
            texto_fundo_senhaesquecida.place_forget()
            paginasenhaesquecida.place_forget()
            texto_senha_esquecida.place_forget()
            texto_email_senhaesquecida.place_forget()
            e_senha_esquecida.place_forget()
            e_email_senhaesquecida.place_forget()
            botao_senha_esquecida.place_forget()
            #-----------------------------------------------
            #-----------------------------------------------
            #FRAME PAGINA NOVA_SENHA
            #-----------------------------------------------
            #FUNDO TITULO NOVA_SENHA
            #-----------------------------------------------
            fundo_nova_senha.place(height=70,width=750)
            #-----------------------------------------------
            #TEXTO PARA O FUNDO
            #-----------------------------------------------
            textofundo_nova_senha.place(x=260,y=10)
            #-----------------------------------------------
            #FRAME 2 PAGINA NOVA_SENHA - ONDE FICA TODOS OS CAMPOS
            #-----------------------------------------------
            principal_nova_senha.place(y=70,height=480,width=750)
            #-----------------------------------------------
            #IMAGEM EDITARSENHA
            l_editpass.place(x=210,y=10)
            texto_edit_texto_nova_senha.place(x=285,y=24)
            #TEXTO DO CAMPO
            #-----------------------------------------------
            texto_nova_senha.place(x=331,y=100)
            texto2_nova_senha.place(x=325,y=180)
            texto_novasenha_status.place(x=287,y=375)

            #-----------------------------------------------
            #CAMPO
            #-----------------------------------------------
            codi_nova_senha.place(x=229,y=130,height=27)
            codi2_nova_senha.place(x=229,y=210,height=27)

            #-----------------------------------------------
            #BOTAO
            #-----------------------------------------------
            botao_verificar_nova_senha.place(x=235,y=270) # FUNC-1 (EXECUTA A FUNCAO EM QUE TROCA A SENHA NO BANCO DE DADOS)

            #LINHA
            #-----------------------------------------------
            #Criando uma linha horizontal
            linha_nova_senha.place(x=85,y=350, width=570)

            #-----------------------------------------------
            #CARREGAMENTO NOVA SENHA
            bar1.place(x=280,y=425)
            bar1['value'] = 88
            #-----------------------------------------------




#-----------------------------------------------
#FUNCOES DO PROGRAMA
#-----------------------------------------------
#-----------------------------------------------
#FUNCAO DA PAGINA CONFIRMAR CONTA FRAME SE-0, VERIFICA SE A CONTA TEM CPF E E-MAIL CORRETO FUNC-0
#-----------------------------------------------
#PAGINA CONFIRMAR CONTA
#-----------------------------------------------
def confirmar_user_senha(event=None):
    global teste22, cpf_nova
    cpf_nova = e_senha_esquecida.get()
    if (e_senha_esquecida.get()=="" or e_email_senhaesquecida.get()==""):
        MessageBox.showinfo("Status", "Todos os campos são requeridos")
    else:
        #-------------------------------------------------------------------
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
        cursor = con.cursor()
        #-------------------------------------------------------------------
        try:
            cursor.execute("select cpf,telefone from cliente where cpf  = '"+ e_senha_esquecida.get() +"' and email = '"+ e_email_senhaesquecida.get() +"'")
            teste22 = cursor.fetchall()
            con.close();
            #SE CPF DIGITADO É IGUAL A DO CPF DO BANCO DE DADOS
            if e_senha_esquecida.get() == (f"{teste22[0][0]}"):
            
               
               #-----------------------------------------------
               #EXECUTA ENVIAR CODIGO SMS - SMS-0
               #-----------------------------------------------
               enviar_codigo_senha()
               #-----------------------------------------------
               #EXECUTA PAGINA CONFIRMAR SMS FRAME SE-1
               #-----------------------------------------------
               con_sms()
               #-----------------------------------------------


        except:
            MessageBox.showinfo("Status", "Usúario Não encontrado ou Inválido")
        
        #APAGA CAMPOS DA PAGINA SENHA ESQUECIDA
        e_senha_esquecida.delete(0, 'end')
        e_email_senhaesquecida.delete(0, 'end')

#-----------------------------------------------
#-----------------------------------------------
#FUNCAO DA PAGINA (FRAME) CADASTRO - ARRUMAR
#-----------------------------------------------
def fazer_cadastro(event=None):

    global x, codi ,nome ,cpf, email,telefone, usuario, senha
    #-------------------------------------------------------------------
    #Variaveis que irão receber o texto dentro da caixa de texto com o método get
    nome = e_nome.get()
    cpf = e_cpf.get()
    email = e_email.get()
    telefone = e_telefone.get()
    usuario = e_usuario.get()
    senha = e_cria_senha.get()
    #-------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------
    #Se todos os campos estiverem Vazios, não ira continuar até ter todos os campos preenchidos
    #Senão ele irá processeguir com a conexão com o banco de dados
    if(e_nome.get() =="" or e_cpf.get()=="" or  e_email.get()=="" or  e_telefone.get()=="" or  e_usuario.get()=="" or  e_cria_senha.get()==""):
        MessageBox.showinfo("Status", "Todos os campos são requeridos")
    else:
        #-------------------------------------------------------------------
        #Conexão e Entrada de dados no banco
        con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
        cursor = con.cursor()
        #-------------------------------------------------------------------
        #Decisão se o usuario é cadastrado ou não, se não for ele procede com a inserção no banco de dados
        try:
          cursor.execute("select cpf from cliente where cpf  = '"+ e_cpf.get() +"'")
          teste22 = cursor.fetchall()
          
          if e_cpf.get() == (f"{teste22[0][0]}"):
              e_cpf.delete(0, 'end')
              MessageBox.showinfo("Status", "Usúario Já cadastrado")
              con.close();
        except:
            try:
              con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
              cursor = con.cursor()
              cursor.execute("select nome from login where nome  = '"+ e_usuario.get() +"'")
              user_banco = cursor.fetchall()
          
              if e_usuario.get() == (f"{user_banco[0][0]}"):
                 e_usuario.delete(0, 'end')
                 MessageBox.showinfo("Status", "Esse nome de Usúario já está registrado")
                 con.close();
            except:

                
                #Sms#
                enviar_codigo()
                #Sms#
                #Sms#
            
                #FAZER O FRAME SMS_CADASTRO, ONDE ABRE A PAGINA PARA CONFIRMAR SMS DO CADASTRO
                sms_cadastro()

#FUNCAO SMS_CADASTRO_CONFIRMMAR
def enviar_codigo():
            global x 
                #SMS#
            import random

            x = random.randrange(10000,99999)

            print(x)

            codi = "+55"
            opcaonumero = e_telefone.get()
            opcaonumero = codi + opcaonumero

            #COLOCAR DADOS DA CONTA TWILIO
            from twilio.rest import Client
            account_sid ="AC79f6343a2745931d2f9ceb614cd41488"
            auth_token = "ab6e466e7a404a2f79188235b2f12d2f"
            meu_numero = opcaonumero
            numero_twilio = "+19312403449"

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure

            client = Client(account_sid, auth_token)


            message = client.messages \
                    .create(
                        body=f'''
                        {x}
                        ''',
                        from_=numero_twilio,
                        to=opcaonumero
                 )

            print(message.sid)        
#-----------------------------------------------
#FUNCAO EM QUE ENVIA O CODIGO SMS PARA O CELULAR DA CONTA CONFIRMADA - SMS-0
#-----------------------------------------------
def enviar_codigo_senha():
            global x 
            #SMS#
            import random

            x = random.randrange(10000,99999)

            print(x)

            codi = "+55"
            opcaonumero = (f"{teste22[0][1]}")
            opcaonumero = codi + opcaonumero

            
            #COLOCAR DADOS DA CONTA TWILIO
            from twilio.rest import Client
            account_sid ="AC79f6343a2745931d2f9ceb614cd41488"
            auth_token = "ab6e466e7a404a2f79188235b2f12d2f"
            meu_numero = opcaonumero
            numero_twilio = "+19312403449"

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure

            client = Client(account_sid, auth_token)


            message = client.messages \
                    .create(
                        body=f'''
                        {x}
                        ''',
                        from_=numero_twilio,
                        to=opcaonumero
                 )

            print(message.sid)  
#VENDO JUNTO COM SMS_CADASTRO
def verificar(event=None):
    x2 = str(x)
    codi2 = codi_sms_cadastro.get()
    print(x2)
    if (codi_sms_cadastro.get()==""):

        MessageBox.showinfo("Status", "Campo Vazio")
     
    else:
        if codi2 == x2:
            #--------------------------------
            #FAZ O CADASTRO E JA SALVA O REGISTRO LOGIN TAMBEM
            #--------------------------------
            #-------------------------------------------------------------------
            #Conexão e Entrada de dados no banco
            con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
            cursor = con.cursor()
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #Comando mysql parar inserir um cadastro novo caso não seja um já registrado
            cursor.execute("insert into cliente values(default,'"+ cpf + "','"+ nome + "','"+ email + "','"+ telefone + "')")
            cursor.execute("commit");

            #Comando mysql parar inserir um cadastro novo caso não seja um já registrado
            cursor.execute("insert into login values(default,'"+ cpf + "','"+ usuario + "','"+ senha + "')")
            cursor.execute("commit");
            con.close();
            #-------------------------------------------------------------------
            #Após confirmar, apaga as linhas
            e_nome.delete(0, 'end')
            e_cpf.delete(0, 'end')
            e_email.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_usuario.delete(0, 'end')
            #e_senha.delete(0, 'end')
            e_cria_senha.delete(0, 'end')
            contagem()
            #-------------------------------------------------------------------
            #Janela, Inserido com sucesso
            texto_sms_status_cadastro['text'] = "Concluído!"
            bar2['value'] = 100
            MessageBox.showinfo("Status", "Inserido Com Sucesso!")
            inicio()
            #-------------------------------------------------------------------
        else:
             MessageBox.showinfo("Status", "Código Inválido!")


    codi_sms_cadastro.delete(0, 'end')


#-------------------------------------------------------------------
#FUNCAO EM QUE VERIFICA O SMS ENVIADO DA SEQUENCIA SENHA ESQUECIDA COM O CODIGO DO CELULAR - SMS-1
#-------------------------------------------------------------------
def verificar_sms(event=None):
    x2 = str(x)
    codi7 = codi_sms.get()
    
    if (codi_sms.get()==""):

        MessageBox.showinfo("Status", "Campo Vazio")
     
    else:
        if codi7 == x2:
             #--------------------------------
             #ABRE A PAGINA NOVA SENHA
             #--------------------------------
             nova_senha()  #FRAME SE-2
             #--------------------------------
        else:
             MessageBox.showinfo("Status", "Código Inválido!")


    codi_sms.delete(0, 'end')


#-------------------------------------------------------------------
#FUNCAO QUE ALTERA A SENHA DA CONTA CONFIRMADA POR SMS - FUNC-1
#-------------------------------------------------------------------
def mudar_senha(event=None):
 
            if (codi_nova_senha.get()=="" or codi2_nova_senha.get()==""):
                MessageBox.showinfo("Status", "Campos Vazios!")
            else:
                if codi_nova_senha.get() != codi2_nova_senha.get():
                    MessageBox.showinfo("Status", "As senhas não são iguais!")
                    codi_nova_senha.delete(0, 'end')
                    codi2_nova_senha.delete(0, 'end')
                
                else:
                    cpf_nova1 = cpf_nova

                    senha_nova_esq = codi_nova_senha.get()
        
                    #-------------------------------------------------------------------
                    #Conexão e Entrada de dados no banco
                    con = mysql.connect(host="localhost", user="root", password="", database="projeto_login")
                    cursor = con.cursor()
                    #-------------------------------------------------------------------
                    #-------------------------------------------------------------------
                    #Comando mysql parar inserir um cadastro novo caso não seja um já registrado
                    cursor.execute("update login set senha ='"+ senha_nova_esq + "' where id_cpf='"+ cpf_nova1 +"' ")
                    cursor.execute("commit");
                    con.close();

                    #Comando mysql parar inserir um cadastro novo caso não seja um já registrado
                    #cursor.execute("insert into login values(default,'"+ cpf + "','"+ usuario + "','"+ senha + "')")
                    #cursor.execute("commit");
                    #-------------------------------------------------------------------
                    #Após confirmar, apaga as linhas
                    codi_nova_senha.delete(0, 'end')
                    codi2_nova_senha.delete(0, 'end')
                
                
                    contagem()
                    texto_novasenha_status['text'] = "      Concluído!"
                    bar1['value'] = 100
                    #-------------------------------------------------------------------
                    #Janela,SENHA ALTERADA COM SUCESSO
                    MessageBox.showinfo("Status", "Senha Alterada Com Sucesso")
                    e_name.delete(0, 'end')
                    #VOLTA PARA INICIO
                    inicio()
                    #-------------------------------------------------------------------
            


#-------------------------------------------------------------------


start()