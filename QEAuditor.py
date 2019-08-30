import sqlite3
import time
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Treeview
from db import *
from QEValidations.validation import run_validations
from Web.ses import SES
from win10toast import ToastNotifier
import os
from QEMaths.maths import *
from export import qe_export
from datetime import datetime
import calendar
import threading
from glob import glob


class main_window():


    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap(default="icon.ico")
        self.root.title("Grant Thornton Brasil - Serviços Atuariais")
        self.root.resizable(False, False)
        self.root.config(padx=3, pady=3)
        self.design()
        self.positions()
        self.active_list = []

        
    def design(self):
        # Big Frame 1 - Esquerda
        self.left_frame = Frame(self.root)
        # Entcodigo
        self.entcodigo_frame = LabelFrame(self.left_frame,
                                          text="Código SUSEP - ENTCODIGO:")
        self.entcodigo_entry = Entry(self.entcodigo_frame)
        self.entcodigo_button = Button(
            self.entcodigo_frame,
            text="Validar e obter ramos",
            command=lambda: self.get_ramos_thread())
        # Ano
        self.year_frame = LabelFrame(self.left_frame,
                                     text="Período")
        self.year_label = Label(self.year_frame,
                                text="Ano Base:")
        self.year_spinbox = Spinbox(self.year_frame,
                                    from_=2010,
                                    to=2100)
        self.year_spinbox.delete(0, "end")
        # Ramos
        self.ramos_frame = LabelFrame(self.left_frame,
                                      text="Ramos:")
        self.ramos_text = Text(self.ramos_frame,
                               width=23,
                               height=15,
                               state=DISABLED)
        self.ramos_scroll = Scrollbar(self.ramos_frame,
                                      command=self.ramos_text.yview)

        # Big Frame 2 - Direita
        self.right_frame = Frame(self.root)
        # QE Types
        self.qetype_frame = LabelFrame(self.right_frame,
                                       text="QE")
        self.qetype_label1 = Label(self.qetype_frame,
                                   text="Seguros:")
        self.qetype_label2 = Label(self.qetype_frame,
                                   text="Resseguros:")
        self.qetype_label3 = Label(self.qetype_frame,
                                   text="Capitalização:")
        # QE Types RBs
        self.qetype_var = IntVar()
        self.qetype_rb376 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="376",
                                        value=376)
        self.qetype_rb377 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="377",
                                        value=377)
        self.qetype_rb378 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="378",
                                        value=378)
        self.qetype_rb404 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="404",
                                        value=404)
        self.qetype_rb405 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="405",
                                        value=405)
        self.qetype_rb406 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="406",
                                        value=406)
        self.qetype_rb407 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="407",
                                        value=407)
        self.qetype_rb408 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="408",
                                        value=408)
        self.qetype_rb409 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="409",
                                        value=409)
        self.qetype_rb419 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="419",
                                        value=419)
        self.qetype_rb420 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="420",
                                        value=420)
        self.qetype_rb421 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="421",
                                        value=421)
        self.qetype_rb422 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="422",
                                        value=422)
        self.qetype_rb423 = Radiobutton(self.qetype_frame,
                                        variable=self.qetype_var,
                                        text="423",
                                        value=423)
        # Lista Arquivos
        self.arquivos_frame = LabelFrame(self.right_frame,
                                         text="Arquivos Importados")
        self.arquivos_text = Text(self.arquivos_frame,
                                  height=19,
                                  width=70,
                                  state=DISABLED)
        self.arquivos_button = Button(self.arquivos_frame,
                                      text="Importar TXTs",
                                      command=lambda: self.add_files(),
                                      height=13,
                                      width=12)
        self.arquivos_button_clear = Button(self.arquivos_frame,
                                            text="Limpar",
                                            command=lambda: self.clear_files(),
                                            height=6,
                                            width=12)
        self.arquivos_scroll = Scrollbar(self.arquivos_frame,
                                         command=self.arquivos_text.yview)
        # Processos
        self.processo1_var = IntVar()
        self.processo2_var = IntVar()
        self.processo3_var = IntVar()
        self.processo4_var = IntVar()
        self.processos_frame = LabelFrame(self.left_frame,
                                          text="Processos")
        self.processo1 = Checkbutton(self.processos_frame,
                                     text="Críticas",
                                     variable=self.processo1_var)
        self.processo2 = Checkbutton(self.processos_frame,
                                     text="Confronto ($)",
                                     variable=self.processo2_var)
        self.processo3 = Checkbutton(self.processos_frame,
                                     text="Críticas (Detalhamento)",
                                     variable=self.processo3_var,
                                     command=lambda: self.processo1_var.set(1))
        self.processo4 = Checkbutton(self.processos_frame,
                                     text="Exportar para CSV",
                                     variable=self.processo4_var)

        # Path Bars:
        self.path_bars_frame = LabelFrame(self.right_frame, text="Caminhos")
        self.path_detalhamento_label = Label(self.path_bars_frame,
                                             text="Criticas (Detalhamento)")
        self.path_detalhamento_entry = Entry(self.path_bars_frame,
                                             width=73)
        self.path_detalhamento_button = Button(self.path_bars_frame,
                                               text="Selecionar Pasta",
                                               command= lambda: self.get_folders(1))
        self.path_export_label = Label(self.path_bars_frame,
                                       text="Exportação CSVs")
        self.path_export_entry = Entry(self.path_bars_frame,
                                       width=73)
        self.path_export_button = Button(self.path_bars_frame,
                                         text="Selecionar Pasta",
                                               command= lambda: self.get_folders(2))

        # Tree Process
        self.process_tree_frame = Frame(self.root)
        self.process_tree = Treeview(self.process_tree_frame,
                                     height=3,
                                     columns=[i for i in range(1,3)])                       
        self.process_start = Button(
            self.process_tree_frame, height=4, text="EXECUTAR!",
            command=lambda: self.validate(),
            font=("TkDefaultFont",9,"bold"))
        self.process_end = Button(
            self.process_tree_frame, text="ABORTAR!", fg="red",
            font=("TkDefaultFont",8,"bold"),
            command=lambda: self.kill_process())
        self.process_scroll = Scrollbar(self.process_tree_frame,
                                        command=self.process_tree.yview)
        self.process_tree.heading("#0", text="#")
        self.process_tree.heading("#1", text="Processos")
        self.process_tree.heading("#2", text="Status")
        self.process_tree.column("#0",width=40)
        self.process_tree.column("#1", width=365)
        self.process_tree.column("#2", width=365)
    

    def positions(self):
        # Big Frame 1 - Esquerda
        self.left_frame.grid(row=0, column=0)
        # Entcodigo
        self.entcodigo_frame.pack(fill=X)
        self.entcodigo_entry.pack(fill=X)
        self.entcodigo_button.pack(fill=X)
        # Ano
        self.year_frame.pack(fill=X, ipady=3)
        self.year_label.grid(row=0, column=0)
        self.year_spinbox.grid(row=0, column=1)

        # Ramos
        self.ramos_frame.pack(fill=X)
        self.ramos_text.pack(side=LEFT)
        self.ramos_scroll.pack(side=LEFT, fill=Y)
        self.ramos_text.config(yscrollcommand=self.ramos_scroll.set)

        # Big Frame 2 - Direita
        self.right_frame.grid(row=0, column=1)
        self.qetype_frame.pack(fill=X)
        self.qetype_label1.grid(row=0, column=0, sticky=W)
        self.qetype_label2.grid(row=1, column=0, sticky=W)
        self.qetype_label3.grid(row=2, column=0, sticky=W)
        self.qetype_rb376.grid(row=0, column=1)
        self.qetype_rb377.grid(row=0, column=2)
        self.qetype_rb378.grid(row=0, column=3)
        self.qetype_rb404.grid(row=1, column=1)
        self.qetype_rb405.grid(row=1, column=2)
        self.qetype_rb406.grid(row=1, column=3)
        self.qetype_rb407.grid(row=1, column=4)
        self.qetype_rb408.grid(row=1, column=5)
        self.qetype_rb409.grid(row=1, column=6)
        self.qetype_rb419.grid(row=2, column=1)
        self.qetype_rb420.grid(row=2, column=2)
        self.qetype_rb421.grid(row=2, column=3)
        self.qetype_rb422.grid(row=2, column=4)
        self.qetype_rb423.grid(row=2, column=5)
        # Arquivos
        self.arquivos_frame.pack(fill=X)
        self.arquivos_text.grid(row=0, column=0)
        self.arquivos_scroll.grid(row=0, column=1, sticky=(N, W, E, S))
        self.arquivos_button.grid(row=0, column=2, sticky=N, columnspan=2)
        self.arquivos_button_clear.grid(
            row=0, column=2, sticky=S, columnspan=2)
        self.arquivos_text.config(yscrollcommand=self.arquivos_scroll.set)
        # Processos
        self.processos_frame.pack(fill=X, side=BOTTOM, anchor=S)
        self.processo1.grid(row=0, column=0, sticky=W)
        self.processo2.grid(row=1, column=0, sticky=W)
        self.processo3.grid(row=2, column=0, sticky=W)
        self.processo4.grid(row=3, column=0, sticky=W)

        # Path Bars
        self.path_bars_frame.pack(fill=X)
        self.path_detalhamento_label.grid(row=0, column=0, sticky=W)
        self.path_detalhamento_entry.grid(row=0, column=1)
        self.path_detalhamento_button.grid(row=0, column=2, padx=3)
        self.path_export_label.grid(row=1, column=0, sticky=W)
        self.path_export_entry.grid(row=1, column=1)
        self.path_export_button.grid(row=1, column=2)

        # Tree Process
        self.process_tree_frame.grid(
            row=1, column=0, columnspan=2, sticky=(W, E))
        self.process_tree.pack(side=LEFT, fill=BOTH)
        self.process_scroll.pack(side=LEFT, fill=BOTH)
        self.process_start.pack(fill=BOTH)
        self.process_end.pack(fill=BOTH)


    # COMMANDS
    def get_folders(self,process_type):
        if process_type == 1:
            self.path_detalhamento_entry.delete(0,END)
            self.path_detalhamento_entry.insert(0,string=filedialog.askdirectory())
        elif process_type == 2:
            self.path_export_entry.delete(0,END)
            self.path_export_entry.insert(0,string=filedialog.askdirectory())


    def get_ramos_thread(self):
        x= threading.Thread(target=self.validate_entcodigo)
        x.start()


    def validate_entcodigo(self):
        try:
            int(self.entcodigo_entry.get())
            if len(self.entcodigo_entry.get()) != 5:
                raise
            int(self.year_spinbox.get())
        except BaseException:
            messagebox.showerror(
                title="Erro",
                message="Verifique o ENTCODIGO e o ANO!\n\n"
                "ENTCODIGO -> (Inteiro e cinco digitos)"
            )
            return
        self.ramos_text.delete('1.0', END)
        self.entcodigo_button.config(
            text="Acessando SES...",
            state=DISABLED
        )
        ramos = SES()
        ramos = ramos.get_ramos(
            self.entcodigo_entry.get(),
            self.year_spinbox.get())
        if not ramos:
            messagebox.showerror(
                title="Erro",
                message="Impossível validar o ENTCODIGO e consultar os ramos.\n\n"
                "Verifique sua conexão...\n\n"
                "OBS: É possível imputar manualmente.")
            self.ramos_text.config(state=NORMAL)    
            return
        self.ramos_text.config(state=NORMAL)
        for ramo in ramos:
            self.ramos_text.insert(END, ramo + "\n")
        self.ramos_text.config(state=DISABLED)
        self.entcodigo_button.config(text="Validar e obter ramos",
            state=NORMAL)


    def validate(self):
        # ENTCODIGO
        if self.entcodigo_entry.get() == None or \
            self.entcodigo_entry.get() == "" or \
                len(self.entcodigo_entry.get())==0:
            messagebox.showerror(
                title="Erro",
                message="Insira um ENTCODIGO."
            )
            return
        # Year
        if self.year_spinbox.get()==0 or self.year_spinbox.get()==None or \
            self.year_spinbox.get()=="":
            messagebox.showerror(
                title="Erro",
                message="Insira um Ano Base."
            )
            return
        # Ramos
        try:
            if len(self.ramos_text.get("1.0",END).split("\n")[:-1]) == 1:
                raise
        except:
            messagebox.showerror(
                title="Erro",
                message="Preencha os ramos\n\n"\
                    "É possível preencher manualmente."
            )
            return
        # QE
        if self.qetype_var.get() == 0:
            messagebox.showerror(
                title="Erro",
                message="Selecione um Quadro Estatístico"
            )
            return
        # Processos
        if self.processo1_var.get() == 0 and \
            self.processo2_var.get() == 0 and \
                self.processo3_var.get() == 0 and \
                    self.processo4_var.get() == 0:
            messagebox.showerror(
                title="Erro",
                message="Selecione aom menos um processo.")
            return
        process = "QE "+str(self.qetype_var.get())+" - "
        if self.processo1_var.get() == 0:
            process += "Críticas, "
        if self.processo2_var.get() == 0:
            process += "Confrontos ($), "
        if self.processo3_var.get() == 0:
            process += "Críticas (Detalhamento), "
        if self.processo4_var.get() == 0:
            process += "Exportar para CSV."
        

        self.active_list.append(threading.Thread(target=self.run,args=[len(self.active_list)]))
        self.active_list[-1].start()
        self.process_tree.insert("",END,text=str(len(self.active_list)),
            values=(process,"Executando..."))


    def add_files(self):
        arquivos = filedialog.askopenfilenames()
        self.arquivos_text.config(state=NORMAL)
        for n, arquivo in enumerate(arquivos, 1):
            self.arquivos_text.insert(END, str(n) + "\n")
            self.arquivos_text.insert(END, arquivo + "\n")
            self.arquivos_text.insert(END, "-" * 70 + "\n")
        self.arquivos_text.config(state=DISABLED)


    def clear_files(self):
        self.arquivos_text.config(state=NORMAL)
        self.arquivos_text.delete("1.0", END)
        self.arquivos_text.config(state=DISABLED)


    def run(self,process_number):
        conn = sqlite3.connect(f"DBs\\{process_number}.db")
        start = time.time()
        processos = [self.processo1_var.get(), self.processo2_var.get(),
                     self.processo3_var.get(), self.processo4_var.get()]
        # Críticas
        if processos[0] == 1:
            qe = self.qetype_var.get()
            entcodigo = self.entcodigo_entry.get()
            ramcodigos = self.ramos_text.get("1.0", END).splitlines()[:-1]
            create_main_tables(conn)
            esrcodcess = ["38741", "30074", "34819", "36099", "37052",
                          "38253", "31623", "38873", "33294", "39764",
                          "37729", "31551", "38270", "30201", "34665", "32875", entcodigo]
            for arquivo in self.arquivos_text.get(
                    "1.0", END).splitlines()[:-1]:
                if arquivo != "-" * 70:
                    try:
                        with open(arquivo, "r") as txt:

                            linhas = txt.readlines()
                            for n, linha in enumerate(linhas, 1):
                                linha = linha.replace(",", ".").strip()
                                run_validations(
                                    qe=qe,
                                    nome_arquivo=txt.name,
                                    linha=linha,
                                    n=n,
                                    conn=conn,
                                    year=int(self.year_spinbox.get()),
                                    entcodigo=entcodigo,
                                    ramcodigos=ramcodigos,
                                    esrcodcess=esrcodcess)
                    except FileNotFoundError:
                        pass
            conn.commit()
        # Confrontos
        if processos[1] == 1:
            year = int(self.year_spinbox.get())
            dates_seguros = [datetime(year, month, calendar.monthrange(year, month)[1]).strftime("%Y%m%d") for month in range(1, 13)]
            dates_reseguros = [f"2018" + f"{month}".zfill(2) for month in range(1, 13)]
            m376 = maths_376(dates_seguros)
            m377 = maths_377(dates_seguros)
            m378 = maths_378(dates_seguros)
            m404 = maths_404(dates_reseguros)
            m405 = maths_405(dates_reseguros)
            m406 = maths_406(dates_reseguros)
            m407 = maths_407(dates_reseguros)
            m408 = maths_408(dates_reseguros)
            m409 = maths_408(dates_reseguros)
            qe = self.qetype_var.get()
            for arquivo in self.arquivos_text.get("1.0", END).splitlines()[:-1]:
                try:
                    with open(arquivo,"r") as txt:
                        linhas = txt.readlines()
                        for linha in linhas:
                            linha = linha.replace(",", ".").strip()
                            if qe == 376:
                                m376.run(linha)
                            elif qe == 377:
                                m377.run(linha)
                            elif qe == 376:
                                m378.run(linha)
                            elif qe == 404:
                                m404.run(linha)
                            elif qe == 405:
                                m405.run(linha)
                            elif qe == 406:
                                m406.run(linha)
                            elif qe == 407:
                                m407.run(linha)
                            elif qe == 408:
                                m408.run(linha)
                            elif qe == 409:
                                m409.run(linha)
                except FileNotFoundError:
                    pass
                except KeyError:
                    messagebox.showerror(
                        title="Erro",
                        message="As datas dos campos MRFMESANO não condizem com o ano base informado.\n\n"\
                            "Favor corrigir o ano base ou selecione novamente os arquivos!")
            folder = os.path.abspath(filedialog.askdirectory())
            if qe == 376:
                m376.df.to_excel(folder+"\\376.xlsx")
            elif qe == 377:
                m377.df.to_excel(folder+"\\377.xlsx")
            elif qe == 376:
                m378.df.to_excel(folder+"\\378.xlsx")
            elif qe == 404:
                m404.df.to_excel(folder+"\\404.xlsx")
            elif qe == 405:
                m405.df.to_excel(folder+"\\405.xlsx")
            elif qe == 406:
                m406.df.to_excel(folder+"\\406.xlsx")
            elif qe == 407:
                m407.df.to_excel(folder+"\\407.xlsx")
            elif qe == 408:
                m408.df.to_excel(folder+"\\408.xlsx")
            elif qe == 409:
                m409.df.to_excel(folder+"\\409.xlsx")
        if processos[2] == 1:
            path = os.path.abspath(filedialog.askdirectory())
            make_report(self.qetype_var.get(),conn,path)
        if processos[3] == 1:
            path = os.path.abspath(filedialog.askdirectory())
            qe_export(self.qetype_var.get(),path,self.arquivos_text.get("1.0",END).splitlines())
        end = time.time()
        notifier = ToastNotifier()
        notifier.show_toast(
            "Processo Finalizado com Sucesso!",
            f"O processo levou {round(end-start,2)} segundos",
            icon_path="icon.ico",
            threaded=True
        )


    def kill_process(self):
        print(int(self.process_tree.focus()[1:]))


if __name__ == "__main__":
    for db in glob("DBs\\*.db"):
        os.remove(db)
    a = main_window()
    a.root.mainloop()
