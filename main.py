import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime


# メインメニューの表示
class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("雛形")

        # path処理
        # 保存ディレクトリー場所、月、日、ディレクトリーpath,ファイルpath
        global source_path, dir_index, file_index, dir_path, file_path
        source_path = r"C:\\ToDoEveryDay"

        # 初回起動時、ディレクトリーがないなら作る
        if os.path.isdir(source_path) is False:
            os.mkdir(source_path)

        # time get
        a = datetime.now()
        dir_index = a.month
        file_index = a.day

        # each path setting
        dir_path = source_path + '\\' + str(dir_index) + '月'
        file_path = dir_path + '\\' + str(file_index) + '日.txt'

        # ここからガジェットの配置=================================
        # todolist（ファイル)があるなら表示
        flag = 0
        todolist = []
        try:
            with open(file_path) as f:
                todolist = [s.strip() for s in f.readlines()]
            flag = 1
        except:
            self.disptodolist = tk.Label(text="設定されたものはありません")
            self.disptodolist.pack()

        if flag == 1:
            line = '区分け'
            i = 0
            while True:
                print(todolist[i])
                if todolist[i] == line:
                    break
                i += 1

            for j in range(i):
                newlabel = tk.Label(text=todolist[j])
                newlabel.pack()


        sbtn = tk.Button(text="出来た！", command=Success)
        sbtn.pack()
        # 一つでもダメだったら出来なかった
        fbtn = tk.Button(text="出来なかった...", command=Failure)
        fbtn.pack()
        itodo = tk.Button(text="明日やることの設定", command=SetToDo)
        itodo.pack()


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
        self.comment = tk.Entry(self.sub)
        self.comment.pack()
        self.bln = tk.BooleanVar()
        self.bln.set(False)
        self.flag = tk.Checkbutton(self.sub, variable=self.bln, text="思い出に残る成功？")
        self.flag.pack()

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()
        savebtn = tk.Button(self.sub, text="セーブ", command=self.sdata_send)
        savebtn.pack()

    def sdata_send(self):
        a = self.comment.get()
        b = self.bln.get()
        c = 0
        ProcessStore().save_comment(a, b, c)
        self.sub.destroy()



class Failure:
    def __init__(self):
        self.sub = tk.Toplevel(root)

        self.sub.geometry("300x300")
        self.sub.title("失敗")


        # todolistにチェックボックスを付けて表示
        flabel1 = tk.Label(self.sub, text="コメント")
        flabel1.pack()
        self.comment = tk.Entry(self.sub)
        self.comment.pack()
        self.bln = tk.BooleanVar()
        self.bln.set(False)
        self.flag = tk.Checkbutton(self.sub, variable=self.bln, text="思い出に残る失敗？")
        self.flag.pack()

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()
        savebtn = tk.Button(self.sub, text="セーブ", command=self.fdata_send)
        savebtn.pack()

    def fdata_send(self):
        a = self.comment.get()
        b = self.bln.get()
        c = 1
        ProcessStore().save_comment(a, b, c)
        self.sub.destroy()


class SetToDo:
    def __init__(self):
        self.sub = tk.Toplevel(root)

        self.sub.geometry("300x300")
        self.sub.title("明日することの設定")


        # 変数に順番に数字をつけて、かつpack()するやり方がわからず、とりあえず保留
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

        exitbtn = tk.Button(self.sub, text="やっぱりやめる", command=self.sub.destroy)
        exitbtn.pack()

        savebtn = tk.Button(self.sub, text="設定完了！", command=self.todo_send)
        savebtn.pack()



    def todo_send(self):
        todolist = []
        for i in range(5):
            a = "self.todo" + str(i + 1) + ".get()"
            # 文字列をpythonの命令として読み込み、実行
            b = eval(a)
            todolist.append(str(b))

        # 途中の空要素の削除
        a = todolist
        todolist = [i for i in a if i != '']
        ProcessStore().save_todo(todolist)
        self.sub.destroy()

class ProcessStore:
    def save_todo(self, todolist):
        txt = todolist
        # txtに内容があるなら処理を続ける
        if len(txt) != 0:
            global source_path, dir_index, file_index, dir_path, file_path

            # create now month folder
            if os.path.isdir(dir_path) is False:
                os.mkdir(dir_path)

            # todoリストにクリアをかける（評価などが書いてあっても消去）
            # 最悪ファイルを直接編集（コア機能の開発優先）
            try:
                os.remove(file_path)
            except:
                pass

            for i in range(len(todolist)):
                # write file
                with open(file_path, mode='a') as f:
                    f.write(txt[i] + '\n')

            with open(file_path, mode='a') as f:
                # todoと評価の区分け線
                f.write('区分け' + '\n')

    # todoリストが作ってあることが前提。なければエラー
    def save_comment(self, comment, flag, which):
        txt = comment
        # txtに内容があるなら処理を続ける
        if len(txt) != 0:
            global source_path, dir_index, file_index, dir_path, file_path
            # "区分け"の下に追記
            # 一連の処理を行うことで'区分け'以降の行に追記される（評価した分だけ追記されない）
            flag = 0
            todolist = []
            try:
                with open(file_path) as f:
                    todolist = f.readlines()
                flag = 1
            except:
                # ここでサブウインドウが落ちる
                messagebox.showerror("error", "Todoリストを先に作成してください")

            line = '区分け\n'
            i = 0
            # ファイルがなかった場合エラーログが出るのでtryで囲んだ
            try:
                while True:
                    if todolist[i] == line:
                        break
                    i += 1

                del todolist[i+1:]

                with open(file_path, mode='w') as f:
                    f.writelines(todolist)

                # write file(append review text)
                with open(file_path, mode='a') as f:
                    f.write(txt + '\n')

                    if flag:
                        f.write("★" + '\n')

                    if which == 0:
                        f.write("出来た！" + '\n')
                    else:
                        f.write("出来なかった..." + '\n')
            except:
                pass
        else:
            messagebox.showerror("error", "コメントがありません")


if __name__ == '__main__':
    root = tk.Tk()
    app = MainMenu(master=root)
    app.mainloop()


