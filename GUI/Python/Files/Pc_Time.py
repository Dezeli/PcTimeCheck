from PIL import ImageTk
from tkinter import *
from tkinter import messagebox
import time
import sqlite3
import tkinter.messagebox
import pyglet
from Make_label import Get_label
from db import *
import os

img_path = os.path.join(os.getcwd())


class Gui:
    def __init__(self):
        self.screen = Tk()
        self.screen.iconbitmap("../../images/logo.ico")
        self.screen.title("컴퓨터 사용시간 프로그램")
        self.screen.geometry("805x805")
        self.screen.resizable(width=False, height=False)
        pyglet.font.add_file("../../font/GodoM.otf")
        pyglet.font.add_file("../../font/HoonDdukbokki.ttf")
        self.sort_color = 0
        self.sort_num = 0
        self.main_screen()
        self.screen.mainloop()

    def main_screen(self):
        self.destroy()
        Main_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/main_bg.png"), 0, 0
        )
        refresh_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/refresh.png"),
            660,
            50,
            self.main_screen,
        )
        User_button = Get_label.image_button(
            self, os.path.join(img_path, "../../images/btn_1.png"), 28, 290, self.reload
        )
        Exit_button = Get_label.image_button(
            self, os.path.join(img_path, "../../images/btn_2.png"), 415, 290, self._quit
        )
        now_data = get_recent_data()
        Data_1 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "../../images/Data.png"),
            31,
            390,
            f"현재 PC 이용 시간은 \n\n {now_data[3]} \n\n (시간:분:초) 입니다",
            "#472f91",
            ("고도 M", 24),
        )
        week_data = cal_week()
        Data_2 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "../../images/Data.png"),
            421,
            390,
            f"이번주 컴퓨터 이용횟수는 \n\n {week_data}번 입니다.",
            "#472f91",
            ("고도 M", 24),
        )

    def destroy(self):
        list1 = self.screen.place_slaves()
        for l in list1:
            l.destroy()

    def no_action(self):
        pass

    def reload(self):
        self.list = get_list("Date", self.sort_num)
        self.list_screen1()

    def list_screen1(self):
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.no_action,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.list_screen2,
        )
        left_button.config(state="disabled")
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            163,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            163,
            self.sort1,
            f"시작 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            307,
            163,
            self.sort2,
            f"종료 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            552,
            163,
            self.sort3,
            f"이용 시간",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 15:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                203 + (40 * i),
                f"{i+1}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                203 + (40 * i),
                f"{self.list[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                307,
                203 + (40 * i),
                f"{self.list[i][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                552,
                203 + (40 * i),
                f"{self.list[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )

    def list_screen2(self):
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.list_screen1,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.list_screen3,
        )
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            163,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            163,
            self.sort1,
            f"시작 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            307,
            163,
            self.sort2,
            f"종료 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            552,
            163,
            self.sort3,
            f"이용 시간",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 30:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length - 15
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                203 + (40 * i),
                f"{i+16}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                203 + (40 * i),
                f"{self.list[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                307,
                203 + (40 * i),
                f"{self.list[i+15][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                552,
                203 + (40 * i),
                f"{self.list[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )

    def list_screen3(self):
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "../../images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/left.png"),
            300,
            40,
            self.list_screen2,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "../../images/right.png"),
            400,
            40,
            self.no_action,
        )
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li1.png"),
            12,
            163,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            62,
            163,
            self.sort1,
            f"시작 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            307,
            163,
            self.sort2,
            f"종료 날짜 & 시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "../../images/li2.png"),
            552,
            163,
            self.sort3,
            f"이용 시간",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 45:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length - 30
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li1-1.png"),
                12,
                203 + (40 * i),
                f"{i+31}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                62,
                203 + (40 * i),
                f"{self.list[i+30][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                307,
                203 + (40 * i),
                f"{self.list[i+30][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "../../images/li2-1.png"),
                552,
                203 + (40 * i),
                f"{self.list[i+30][2]}",
                "#472f91",
                ("고도 M", 12),
            )

    def sort1(self):
        self.sort = "Start_time"
        self.list = get_list("Start_time", self.sort_num)
        self.sort_color = 1
        fir = self.list_screen1()

    def sort2(self):
        self.sort = "End_time"
        self.list = get_list("End_time", self.sort_num)
        self.sort_color = 2
        fir = self.list_screen1()

    def sort3(self):
        self.sort = "Use_time"
        self.list = get_list("Use_time", self.sort_num)
        self.sort_color = 3
        fir = self.list_screen1()

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.screen.quit()
            self.screen.destroy()
            exit()

    def change_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")


if __name__ == "__main__":
    a = Gui()
