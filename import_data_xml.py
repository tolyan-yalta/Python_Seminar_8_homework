import xml.etree.ElementTree as ET

def delete_tail(data):
    new_data = []
    for person in data:
        if len(person) == 1:
            continue
        elem_pers = []
        for i in person:
            if i == None:
                i = ''
            elem_pers.append(i)
        new_data.append(tuple(elem_pers))
    return new_data       


def parse_xml(file_name):
    # Чтение данных из файла в формате xml
    with open(f'{file_name}', 'r'):
        # tree = ET.parse(f'{file_name}')
        # root = tree.getroot()

        data = [tuple([i.text  for i in ET.parse(f'{file_name}').getroot()[j]]) 
                for j in range(len(ET.parse(f'{file_name}').getroot()))]
        # print(data)
    return data

    #     def add_id(i):
    #         value_id = i.attrib.get('id', None)
            
    #         person = [j.text for j in i]
    #         return (value_id, *person)
    # temp_data = list(map(add_id , ET.parse(f'{file_name}').getroot()))
    # # temp_data = list(map(add_id , ET.parse('data2.xml').getroot()))

    # # print(temp_data)
    # # print(delete_tail(temp_data))

    # return delete_tail(temp_data)
