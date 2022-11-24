import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

main_window = None
main_table = None
non_stop = True

load_file = None
type_file = None
last_file_name = None

data = None
data_changed = None


def close_main_window():
    # Закрывает основное окно
    global non_stop
    main_window.destroy()
    non_stop = False


def stop_programm():
    # Передает в controller non_stop = False
    global non_stop
    return non_stop


def dismiss(window):
    # window.grab_release()
    window.destroy()


def clean_main_table():
    # Очищает таблицу
    for i in main_table.get_children():
        main_table.delete(i)


def transfer_data(tr_data):
    # Перенос данных в view
    global data
    data = tr_data


def transfer_data_from_view():
    # Перенос данных из view
    global data
    return data


def btn_load_click():
    # нажатие кнопки "Загрузить"
    global load_file
    global type_file
    global last_file_name
    # clean_main_table() filetypes=[['csv', 'CSV'], ['xml', 'XML']]
    file_name = filedialog.askopenfilename()
    temp = file_name[-3:]
    match temp:
        case 'xml':
            load_file = True
            type_file = 'xml'
            last_file_name = file_name
        case 'csv':
            load_file = True
            type_file = 'csv'
            last_file_name = file_name
        case _:
            type_file = None


def transfer_load_file():
    # Перенос из view данных для загрузки из файла
    global load_file
    global type_file
    global last_file_name
    # load_file = None
    # type_file = None
    # last_file_name = None
    return load_file, type_file, last_file_name


def transfer_load_file_reset():
    # Сброс информации о загрузке из файла
    global load_file
    # global type_file
    # global last_file_name
    # last_file_name = None
    load_file = None


def btn_add_data_click():
    # Запускается окно добавления данных

    # global new_data
    global main_table

    add_data_win = tk.Toplevel(main_window)
    add_data_win.title('Добавление в телефонный справочник')

    h = 120
    w = 1100
    sw = add_data_win.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = add_data_win.winfo_screenheight()
    y = int((sh - h) / 2)
    add_data_win.geometry(f"{w}x{h}+{x}+{y}")
    add_data_win.resizable(False, False)

    def dismiss(window):
        window.grab_release()
        window.destroy()

    add_data_win.protocol("WM_DELETE_WINDOW", lambda: dismiss) # перехватываем нажатие на крестик

    init_heading_panel(add_data_win)
    
    frame_panel = tk.Frame(add_data_win, borderwidth=1, relief="raised")
    frame_panel.pack(anchor='nw', fill='x')

    entry_1 = ttk.Entry(frame_panel, font=('times new roman', 14, 'bold'))
    entry_1.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_2 = ttk.Entry(frame_panel, font=('times new roman', 14, 'bold'))
    entry_2.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_3 = ttk.Entry(frame_panel, font=('times new roman', 14, 'bold'))
    entry_3.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_4 = ttk.Entry(frame_panel, font=('times new roman', 14, 'bold'))
    entry_4.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_5 = ttk.Entry(frame_panel, font=('times new roman', 14, 'bold'))
    entry_5.pack(side="left", anchor='nw', padx=8, pady=8)


    def find_new_id():
        # Находится последний id  и создается новый
        global data
        temp = [int(i[0]) for i in data]
        temp.sort()
        return str(temp[-1] + 1)


    def get_new_data():
        # Извлекаются данные из полей ввода, добавляется новый id и устанавливается флаг наличия новых данных
        global data
        global data_changed
        new_data = [(find_new_id(), entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get())]
        data = data + new_data
        data_changed = True
        dismiss(add_data_win)


    frame = tk.Frame(add_data_win, borderwidth=1, relief="raised")
    frame.pack(anchor='nw', fill='x')

    btn_save = tk.Button(frame, text='Сохранить', command=get_new_data, font=('times new roman', 14, 'bold'))
    btn_save.pack(side="left")
    btn_destroy = tk.Button(frame, text='Закрыть', command=lambda: dismiss(add_data_win), font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left")

    add_data_win.transient(main_window)
    add_data_win.grab_set()


def transfer_add_data():
    # Перенос из view информации о добавлении данных
    global data_changed
    return data_changed

def transfer_add_data_reset():
    # Сброс информации о добавлении данных
    global data_changed
    data_changed = None


def init_heading_panel(window):
    frame = tk.Frame(window, borderwidth=1, relief="raised")
    frame.pack(anchor='nw', fill='x')

    lbl_famaly = tk.Label(frame, text='Фамилия', font=('times new roman', 14, 'bold'))
    lbl_famaly.pack(ipadx=75, side="left")
    lbl_name = tk.Label(frame, text='Имя', font=('times new roman', 14, 'bold'))
    lbl_name.pack(ipadx=75,side="left")
    lbl_last_name = tk.Label(frame, text='Отчество', font=('times new roman', 14, 'bold'))
    lbl_last_name.pack(ipadx=75,side="left")
    lbl_telephone = tk.Label(frame, text='Телефон', font=('times new roman', 14, 'bold'))
    lbl_telephone.pack(ipadx=70,side="left")
    lbl_e_mail = tk.Label(frame, text='E-mail', font=('times new roman', 14, 'bold'))
    lbl_e_mail.pack(ipadx=70,side="left")


def btn_change_click():
    # нажатие кнопки "Изменить"
    try:
        change_id = main_table.item(main_table.selection ())['values'][0]
        if change_id:
            change_data(change_id)
    except IndexError:
        pass
    

def change_data(change_id):
    # Запускается окно изменения данных
    global data
    global main_table

    change_data_win = tk.Toplevel(main_window)
    change_data_win.title('Изменение в телефонном справочнике')

    h = 120
    w = 1100
    sw = change_data_win.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = change_data_win.winfo_screenheight()
    y = int((sh - h) / 2)
    change_data_win.geometry(f"{w}x{h}+{x}+{y}")
    change_data_win.resizable(False, False)

    change_data_win.protocol("WM_DELETE_WINDOW", lambda: dismiss) # перехватываем нажатие на крестик

    def dismiss(window):
        window.grab_release()
        window.destroy()


    # Находим в базе данных конкретного человека
    for i in data:
        if int(i[0]) == change_id:
            change_data = i
            index_temp = data.index(i)
            break


    def get_new_data():
        # Получаем и сохраняем новые данные
        global data_changed
        new_data = (str(change_id), entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get())
        data[index_temp] = new_data
        data_changed = True
        dismiss(change_data_win)


    init_heading_panel(change_data_win)

    group_3 = tk.Frame(change_data_win, borderwidth=1, relief="raised")
    group_3.pack(anchor='nw', fill='x')

    entry_1 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_1.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_1.insert(0, change_data[1])
    entry_2 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_2.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_2.insert(0, change_data[2])
    entry_3 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_3.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_3.insert(0, change_data[3])
    entry_4 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_4.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_4.insert(0, change_data[4])
    entry_5 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_5.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_5.insert(0, change_data[5])

    group_4 = tk.Frame(change_data_win, borderwidth=1, relief="raised")
    group_4.pack(anchor='nw', fill='x')
    btn_save = tk.Button(group_4, text='Сохранить', command=get_new_data, font=('times new roman', 14, 'bold'))
    btn_save.pack(side="left")
    btn_destroy = tk.Button(group_4, text='Закрыть', command=lambda: dismiss(change_data_win), font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left")

    change_data_win.transient(main_window)
    change_data_win.grab_set()


def btn_remove_click():
    # нажатие кнопки "Удалить"
    try:
        remove_id = main_table.item(main_table.selection ())['values'][0]
        if remove_id:
            remove_data(remove_id)
    except IndexError:
        pass


def remove_data(remove_id):
    # Удаляем строку из данных
    global data    
    global data_changed
    # Находим в базе данных конкретного человека
    for i in data:
        if int(i[0]) == remove_id:
            index_remove = data.index(i)
            data.pop(index_remove)
            break
    data_changed = True


def btn_find_click():
    # нажатие кнопки "Найти"
    global data
    global main_table
    str_query = main_window.children['control_panel'].children['entry_find'].get()
    find_element = []
    for elem in data:
        for subelem in elem:
            if subelem == None:
                break
            if str_query in subelem:
                find_element.append(elem)
                break

    find_data_win = tk.Toplevel(main_window)
    find_data_win.title('Найдено в телефонном справочнике')

    h = 420
    w = 1100
    sw = find_data_win.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = find_data_win.winfo_screenheight()
    y = int((sh - h) / 2)
    find_data_win.geometry(f"{w}x{h}+{x}+{y}")
    find_data_win.resizable(False, False)

    def dismiss(window):
        window.grab_release()
        window.destroy()

    find_data_win.protocol("WM_DELETE_WINDOW", lambda: dismiss) # перехватываем нажатие на крестик

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('mystyle.Treeview', background='white', font=('times new roman', 12, 'bold')) # Modify the font of the body
    style.configure('mystyle.Treeview.Heading', background='grey70', font=('times new roman', 14, 'bold')) # Modify the font of the headings

    table = ttk.Treeview(find_data_win, name='main_table2', columns=['id', 'family', 'name', 'last_name', 'telephone', 'e_mail'], show='headings', style='mystyle.Treeview', selectmode='browse')
    table.pack(fill='both', expand=True)


    table.heading('id', text='id', anchor='center')
    table.column('id', width=50, anchor='center')

    table.heading('family', text='Фамилия', anchor='center')
    table.column('family', width=150)
    table.heading('name', text='Имя', anchor='center')
    table.column('name', width=150)
    table.heading('last_name', text='Отчество', anchor='center')
    table.column('last_name', width=150)
    table.heading('telephone', text='Телефон', anchor='center')
    table.column('telephone', anchor='center', width=150)
    table.heading('e_mail', text='E-mail', anchor='center')
    table.column('e_mail', anchor='center', width=150)
    

    for person in find_element:
        table.insert("", 'end', values=person)

    frame = tk.Frame(find_data_win, borderwidth=1, relief="raised")
    frame.pack(anchor='nw', fill='x')


    btn_destroy = tk.Button(frame, text='Закрыть', command=lambda: dismiss(find_data_win), font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left")

    find_data_win.transient(main_window)
    find_data_win.grab_set()


def init_main_window():
    # инициализация основного окна
    
    main_window.title('Телефонный справочник')

    h = 500
    w = 1070
    sw = main_window.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = main_window.winfo_screenheight()
    y = int((sh - h) / 2)
    main_window.geometry(f"{w}x{h}+{x}+{y}")
    main_window.resizable(False, False)


def init_control_panel():
    # инициализация панели управления

    control_panel = tk.Frame(main_window, name='control_panel', borderwidth=1, relief='raised')
    control_panel.pack(anchor='nw', fill='x')

    btn_load = tk.Button(control_panel, text='Загрузить', command=btn_load_click, font=('times new roman', 14, 'bold'))
    btn_load.pack(side='left', pady=5)
    btn_add = tk.Button(control_panel, text='Добавить', command=btn_add_data_click, font=('times new roman', 14, 'bold'))
    btn_add.pack(side='left', pady=5)
    btn_change = tk.Button(control_panel, text='Изменить', command=btn_change_click, font=('times new roman', 14, 'bold'))
    btn_change.pack(side='left', pady=5)
    btn_delete = tk.Button(control_panel, text='Удалить', command=btn_remove_click, font=('times new roman', 14, 'bold'))
    btn_delete.pack(side='left', pady=5)

    entry_find = ttk.Entry(control_panel, name='entry_find', width=50, font=('times new roman', 14, 'bold'))
    entry_find.pack(side='left', pady=5, fill='y')
    btn_search = tk.Button(control_panel, text='Найти', command=btn_find_click, font=('times new roman', 14, 'bold'))
    btn_search.pack(side='left', pady=5)

    btn_destroy = tk.Button(control_panel, text='Закрыть', command=close_main_window, font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left", pady=5)


def init_main_table(): 
    # инициализация основной таблицы
    
    global main_table

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('mystyle.Treeview', background='white', font=('times new roman', 12, 'bold')) # Modify the font of the body
    style.configure('mystyle.Treeview.Heading', background='grey70', font=('times new roman', 14, 'bold')) # Modify the font of the headings

    main_table = ttk.Treeview(main_window, name='main_table2', columns=['id', 'family', 'name', 'last_name', 'telephone', 'e_mail'], show='headings', style='mystyle.Treeview', selectmode='browse')
    main_table.pack(fill='both', expand=True)

    main_table.heading('id', text='id', anchor='center')
    main_table.column('id', width=50, anchor='center')

    main_table.heading('family', text='Фамилия', anchor='center')
    main_table.column('family', width=150)
    main_table.heading('name', text='Имя', anchor='center')
    main_table.column('name', width=150)
    main_table.heading('last_name', text='Отчество', anchor='center')
    main_table.column('last_name', width=150)
    main_table.heading('telephone', text='Телефон', anchor='center')
    main_table.column('telephone', anchor='center', width=150)
    main_table.heading('e_mail', text='E-mail', anchor='center')
    main_table.column('e_mail', anchor='center', width=150)

  
def fill_main_table():
    # Заполняется основная таблица
    global data
    global main_table
    for person in data:
        main_table.insert("", 'end', values=person)


def init():
    # инициализация чего??? tkinter-а
    # инициализация основного окна
    # инициализация панели управления
    # инициализация основной таблицы
    global main_window

    main_window = tk.Tk()

    init_main_window()
    init_control_panel()
    init_main_table()

    main_window.mainloop()

