import xml.sax
import xml.sax.handler

class ToolHireHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
       super().__init__()
       self.dates = []
       self.dateLent = ''
       self.dateCounter = 0
       self.isDate = False
       
    def startElement(self, name, attributes):
       if name == "Data":
            data = attributes.get('ss:Type', None)
            if data == 'DateTime':
                self.isDate = True
                self.dateCounter += 1
            else:
                self.dateCounter = 0
                    
    def endElement(self, name):
        self.isDate = False
 
    def characters(self, data):
        if self.isDate:
            if self.dateCounter == 1:
                self.dateLent = data
            else:
                self.dates.append((self.dateLent, data))

if __name__ == '__main__':
    handler = ToolHireHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('toolhire.xml')
    print(handler.dates)

                

