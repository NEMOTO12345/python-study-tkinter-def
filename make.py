import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tks

class Window(tk.Frame):#tk.Frameを継承
    def __init__(self,master,title='タイトル',geometry="300x300"):
        super().__init__(master)
        # tk.Frameの初期化メソッドをつかう
        self.master = master #root(tk.Tk())
        self.master.geometry(geometry)
        self.master.title(title)
    def Entry(self,width=None):
        if width != None:
            self.entry = tk.Entry(width=width)
            self.entry.pack()
    def Label(self,text=None):
        if text != None:
            self.label = tk.Label(text=text)
            self.label.pack()
    def Combo(self,list=None):
        if list != None:
            self.combo = ttk.Combobox(self.master, state='readonly')
            self.combo["values"] = (list)
            self.combo.pack()
    def Btn(self,text=None,event=None,def_name=None):
        if text != None:
            self.btn = tk.Button(text=text)
            self.btn.bind(event, def_name)
            self.btn.pack()
    def Scroll(self,widht=None,heght=None):
        if widht != None:
            self.scroll = tks.ScrolledText(width = widht,height=heght)
            self.scroll.pack()
    def Insert(self,entry=None,scroll=None):
        if entry != None:
            self.entry.insert(tk.END,entry)
        if scroll != None:
            self.scroll.insert(tk.END,scroll)

def main():
    root = tk.Tk()
    app = Window(root)#タイトル、配置(300x300)
    app.Entry(30)#横
    app.Insert(entry="10")#↑Entry()に必ず値を入れる。
    app.Entry(30)#横
    app.Insert(entry="10")
    app.Label()#ラベルの名前
    app.Combo()#リスト
    app.Btn()#テキスト、イベント、イベントの名前
    app.Scroll(10,5)#横、縦
    app.Insert(scroll="faffafa")#↑Scroll()に必ず値を入れる。
    app.mainloop()

if __name__ == "__main__":
    main()