from tkinter import Tk, Label, Radiobutton, IntVar, Grid, W

class SofaGUI:
    def __init__(self, master):
        self.master = master
        
        self.master.title('SOFA Score Calculator')

        self.h1 = Label(master, text='SOFA Score Rechner' ,font='Times 16 bold')
        self.h1.grid(row=0, column=0, sticky=W)

        self.spacer1 = Label(master, text='              ', font='Times 16')
        self.spacer1.grid(row=1, column=1)

        self.po2fio2 = IntVar()
        self.po2fio2_label = Label(master, text='pO2/FiO2:', font='Times 11')
        self.po2fio2_label.grid(row=2, column=0, sticky=W)
        self.po2fio2_1point = Radiobutton(master, text='<400 mmHg', variable=self.po2fio2, value=1,
                                            selectcolor='black')
        self.po2fio2_1point.grid(row=3, column=0, sticky=W)
        self.po2fio2_2point = Radiobutton(master, text='<300 mmHg', variable=self.po2fio2, value=2,
                                            selectcolor='black')
        self.po2fio2_2point.grid(row=4, column=0, sticky=W)
        self.po2fio2_3point = Radiobutton(master, text='<200 mmHg bei Beatmung', variable=self.po2fio2 , 
                                            value=3, selectcolor='black')
        self.po2fio2_3point.grid(row=5, column=0, sticky=W)
        self.po2fio2_4point = Radiobutton(master, text='<100 mmHg bei Beatmung', variable=self.po2fio2,
                                            value=4, selectcolor='black')
        self.po2fio2_4point.grid(row=6, column=0, sticky=W)

        self.gcs = IntVar()
        self.gcs_label = Label(master, text='GCS:', font='Times 11')
        self.gcs_label.grid(row=2, column=2, sticky=W)
        self.gcs_1point = Radiobutton(master, text='13-14', variable=self.gcs, value=1, 
                                        selectcolor='black')
        self.gcs_1point.grid(row=3, column=2, sticky=W)
        self.gcs_2point = Radiobutton(master, text='10-12', variable=self.gcs, value=2,
                                        selectcolor='black')
        self.gcs_2point.grid(row=4, column=2, sticky=W)
        self.gcs_3point = Radiobutton(master, text='6-9', variable=self.gcs, value=3,
                                        selectcolor='black')
        self.gcs_3point.grid(row=5, column=2, sticky=W)
        self.gcs_4point = Radiobutton(master, text='<6', variable=self.gcs, value=4,
                                        selectcolor='black')
        self.gcs_4point.grid(row=6, column=2,sticky=W)

        self.spacer2 = Label(master, text='              ', font='Times 16')
        self.spacer2.grid(row=7, column=3)


if __name__ == '__main__':
    root = Tk()
    sofa_gui = SofaGUI(root)
    root.mainloop()



