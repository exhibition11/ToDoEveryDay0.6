import tkinter as tk

# メインメニューの表示


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("雛形")

        global todolist
        try:
            self.disptodolist = tk.Label(text=todolist)
            self.disptodolist.pack()
        except:
            todolist = []
            self.disptodolist = tk.Label(text="設定されたものはありません")
            self.disptodolist.pack()

        sbtn = tk.Button(text="出来た！", command=Success)
        sbtn.pack()
        # 一つでもダメだったら出来なかった
        fbtn = tk.Button(text="出来なかった...", command=Failure)
        fbtn.pack()
        itodo = tk.Button(text="明日やることの設定", command=SetToDo)
        itodo.pack()

        dbtn = tk.Button(text="debag", command=self.a)
        dbtn.pack()

    def a(self):
        global todolist
        print(todolist)


class Success:
    def __init__(self):
        self.sub = tk.Toplevel(root)

        self.sub.geometry("300x300")
        self.sub.title("達成")

        # 賞賛演出
        dummy1 = tk.Label(self.sub, text="Conglatilation!!")
        dummy1.pack()

        # 連続成功記録の表示

        slabel1 = tk.Label(self.sub, text="コメント")
        slabel1.pack()
        comment = tk.Entry(self.sub)
        comment.pack()
        bln = tk.BooleanVar()
        bln.set(False)
        sflag = tk.Checkbutton(self.sub, variable=bln, text="思い出に残る成功？")
        sflag.pack()

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()


class Failure:
    def __init__(self):
        self.sub = tk.Toplevel(root)

        self.sub.geometry("300x300")
        self.sub.title("失敗")

        # todolist一つ一つにチェックボックスを付けて表示
        flabel1 = tk.Label(self.sub, text="出来なかった理由")
        flabel1.pack()
        # 出来なかった理由の主なものはチェックボックス表示
        comment = tk.Entry(self.sub)
        comment.pack()
        bln = tk.BooleanVar()
        bln.set(False)
        fflag = tk.Checkbutton(self.sub, variable=bln, text="思い出に残る失敗？")
        fflag.pack()

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()

class SetToDo:
    def __init__(self):
        self.sub = tk.Toplevel(root)

        self.sub.geometry("300x300")
        self.sub.title("明日することの設定")

        # なぜか上手くいかず、要検討
        self.todo1 = tk.Entry(self.sub)
        self.todo1.pack()
        self.todo2 = tk.Entry(self.sub)
        self.todo2.pack()
        self.todo3 = tk.Entry(self.sub)
        self.todo3.pack()
        self.todo4 = tk.Entry(self.sub)
        self.todo4.pack()
        self.todo5 = tk.Entry(self.sub)
        self.todo5.pack()

        savebtn = tk.Button(self.sub, text="設定完了！", command=self.SaveToDo)
        savebtn.pack()

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()

    def SaveToDo(self):
        global todolist
        for i in range(5):
            a = "self.todo" + str(i + 1) + ".get()"
            # 文字列をpythonの命令として読み込み、実行
            b = eval(a)
            print(b)
            todolist.append(str(b))

        # 途中の空要素の削除
        a = todolist
        todolist = [i for i in a if i != '']
        print(todolist)

        # windowを閉じる
        self.sub.destroy()




if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(master=root)
    app.mainloop()
