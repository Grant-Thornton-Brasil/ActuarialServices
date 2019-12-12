from glob import glob
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Separator
import os
from web_ses import *
from threading import Thread
from QEValidations.validation import run_validations
from win10toast import ToastNotifier
import time
import sqlite3
from db import *
from excel_tools import Handler
from QEMaths.maths import maths
import shutil


class main_window:
    # GUI ITSELF
    def __init__(self):
        self.root = Tk()
        self.dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),"..")
        self.root.iconbitmap(default=self.dir+"\\GUI_res\\icon.ico")
        self.root.title("Grant Thornton Brasil - Serviços Atuariais")
        self.root.resizable(False, False)
        self.root.config(padx=3, pady=3)
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen
        self.root.geometry(
            f"717x498+{int(round(ws/7,0))}+{int(round(hs/17,0))}")
        self.design()
        self.positions()
        self.files_list = []
        self.ramos_list = []
        self.ramos_validated = False

    def design(self):
        # QE Types
        self.qe_frame = LabelFrame(self.root, text="QEs")
        self.qe_label1 = Label(self.qe_frame, text="Seguros:")
        self.qe_label2 = Label(self.qe_frame, text="Resseguros:")
        self.qe_label3 = Label(self.qe_frame, text="Capitalização:")
        self.qetype_var = IntVar()
        self.qe_rb_376 = Radiobutton(
            self.qe_frame, text="376", value=376, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_377 = Radiobutton(
            self.qe_frame, text="377", value=377, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_378 = Radiobutton(
            self.qe_frame, text="378", value=378, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.separator1 = Separator(self.qe_frame)
        self.qe_rb_404 = Radiobutton(
            self.qe_frame, text="404", value=404, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_405 = Radiobutton(
            self.qe_frame, text="405", value=405, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_406 = Radiobutton(
            self.qe_frame, text="406", value=406, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_407 = Radiobutton(
            self.qe_frame, text="407", value=407, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_408 = Radiobutton(
            self.qe_frame, text="408", value=408, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.qe_rb_409 = Radiobutton(
            self.qe_frame, text="409", value=409, variable=self.qetype_var,
            command = lambda: self.hide_show_up())
        self.separator2 = Separator(self.qe_frame)
        self.qe_rb_419 = Radiobutton(
            self.qe_frame, text="419", value=419, variable=self.qetype_var,
            command = lambda: self.hide_show_up(False))
        self.qe_rb_420 = Radiobutton(
            self.qe_frame, text="420", value=420, variable=self.qetype_var,
            command = lambda: self.hide_show_up(False))
        self.qe_rb_421 = Radiobutton(
            self.qe_frame, text="421", value=421, variable=self.qetype_var,
            command = lambda: self.hide_show_up(False))
        self.qe_rb_42x = Radiobutton(
            self.qe_frame, text="422 & 423", value=429, variable=self.qetype_var,
            command = lambda: self.hide_show_up(False))
        # ENTCODIGO % ANO BASE
        self.entcodyear_frame = LabelFrame(self.root, text="Validação SES")
        self.ent_label = Label(self.entcodyear_frame, text="ENTCODIGO: ")
        self.ent_entry = Entry(self.entcodyear_frame)
        self.year_label = Label(self.entcodyear_frame, text="Ano Base: ")
        self.year_spin = Spinbox(self.entcodyear_frame, from_=2010, to=2100)
        self.ent_vali_button = Button(
            self.entcodyear_frame, text="Validar\n&\nObter Ramos",
            height=3,
            width=10,
            command=lambda: self.make_thread(self.get_ramos).start())
        # PROCESSOS
        self.processo1_var = IntVar()
        self.processo2_var = IntVar()
        self.processo3_var = IntVar()
        self.processo4_var = IntVar()
        self.processos_frame = LabelFrame(self.root, text="Processos")
        self.processo1 = Checkbutton(
            self.processos_frame, text="Críticas", variable=self.processo1_var)
        self.processo2 = Checkbutton(
            self.processos_frame,
            text="Confronto ($)",
            variable=self.processo2_var)
        self.processo3 = Checkbutton(
            self.processos_frame,
            text="Críticas (Detalhamento)",
            variable=self.processo3_var,
            command=lambda: self.processo1_var.set(1))
        self.processo4 = Checkbutton(
            self.processos_frame,
            text="Exportar para CSV",
            variable=self.processo4_var)
        # RAMOS
        self.ramos_frame = LabelFrame(self.root, text="Ramos:")
        self.ramos_text = Text(
            self.ramos_frame,
            state=DISABLED,
            height=4,
            width=20,
            padx=2,
            pady=2)
        self.ramos_scroll = Scrollbar(
            self.ramos_frame, command=self.ramos_text.yview)
        # FIP
        self.search_image = PhotoImage(file=self.dir+"\\GUI_res\\search.png")
        self.fip_frame = LabelFrame(self.root, text="FIP - Arquivo Access (.mdb ou .accdb)")
        self.fip_label = Label(self.fip_frame, text="Caminho: ")
        self.fip_entry = Entry(self.fip_frame, state=DISABLED, width= 102,
                                  disabledbackground="white",
                                  disabledforeground="black")
        self.fip_serch_bt = Button(self.fip_frame, text="X",
                                      image=self.search_image,
                                      command=lambda: self.search("FIP"))
        # ARQUIVOS
        self.arquivos_frame = LabelFrame(self.root, text="Arquivos:")
        self.arquivos_text = Text(self.arquivos_frame, width=75, height=15,
                                  state=DISABLED)
        self.arquivos_scroll = Scrollbar(
            self.arquivos_frame, command=self.arquivos_text.yview)
        self.arquivos_insert_bt = Button(
            self.arquivos_frame, text="Importar TXTs", height=8,
            command=lambda: self.add_txt_file())
        self.arquivos_clear_bt = Button(self.arquivos_frame, text="Limpar",
                                        command=lambda: self.clear_arquivos())
        # OUTPUT
        self.output_frame = LabelFrame(self.root)
        self.output_label = Label(self.output_frame, text="Caminho: ")
        self.output_entry = Entry(self.output_frame, width=88, state=DISABLED,
                                  disabledbackground="white",
                                  disabledforeground="black")
        
        self.output_serch_bt = Button(self.output_frame, text="X",
                                      image=self.search_image,
                                      command=lambda: self.search("OUT"))
        self.output_execute_bt = Button(self.output_frame, text="EXECUTAR!",
                                        font=("TkDefaultFont", 10, "bold"),
                                        command=lambda:self.make_thread(self.validate).start() )

    def positions(self):
        # QE Types
        self.qe_frame.grid(row=0, column=0, rowspan=2, sticky=(W, N, S, E))
        self.qe_label1.grid(row=0, column=0, sticky=W)
        self.qe_rb_376.grid(row=0, column=1)
        self.qe_rb_377.grid(row=0, column=2)
        self.qe_rb_378.grid(row=0, column=3)
        self.separator1.grid(row=1, columnspan=4, sticky=(W, E))
        self.qe_label2.grid(row=2, column=0, rowspan=2, sticky=W)
        self.qe_rb_404.grid(row=2, column=1)
        self.qe_rb_405.grid(row=2, column=2)
        self.qe_rb_406.grid(row=2, column=3)
        self.qe_rb_407.grid(row=3, column=1)
        self.qe_rb_408.grid(row=3, column=2)
        self.qe_rb_409.grid(row=3, column=3)
        self.separator2.grid(row=4, columnspan=4, sticky=(W, E))
        self.qe_label3.grid(row=5, column=0, rowspan=2, sticky=W)
        self.qe_rb_419.grid(row=5, column=1)
        self.qe_rb_420.grid(row=5, column=2)
        self.qe_rb_421.grid(row=5, column=3)
        self.qe_rb_42x.grid(row=6, column=1,columnspan=2,sticky=W)
        # ENTCODIGO % ANO BASE
        self.entcodyear_frame.grid(row=0, column=1, sticky=(W, N, S, E))
        self.ent_label.grid(row=0, column=0, sticky=W)
        self.ent_entry.grid(row=0, column=1, sticky=(W, E))
        self.year_label.grid(row=1, column=0, sticky=W)
        self.year_spin.grid(row=1, column=1, sticky=W)
        self.ent_vali_button.grid(
            row=0, column=2, rowspan=2, sticky=(W, N, E, S), padx=2)
        # PROCESSOS
        self.processos_frame.grid(row=1, column=1, sticky=(W, N, S, E))
        self.processo1.grid(row=0, column=0, sticky=W)
        self.processo2.grid(row=0, column=1, sticky=W)
        self.processo3.grid(row=1, column=0, sticky=W)
        self.processo4.grid(row=1, column=1, sticky=W)
        # RAMOS
        self.ramos_frame.grid(row=0, column=2, rowspan=2, sticky=(W, N, S, E))
        self.ramos_text.pack(fill=BOTH, side=LEFT)
        self.ramos_scroll.pack(fill=BOTH, side=LEFT)
        self.ramos_text.config(yscrollcommand=self.ramos_scroll.set)
        # FIP DB
        self.fip_frame.grid(
            row=2, column=0, columnspan=3,
            sticky=(W, N, S, E))
        self.fip_label.pack(side=LEFT)
        self.fip_entry.pack(side=LEFT,fill=BOTH)
        self.fip_serch_bt.pack(side=LEFT)
        # ARQUIVOS
        self.arquivos_frame.grid(
            row=3, column=0, columnspan=3,
            sticky=(W, N, S, E))
        self.arquivos_text.grid(row=0, column=0, rowspan=2)
        self.arquivos_scroll.grid(
            row=0, column=1, rowspan=2,
            sticky=(W, N, S, E))
        self.arquivos_text.config(yscrollcommand=self.arquivos_scroll.set)
        self.arquivos_insert_bt.grid(row=0, column=2, sticky=(W, N, S, E))
        self.arquivos_clear_bt.grid(row=1, column=2, sticky=(W, N, S, E))
        # OUTPUT
        self.output_frame.grid(
            row=4,
            column=0,
            sticky=(W, N, S, E),
            columnspan=3)
        self.output_label.pack(side=LEFT, fill=X)
        self.output_entry.pack(side=LEFT, fill=BOTH)
        self.output_serch_bt.pack(side=LEFT, fill=BOTH)
        self.output_execute_bt.pack(side=RIGHT, fill=BOTH)

    # CORE FUNCTIONS (COMMANDS)
    def hide_show_up(self, desire=True):
        if desire == False:
            self.ent_vali_button.config(state=DISABLED)
        else:
            self.ent_vali_button.config(state=NORMAL)
        
    def make_thread(self,command):
        return Thread(target=command)

    def validate(self):
        if self.processo1_var.get()+self.processo2_var.get() + \
            self.processo3_var.get()+self.processo4_var.get()==0:
                messagebox.showerror("Erro!",
                "Favor selecionar ao menos um processo!")
                return
        if self.qetype_var.get() == 0 or \
            self.ent_entry.get() == "" or \
                not (2010 <= int(self.year_spin.get())<=2100) or \
                    not self.ramos_validated:
            messagebox.showerror("Erro!","Favor validar o ENTCODIGO " \
                "para obter os ramos!")
            return
        if self.processo3_var.get() == 1 and \
            self.processo1_var.get() == 0:
            messagebox.showerror("Erro!",
                "Para extrair o relatório de críticas detalhado é necessário"\
                    ' selecionar o caixa "críticas" também!')
            return
        if len(self.files_list ) == 0:
            messagebox.showerror("Erro!","Adicione ao menos um arquivo TXT!")
            return
        if len(self.output_entry.get()) ==0:
            messagebox.showerror("Erro!", "É necessário "\
                "escolher um caminho para exportação!")
            return
        if os.path.exists(
            os.path.abspath(self.output_entry.get()+"\\Output")):
            messagebox.showerror("Erro!",
                "Já existe uma pasta OUTPUT nesse diretório.\n"
                "Apague ou renomeia para outro nome.")
            return
        try:
            self.execute()
        except KeyError:
            messagebox.showerror("Erro!",
            "A Ano Base não condiz com as datas do(s) arquivo(s)!\n"
            "Favor verificar...")
            self.conn.close()
            shutil.rmtree(
                os.path.abspath(
                    os.path.join(
                        self.output_entry.get(),"Output")))
            self.clear_form()
            self.output_execute_bt.config(state=NORMAL)
        if self.processo2_var.get() == 1 and self.fip_entry.get() == "":
            messagebox.showerror("Erro!",
            "Selecione um arquivo de banco de dados do FIP!")
            
    def search(self,func):
        if func == "OUT":
            path = filedialog.askdirectory()
            self.output_entry.config(state=NORMAL)
            self.output_entry.delete(0, END)
            self.output_entry.insert(0, path)
            self.output_entry.config(state=DISABLED)
        elif func == "FIP":
            path = filedialog.askopenfilename(filetypes=[("Arquivo de Access","*.mdb;*.accdb")])
            self.fip_entry.config(state=NORMAL)
            self.fip_entry.delete(0, END)
            self.fip_entry.insert(0, path)
            self.fip_entry.config(state=DISABLED)

    def add_txt_file(self):
        self.arquivos_text.config(state=NORMAL)
        for arquivo in filedialog.askopenfilenames(filetypes=[("Arquivos de Texto","*.txt")]):
            self.files_list.append(os.path.abspath(arquivo))
            self.arquivos_text.insert(END, str(len(self.files_list)) + "\n")
            self.arquivos_text.insert(END, arquivo + "\n")
            self.arquivos_text.insert(END, "-" * 75 + "\n")
        self.arquivos_text.config(state=DISABLED)

    def clear_arquivos(self):
        self.arquivos_text.config(state=NORMAL)
        self.files_list = []
        self.arquivos_text.delete("1.0", END)
        self.arquivos_text.config(state=DISABLED)

    def get_ramos(self):
        # Validação
        if self.qetype_var.get() == 0:
            messagebox.showerror("Error!",
                "Selecione um QE!")
            return
        if self.ent_entry.get()=="" or len(self.ent_entry.get())==0:
            messagebox.showerror("Erro!", "Digite um ENTCODIGO válido!")
            return
        try:
            if not 2010<=int(self.year_spin.get())<2100:
                messagebox.showerror("Erro!", "Digite um ano base válido!")
                return
        except:
            messagebox.showerror("Erro!", "Digite um ano base válido!")
            return
        # Format Button
        self.ent_vali_button.config(state=DISABLED,text="Consultando\n SES...")
        # SES
        self.ramos_list = get_ramos(self.ent_entry.get(),
                  self.year_spin.get(),
                  self.qetype_var.get())
        if not self.ramos_list:
            messagebox.showerror("Erro!", "Impossível acessar o SES SUSEP." \
                                 "\n\nVerifique sua conexão!")
            self.ent_vali_button.config(state=NORMAL, 
                                        text="Validar\n&\nObter Ramos")
            return
        self.ramos_text.config(state=NORMAL)
        self.ramos_text.delete("1.0",END)
        for ramo in self.ramos_list:
            self.ramos_text.insert(END,ramo+"\n")
        self.ramos_text.config(state=DISABLED)
        # Reset Button
        self.ent_vali_button.config(state=NORMAL, 
                                        text="Validar\n&\nObter Ramos")
        self.ramos_validated = True

    def execute(self):
        self.output_execute_bt.config(state=DISABLED)
        self.root.wm_state('iconic')
        notifier=ToastNotifier()
        # Vars
        start = time.time()
        qe = self.qetype_var.get()
        year = int(self.year_spin.get())
        entcodigo = self.ent_entry.get()
        esrcodcess = get_esrcodcess()
        esrcodcess.append(entcodigo)
        path = os.path.abspath(self.output_entry.get())
        # Crate new folder
        os.mkdir(path+f"\\Output_{entcodigo}_{qe}_{year}")
        path = os.path.abspath(os.path.join(path,f"Output_{entcodigo}_{qe}_{year}"))
        total = 0
        # Connection
        db_path = path+"\\"+str(len(glob(path+"\\*.db"))+1)+".db"
        self.conn = sqlite3.connect(db_path)
        # Prepare DB Tables
        create_main_tables(self.conn)
        # Prepare Excel File
        excel = Handler(qe)
        # Ok, Lets finally process these fuckers
        if self.processo1_var.get() ==1:
            # CRITICAS
            for arquivo in self.files_list:                   
                with open(arquivo, encoding="utf-8-sig") as txt:
                    linhas = txt.readlines()
                    total += len(linhas)
                    for n, linha in enumerate(linhas,1):
                        run_validations(
                            qe=qe,
                            nome_arquivo = txt.name,
                            linha=linha.replace(",",".").strip(),
                            n=n,
                            conn=self.conn,
                            year = year,
                            entcodigo = entcodigo,
                            ramcodigos = self.ramos_list,
                            esrcodcess = esrcodcess,
                            gracodigos = self.ramos_list)
            self.conn.commit()
            # Export Excel
            excel.critics_to_excel(self.conn,total)
        if self.processo2_var.get()== 1:
            # CRUZAMENTOS
            calculator = maths(year,qe)
            for file in self.files_list:
                with open(file, encoding="utf-8-sig") as txt:
                    for line in txt.readlines():
                        try:
                            calculator.score_line(line.replace(",",".").strip())
                        except:
                            pass
            df = calculator.get_dataframe()
            excel.df_to_excel(df,qe,os.path.abspath(self.fip_entry.get()),year,entcodigo)
            excel.conn.close()
        if self.processo3_var.get()==1:
            make_report(qe,self.conn,path)
        if self.processo4_var.get()==1:
            excel.qe_to_csv(qe,path,self.files_list)
        notifier.show_toast(
            title="Processo Finalizado!",
            msg="Executado em {}".format(round(time.time()-start,2)),
            icon_path=self.dir+"\\GUI_res\\icon.ico",
            threaded=True)
        self.output_execute_bt.config(state=NORMAL)
        self.root.wm_state("normal")
        # Save Excel
        if self.processo1_var.get() == 1 or \
            self.processo2_var.get() == 1:
            excel.save_xl(path)
        # Clear form & Delete DB
        # self.clear_form()
        self.conn.close()
        os.remove(db_path)

    def clear_form(self):
        self.qetype_var.set(0)
        self.ent_entry.delete(0,END)
        self.ramos_text.config(state=NORMAL)
        self.ramos_text.delete("1.0",END)
        self.ramos_text.config(state=DISABLED)
        self.ramos_list = []
        self.clear_arquivos()
        self.output_entry.config(state=NORMAL)
        self.output_entry.delete(0,END)
        self.output_entry.config(state=DISABLED)
        self.clear_arquivos()
        self.processo1_var.set(0)
        self.processo2_var.set(0)
        self.processo3_var.set(0)
        self.processo4_var.set(0)
        self.fip_entry.config(state=NORMAL)
        self.fip_entry.delete(0,END)
        self.fip_entry.config(state=DISABLED)

        
if __name__ == "__main__":
    a = main_window()
    a.root.mainloop()