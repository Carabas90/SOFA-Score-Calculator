from tkinter import Tk, Label, Radiobutton, IntVar, Grid, W

class SofaGUI:
    def __init__(self, master):
        self.master = master
        
        self.master.title('SOFA Score Calculator')
        
        self.spacer0 = Label(master, text='              ', font='Times 16')
        self.spacer0.grid(row=0, column=0)

        self.h1 = Label(master, text='SOFA Score Rechner' ,font='Times 16 bold')
        self.h1.grid(row=1, column=0, sticky=W)

        self.spacer1 = Label(master, text='              ', font='Times 16')
        self.spacer1.grid(row=2, column=1)

        self.po2fio2 = IntVar()
        self.po2fio2_label = Label(master, text='pO2/FiO2:', font='Times 12')
        self.po2fio2_label.grid(row=3, column=0, sticky=W)
        self.po2fio2_0point = Radiobutton(master, text='>400 mmHg', variable=self.po2fio2, value=0,
                                            selectcolor='black', command=self.refresh_sol)
        self.po2fio2_0point.grid(row=4, column=0, sticky=W)
        self.po2fio2_1point = Radiobutton(master, text='<400 mmHg', variable=self.po2fio2, value=1,
                                            selectcolor='black', command=self.refresh_sol)
        self.po2fio2_1point.grid(row=5, column=0, sticky=W)
        self.po2fio2_2point = Radiobutton(master, text='<300 mmHg', variable=self.po2fio2, value=2,
                                            selectcolor='black', command=self.refresh_sol)
        self.po2fio2_2point.grid(row=6, column=0, sticky=W)
        self.po2fio2_3point = Radiobutton(master, text='<200 mmHg bei Beatmung', variable=self.po2fio2 , 
                                            value=3, selectcolor='black', command=self.refresh_sol)
        self.po2fio2_3point.grid(row=7, column=0, sticky=W)
        self.po2fio2_4point = Radiobutton(master, text='<100 mmHg bei Beatmung', variable=self.po2fio2,
                                            value=4, selectcolor='black', command=self.refresh_sol)
        self.po2fio2_4point.grid(row=8, column=0, sticky=W)

        self.gcs = IntVar()
        self.gcs_label = Label(master, text='GCS:', font='Times 12')
        self.gcs_label.grid(row=3, column=2, sticky=W)
        self.gcs_0point = Radiobutton(master, text='> 14', variable=self.gcs, value=0,
                                        selectcolor='black', command=self.refresh_sol)
        self.gcs_0point.grid(row=4, column=2, sticky=W)
        self.gcs_1point = Radiobutton(master, text='13 - 14', variable=self.gcs, value=1, 
                                        selectcolor='black', command=self.refresh_sol)
        self.gcs_1point.grid(row=5, column=2, sticky=W)
        self.gcs_2point = Radiobutton(master, text='10 - 12', variable=self.gcs, value=2,
                                        selectcolor='black', command=self.refresh_sol)
        self.gcs_2point.grid(row=6, column=2, sticky=W)
        self.gcs_3point = Radiobutton(master, text='6 - 9', variable=self.gcs, value=3,
                                        selectcolor='black', command=self.refresh_sol)
        self.gcs_3point.grid(row=7, column=2, sticky=W)
        self.gcs_4point = Radiobutton(master, text='< 6', variable=self.gcs, value=4,
                                        selectcolor='black', command=self.refresh_sol)
        self.gcs_4point.grid(row=8, column=2,sticky=W)

        self.spacer2 = Label(master, text='              ', font='Times 16')
        self.spacer2.grid(row=9, column=3)

        self.map = IntVar()
        self.map_label = Label(master, text='MAP und Einsatz von Vasopressoren:', font='Times 12')
        self.map_label.grid(row=3, column=4, sticky=W)
        self.map_0point = Radiobutton(master, text='MAP > 70mmHg', variable=self.map, value=0,
                                        selectcolor='black', command=self.refresh_sol)
        self.map_0point.grid(row=4, column=4, sticky=W)
        self.map_1point = Radiobutton(master, text='MAP < 70mmHg', variable=self.map, value=1,
                                        selectcolor='black', command=self.refresh_sol)
        self.map_1point.grid(row=5, column=4, sticky=W)
        self.map_2point = Radiobutton(master, text='Dopamin ≤ 5 µg/kg/min oder Dobutamin (Dosierung egal)', 
                                        variable=self.map, value=2, selectcolor='black', command=self.refresh_sol)
        self.map_2point.grid(row=6, column=4, sticky=W)
        self.map_3point = Radiobutton(master, text='Dopamin > 5 µg/kg/min oder Adrenalin ≤ 0,1 µg/kg/min oder Noradrenalin ≤ 0,1 µg/kg/min ', 
                                        variable=self.map, value=3, selectcolor='black', command=self.refresh_sol)
        self.map_3point.grid(row=7, column=4, sticky=W)
        self.map_4point = Radiobutton(master, text='Dopamin > 15 µg/kg/min oder Adrenalin > 0,1 µg/kg/min oder Noradrenalin > 0,1 µg/kg/min ', 
                                        variable=self.map, value=4, selectcolor='black', command=self.refresh_sol)
        self.map_4point.grid(row=8, column=4, sticky=W)
        
        self.bili = IntVar()
        self.bili_label = Label(master, text='Bilirubin:', font='Times 12')
        self.bili_label.grid(row=10, column=0, sticky=W)
        self.bili_0point = Radiobutton(master, text='< 1.2 mg/dl', variable=self.bili, value=0,
                                        selectcolor='black', command=self.refresh_sol)
        self.bili_0point.grid(row=11, column=0, sticky=W)
        self.bili_1point = Radiobutton(master, text='1.2 - 1.9 mg/dl', variable=self.bili, value=1, 
                                        selectcolor='black', command=self.refresh_sol)
        self.bili_1point.grid(row=12, column=0, sticky=W)
        self.bili_2point = Radiobutton(master, text='2.0 - 5.9 mg/dl', variable=self.bili, value=2,
                                        selectcolor='black', command=self.refresh_sol)
        self.bili_2point.grid(row=13, column=0, sticky=W)
        self.bili_3point = Radiobutton(master, text='6.0 - 11.9 mg/dl', variable=self.bili, value=3,
                                        selectcolor='black', command=self.refresh_sol)
        self.bili_3point.grid(row=14, column=0, sticky=W)
        self.bili_4point = Radiobutton(master, text='> 12.0 mg/dl', variable=self.bili, value=4,
                                        selectcolor='black', command=self.refresh_sol)
        self.bili_4point.grid(row=15, column=0, sticky=W)

        self.thrombo = IntVar()
        self.thrombo_label = Label(master, text='Thrombozyten:', font='Times 12')
        self.thrombo_label.grid(row=10, column=2, sticky=W)
        self.thrombo_0point = Radiobutton(master, text='>150 Tsd./µl', variable=self.thrombo, value=0,
                                        selectcolor='black', command=self.refresh_sol)
        self.thrombo_0point.grid(row=11, column=2, sticky=W)
        self.thrombo_1point = Radiobutton(master, text='< 150 Tsd./µl', variable=self.thrombo, value=1, 
                                        selectcolor='black', command=self.refresh_sol)
        self.thrombo_1point.grid(row=12, column=2, sticky=W)
        self.thrombo_2point = Radiobutton(master, text='< 100 Tsd./µl', variable=self.thrombo, value=2,
                                        selectcolor='black', command=self.refresh_sol)
        self.thrombo_2point.grid(row=13, column=2, sticky=W)
        self.thrombo_3point = Radiobutton(master, text='< 50 Tsd./µl', variable=self.thrombo, value=3,
                                        selectcolor='black', command=self.refresh_sol)
        self.thrombo_3point.grid(row=14, column=2, sticky=W)
        self.thrombo_4point = Radiobutton(master, text='< 20 Tsd./µl', variable=self.thrombo, value=4,
                                        selectcolor='black', command=self.refresh_sol)
        self.thrombo_4point.grid(row=15, column=2,sticky=W)

        self.krea = IntVar()
        self.krea_label = Label(master, text='Kreatinin:', font='Times 12')
        self.krea_label.grid(row=10, column=4, sticky=W)
        self.krea_0point = Radiobutton(master, text='< 1.2 mg/dl', variable=self.krea, value=0,
                                        selectcolor='black', command=self.refresh_sol)
        self.krea_0point.grid(row=11, column=4, sticky=W)
        self.krea_1point = Radiobutton(master, text=' 1.2 - 1.9 mg/dl', variable=self.krea, value=1, 
                                        selectcolor='black', command=self.refresh_sol)
        self.krea_1point.grid(row=12, column=4, sticky=W)
        self.krea_2point = Radiobutton(master, text=' 2.0 - 3.4 mg/dl', variable=self.krea, value=2,
                                        selectcolor='black', command=self.refresh_sol)
        self.krea_2point.grid(row=13, column=4, sticky=W)
        self.krea_3point = Radiobutton(master, text=' 3.5 - 4.9 mg/dl', variable=self.krea, value=3,
                                        selectcolor='black', command=self.refresh_sol)
        self.krea_3point.grid(row=14, column=4, sticky=W)
        self.krea_4point = Radiobutton(master, text='> 5.0 mg/dl', variable=self.krea, value=4,
                                        selectcolor='black', command=self.refresh_sol)
        self.krea_4point.grid(row=15, column=4,sticky=W)

        self.spacer3 = Label(master, text='              ', font='Times 16')
        self.spacer3.grid(row=16, column=5)

        self.sol_label = Label(master, text=self.calc() ,font='Times 18', fg='orangered')
        self.sol_label.grid(row=17, column=2, columnspan=3, sticky=W)

        self.spacer4 = Label(master, text='              ', font='Times 16')
        self.spacer4.grid(row=18, column=5)

    def calc(self):
        sofa = 0 
        sofa += self.po2fio2.get()
        sofa += self.gcs.get()
        sofa += self.map.get()
        sofa += self.thrombo.get()
        sofa += self.bili.get()
        sofa += self.krea.get()
        msg = 'Der SOFA-Score des Patienten ist ' + str(sofa) + ' Punkte!'
        return msg
    
    def refresh_sol(self):
        self.sol_label['text'] = self.calc()


if __name__ == '__main__':
    root = Tk()
    sofa_gui = SofaGUI(root)
    root.mainloop()



