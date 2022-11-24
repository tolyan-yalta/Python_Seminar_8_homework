import threading
import view
import export_data_csv
import export_data_xml
import import_data_csv
import import_data_xml

data = None
non_stop = True

type_file = None
last_file_name = None

def stop_while():
    global non_stop
    non_stop = view.stop_programm()


def load_data_xml(file_name):
    # Считывает данные из файла xml 
    global data
    data = import_data_xml.parse_xml(file_name)


def load_data_csv(file_name):
    # Считывает данные из файла csv
    global data
    data = import_data_csv.read_data_csv(file_name)


def write_data_xml():

    global data
    global last_file_name
    # print(last_file_name)
    # print(f'++{data}')
    export_data_xml.write_new_data_xml(data, last_file_name)


def write_data_csv():

    global data
    global last_file_name
    print(last_file_name)
    # print(f'++{data}')
    export_data_csv.write_new_data_csv(data, last_file_name)


def start_window():
    

    thr1 = threading.Thread(target=lambda : view.init()).start()

    def start_work_with_data():
        
        while non_stop:
            global data
            global type_file
            global last_file_name

            # Загрузка данных в таблицу        
            load_file, type_file, last_file_name = view.transfer_load_file()
            if load_file and type_file == 'xml':
                load_data_xml(last_file_name)
                view.transfer_data(data)
                view.fill_main_table()
                view.transfer_load_file_reset()
            if load_file and type_file == 'csv':
                load_data_csv(last_file_name)
                view.transfer_data(data)
                view.fill_main_table()
                view.transfer_load_file_reset()

            # Изменение данных в таблице
            add_data_info = view.transfer_add_data()
            if add_data_info:
                data = view.transfer_data_from_view()
                view.transfer_add_data_reset()
                if type_file == 'xml':
                    write_data_xml()
                    view.clean_main_table()
                    view.fill_main_table()
                if type_file == 'csv':
                    write_data_csv()
                    view.clean_main_table()
                    view.fill_main_table()

            stop_while()

    thr2 = threading.Thread(target = start_work_with_data).start()
        

    
