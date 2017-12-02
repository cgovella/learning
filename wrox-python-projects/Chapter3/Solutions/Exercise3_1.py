import struct

def ser_num(n):
        ''' 
	ser_num(int|float) -> byte string

	convert n to a byte string if it is a float or int.
	ints are stored using their string representation, 
	encoded as UTF-8, since they are arbitrarily long.
	floats are stored as C doubles

	Raise Type error for any other type.'''

        if isinstance(n, int):
           # convert to bytes using str()
           data = bytes('i','utf-8') + bytes(str(n),'utf-8')
        elif isinstance(n, float):
           # convert to bytes with struct.pack
           data = bytes('f','utf-8') + struct.pack('d', n)
        else: raise TypeError('Expecting int or float')
        return data

def get_num(b):
        '''
	get_num(bytes) -> int|float

	convert bytestring b to an int of float'''

        # validate data -> type('i' or 'f')+bytes
        flag = str(b[:1],'utf-8')
        data = b[1:]
        # convert to binary
        if flag == 'i':
           s = str(data, 'utf-8')
           return int(s)
        elif flag == 'f':
           return struct.unpack("d", data)[0]
        else: raise ValueError('Unrecognised byte string format')

if __name__ == '__main__':
    e = 0.000000000000000001
    i = 1234567
    f = 3.1415926
    bi = ser_num(i)
    bf = ser_num(f)
    i == get_num(bi)
    f-e <= get_num(bf) <= f+e
    try: be = ser_num('a string')
    except TypeError: print('Type error on string')
    try: d = get_num(b'1234')
    except ValueError: print('Value Error on invalid bytes')


