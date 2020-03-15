from instruments.instrument import  Instrument

class SiglentSGD2042_Basic():
    def __init__(self,parent):
        self.resource = parent.resource

    def _get_type(self,channel):
        if channel in (1, 2):
            return self.resource.query(f"C{channel}:BaSic_WaVe?").split(',')[1]

    def _set_type(self,channel, wave_type):
        if wave_type not in ('SINE', 'SQUARE', 'RAMP', 'PULSE', 'NOISE', 'ARB', 'DC', 'PRBS'):
            raise Exception('invalid wave_type specified')
        if channel in (1, 2):
            self.resource.write(f'C{channel}:BSWV WVTP,{wave_type}')
        else:
            raise Exception('invalid channel')
    @property
    def type_1(self):
        return self._get_type(1)
    @type_1.setter
    def type_1(self,value):
        return self._set_type(1,value)
    @property
    def type_2(self):
        return self._get_type(2)
    @type_2.setter
    def type_2(self,value):
        return self._set_type(2,value)

    def _get_frequency(self,channel):
        if channel in (1, 2):
            return float(self.resource.query(f"C{channel}:BaSic_WaVe?").split(',')[3])

    def _set_frequency(self,channel, freq):
        if type(freq) is not int:
            raise Exception('frequency must ba an integer')
        if channel in (1, 2):
            self.resource.write(f'C{channel}:BSWV FRQ,{freq}')
        else:
            raise Exception('invalid channel')
    @property
    def frequency_1(self):
        return self._get_frequency(1)
    @frequency_1.setter
    def frequency_1(self,value):
        return self._set_frequency(1,value)
    @property
    def frequency_2(self):
        return self._get_frequency(2)
    @frequency_2.setter
    def frequency_2(self,value):
        return self._set_frequency(2,value)

    def _get_amplitude(self,channel):
        if channel in (1, 2):
            return float(self.resource.query(f"C{channel}:BaSic_WaVe?").split(',')[7])

    def _set_amplitude(self,channel, amp):
        if type(amp) not in (int, float):
            raise Exception('amplitude must ba an integer or float')
        if channel in (1, 2):
            self.resource.write(f'C{channel}:BSWV AMP,{amp}')
        else:
            raise Exception('invalid channel')
    @property
    def amplitude_1(self):
        return self._get_amplitude(1)
    @amplitude_1.setter
    def amplitude_1(self,value):
        return self._set_amplitude(1,value)
    @property
    def amplitude_2(self):
        return self._get_amplitude(2)
    @amplitude_2.setter
    def amplitude_2(self,value):
        return self._set_amplitude(2,value)

    def _get_offset(self,channel):
        if channel in (1, 2):
            return float(self.resource.query(f"C{channel}:BaSic_WaVe?").split(',')[13])

    def _set_offset(self,channel, ofst):
        if type(ofst) not in (int, float):
            raise Exception('offset must ba an integer or float')
        if channel in (1, 2):
            self.resource.write(f'C{channel}:BSWV OFST,{ofst}')
        else:
            raise Exception('invalid channel')
    @property
    def offset_1(self):
        return self._get_offset(1)
    @offset_1.setter
    def offset_1(self,value):
        return self._set_offset(1,value)
    @property
    def offset_2(self):
        return self._get_offset(2)
    @offset_2.setter
    def offset_2(self,value):
        return self._set_offset(2,value)



    def _get_duty(self,channel):
        if channel in (1, 2):
            return float(self.resource.query(f"C{channel}:BaSic_WaVe?").split(',')[21])

    def _set_duty(self,channel, duty):
        if type(duty) not in (int, float):
            raise Exception('duty must ba an integer or float')
        if channel in (1, 2):
            self.resource.write(f'C{channel}:BSWV DUTY,{duty}')
        else:
            raise Exception('invalid channel')
    @property
    def duty_1(self):
        return self._get_duty(1)
    @duty_1.setter
    def duty_1(self,value):
        return self._set_duty(1,value)
    @property
    def duty_2(self):
        return self._get_duty(2)
    @duty_2.setter
    def duty_2(self,value):
        return self._set_duty(2,value)



class SiglentSGD2042(Instrument):
    def __init__(self,visa_name):
        super(SiglentSGD2042, self).__init__(visa_name)
        self.basic = SiglentSGD2042_Basic(self)

    def _get_output(self,channel):
        if channel in (1, 2):
            response = self.resource.query(f"C{channel}:OUTP?").strip("\n8")
        if len(response) > 12:
            state = response.split(',')[0][8:]
            if state == 'OFF':
                return False
            elif state == 'ON':
                return True
            else:
                raise Exception("invalid response value when retrieving output state")
        else:
            raise Exception(f"invalid channel {channel} specified")
    def _set_output(self,channel, state):
        if type(state) is not bool:
            raise Exception('invalid state, boolean expected')
        if channel in (1, 2):
            if state:
                self.resource.write(f'C{channel}:OUTP ON')
            else:
                self.resource.write(f'C{channel}:OUTP OFF')
        else:
            raise Exception('invalid channel')

    @property
    def output_1(self):
        return self._get_output(1)
    @output_1.setter
    def output_1(self,value):
        return self._set_output(1,value)
    @property
    def output_2(self):
        return self._get_output(2)
    @output_2.setter
    def output_2(self,value):
        return self._set_output(2,value)




# -*- coding: utf-8 -*-
# import vxi11
# import binascii
# import time
# import numpy as np
# from numpy import *
# from matplotlib import pyplot as plt
# import math

# arbgen =  vxi11.Instrument("192.168.1.59")
# scope =  vxi11.Instrument("192.168.1.34")

# def int2hex(number, bits):
#   if number < 0:
#     return hex((1 << bits) + number)
#   else:
#     return hex(number)

# MAX_INT = 32767
# PP = 6.0

# # wave_points = []
# def convert_me(voltage,pp):
# 	dac_val = int((voltage*MAX_INT)/(pp/2))
# 	return int2hex(dac_val, 16)
# # wave_points.append(convert_me(-2.5,PP))
# # wave_points.append(convert_me(-1,PP))
# # wave_points.append(convert_me(0,PP))
# # wave_points.append(convert_me(1,PP))
# # wave_points.append(convert_me(2.5,PP))
# # these are the #'s less than 0
# # for pt in range(0x8000, 0xffff, 1):
# #     wave_points.append(pt)
# # wave_points.append(0xffff)

# # # these are the #'s greater than 0
# # for pt in range(0x0000, 0x7fff, 1):
# #     wave_points.append(pt)

# def create_wave_file(wave_points,pp):
#   """create a file"""
#   f = open("wave1.bin", "wb")
#   for a in wave_points:
#       b = convert_me(a, pp)
#       #print 'wave_points: ',a,b
#       b = b[2:]
#       len_b = len(b)
#       if (0 == len_b):
#           b = '0000'
#       elif (1 == len_b):
#           b = '000' + b
#       elif (2 == len_b):
#           b = '00' + b
#       elif (3 == len_b):
#            b = '0' + b
#       b = b[2:4] + b[:2] #change big-endian to little-endian
#       c = binascii.a2b_hex(b) #Hexadecimal integer to ASCii encoded string
#       f.write(c)
#   f.close()


# def send_wave_data(dev, frequency):
# 	"""send wave1.bin to the device"""
# 	f = open("wave1.bin", "rb") #wave1.bin is the waveform to be sent
# 	data = f.read()
# 	print('write bytes:',len(data))
# 	dev.write_raw(b"C1:WVDT WVNM,wave1,FREQ,%f,TYPE,8,AMPL,%f,OFST,0.0,PHASE,0.0,WAVEDATA,%s" % (frequency, PP, data))
# 	dev.write("C1:ARWV NAME,wave1")
# 	f.close()


# def get_wave_data(dev):
# 	"""get wave from the devide"""
# 	f = open("wave2.bin", "w") #save the waveform as wave2.bin
# 	dev.write("WVDT? user,wave1") #"X" series (SDG1000X/SDG2000X/SDG6000X/X-E)
# 	time.sleep(1)
# 	data = dev.read()
# 	data_pos = data.find("WAVEDATA,") + len("WAVEDATA,")
# 	print(data[0:data_pos])
# 	wave_data = data[data_pos:]
# 	print('read bytes:',len(wave_data))
# 	f.write(wave_data)
# 	f.close()

# if __name__ == '__main__':
# 	""""""

# 	# scope.write("*RST")

# 	# single acquisition
# 	scope.ask("SING;*OPC?")

# 	#set data range to all points displayed
# 	scope.write("CHAN:DATA:POIN DMAX")

# 	#set manual depth
# 	scope.write("ACQuire:POINts 10000")

# 	# # Xstart, Xstop, record length in samples
# 	xstart, xstop, rec_len, vals_per_interval = (float(f) for f in scope.ask("CHAN:DATA:HEAD?").split(',',4))

# 	frequency = math.pow((xstop-xstart),-1)

# 	# vertical resolution
# 	yres = int(scope.ask("CHAN:DATA:YRES?"))

# 	# voltage for binary value 0
# 	yor = float(scope.ask("CHAN:DATA:YOR?"))

# 	# time of first sample
# 	xor = float(scope.ask("CHAN:DATA:XOR?"))

# 	# time between adjacent samples
# 	xinc = float(scope.ask("CHAN:DATA:XINC?"))

# 	scope.write("FORM UINT,8") #set format to unsigned 8bit integer
# 	yinc = float(scope.ask("CHAN:DATA:YINC?")) #voltage value per bit
# 	data = scope.ask_raw(b"CHAN:DATA?") #channel data
# 	data2 = np.array(list(map(lambda x: yor+(yinc*x), data))[10:-1])
# 	plt.plot( data2 )
# 	plt.show()

# 	create_wave_file(data2, 6.0)
# 	send_wave_data(arbgen, frequency)
# 	# arbgen.write("C1:SRATE MODE,TARB,VALUE,333333,INTER,LINE") #Use TrueArb and fixed sample rate to play every point
