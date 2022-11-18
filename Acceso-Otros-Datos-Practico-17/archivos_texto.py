import json
import csv
import xml.dom.minidom
import xml.etree.cElementTree as ET

def leer_xml(file: str) -> None:
    """Realiza la lectura de un archivo xml
    :param file: Archivo/Ruta que deseamos leer
    :type file: str"""
    tree = ET.parse("config_new.xml")
    root = tree.getroot()
    COMP = root.findall ('COMP') [0]
    print("Tag:", COMP.tag, "Attributes:", COMP.attrib, "Text:",
    COMP.text.strip(), "Tail:", COMP.tail)
    ruta = COMP.findall (file) [0]
    print("Tag:", COMP.tag, "Attributes:", COMP.attrib, "Text:", COMP.text.strip(),"Tail:", COMP.tail)


def GenerateXml() -> None:
    """Realiza la creación de un archivo xml"""
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'CONFIG_LIST', None)
    root = dom.documentElement
    employee = dom.createElement('COMP')
    root.appendChild(employee)
    nameE = dom.createElement('path')
    nameE.setAttribute ("valor", "aaaaaaaaaaa") # Agregar atributo
    nameT = dom.createTextNode('linux')
    nameE.appendChild(nameT)
    employee.appendChild(nameE)
    f = open('config_new.xml', 'a')
    dom.writexml(f, addindent=' ', newl='\n')
    f.close()

def crear_dictwriter_csv()-> None:
    """Realiza la creación de un archivo csv con la funcion dictwriter"""
    headers = ['name', 'age']
    datas = [{'name':'Bob', 'age':23},
            {'name':'Jerry', 'age':44},
            {'name':'Tom', 'age':15}]
    with open('example.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        for row in datas:
            writer.writerow(row)


def leer_dictwriter_csv(file: str)-> None:
    """Realiza la lectura de un archivo csv con dictwriter
    :param file: Archivo/Ruta que deseamos leer
    :type file: str"""
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            print(name)


def crear_csv()-> None:
    """Realiza la creación de un archivo csv"""
    datas = [['name', 'age'],['Bob', 14], ['Tom', 23], ['Jerry', '18']]
    with open('example.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in datas:
            writer.writerow(row)


def leer_csv(file: str)-> None:
    """Realiza la lectura de un archivo csv
    :param file: Archivo/Ruta que deseamos leer
    :type file: str"""
    with open(file,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(reader.line_num, row) 


def crear_json() -> None:
    """Realiza la creación de un archivo json"""
    test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
    json_str = json.dumps(test_dict,indent=4,sort_keys=True)
    with open('test.json',"w") as f:
        f.write(json_str)


def leer_json(file: str) -> None:
    """Realiza la lectura de un archivo json
    :param file: Archivo/Ruta que deseamos leer
    :type file: str"""
    with open(file,"r") as f:
        json_dic = json.load(f)
        print(json_dic["bigberg"])


def crear_txt() -> None:
    """Realiza la creación de un archivo txt"""
    with open("test.txt","w") as f:
        f.write("test string")


def leer_txt(file: str) -> None:
    """Realiza la lectura de un archivo txt
    :param file: Archivo/Ruta que deseamos leer
    :type file: str"""
    with open(file,"r") as f:
       print(f.read())