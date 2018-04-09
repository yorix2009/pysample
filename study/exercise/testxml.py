# coding: UTF-8
from xml.dom.minidom import parse
import xml.dom.minidom
from xml.dom import Node
import os


# 使用DOM读取XML
def readXml(file):
    doc = parse(file)
    root=doc.documentElement
    print("Root Node=",root.nodeName)
    for n in root.childNodes:
        if n.nodeType==Node.ELEMENT_NODE:
            print(n.nodeName,n.nodeType,n.hasChildNodes())



if __name__ == '__main__':
    filename = os.environ['HOME'] + "/Program/hivemq-3.3.2/conf/config.xml"
    readXml(filename)
