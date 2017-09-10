import javaobj
import logging
import time

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('--- %s ---', time.strftime("%H:%M:%S"))    
    filename = 'bom.zip'
    output = 'bom.ser'
    marshaller = javaobj.JavaObjectMarshaller()
    with open(filename, 'rb') as zip_file:
        data = zip_file.read()
        javaarray = javaobj.JavaByteArray(data, classdesc=javaobj.ByteArrayDesc())
        java_data = marshaller.dump(javaarray)
        with open(output, 'wb') as writefile:
            writefile.write(java_data)

if __name__ == '__main__':
    main()
