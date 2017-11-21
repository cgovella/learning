import xml.etree.ElementTree as ET
import time

def parseDates(filename):
    dates = []
    rows = []
    dom = ET.parse(filename)
    root = dom.getroot()
    for node in dom.iter('*'):
        if 'Row' in node.tag:
           rows.append(node)
    for row in rows:
        row_dates = []
        for node in row.iter('*'):
            for key,value in node.attrib.items():
               if 'Type' in key and 'DateTime' in value:
                  row_dates.append(node.text)
        if len(row_dates) == 2:
            dates += row_dates
    return dates

def main():
    print( parseDates('toolhire.xml') )
    
if __name__ == '__main__':
    main() 