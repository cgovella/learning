import xml.etree.ElementTree as ET
import datetime as dt

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

def calculateAverage(dates):
    loan_periods = []
    while dates:
        lent = dates.pop(0).split('T')[0]
        ret = dates.pop(0).split('T')[0]
        lent_date = dt.datetime.strptime(lent,'%Y-%m-%d')
        ret_date = dt.datetime.strptime(ret,'%Y-%m-%d')
        loan_periods.append( (ret_date - lent_date).days )
    average = sum(loan_periods)/len(loan_periods)
    return average

def main():
    dates = parseDates('toolhire.xml')
    avg = calculateAverage(dates)
    print('Average loan period is: {} days'.format(avg))
    
if __name__ == '__main__':
    main()