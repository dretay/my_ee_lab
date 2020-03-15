from .instrument import Instrument
SenseFunctionMapping = {
        'voltage': 'volt',
        'current': 'curr',
        'concurrent': 'conc'}
class Keithley2280S_Sense():
    def __init__(self,parent):
        self.resource = parent.resource
    @property
    def function(self):
        return float(self.resource.query(":SENS:FUNC?").strip("\n8"))
    @function.setter
    def function(self,value):
        if value not in SenseFunctionMapping:
            raise Exception("invalid value for current setting")
        else:
            self.resource.write(f':SENS:FUNC "{value}"')
    @property
    def nplc(self):
        return float(self.resource.query(":SENS:CURR:NPLC?").strip("\n8"))
    @nplc.setter
    def nplc(self,value):
        if isinstance(value, int) or isinstance(value, float):
            self.resource.write(f':SENS:CURR:NPLC {value}')
        else:
            raise Exception("invalid value for nplc setting")

class Keithley2280S_Configure():
    def __init__(self,parent):
        self.resource = parent.resource
        # self.resource.write(':TRIG:SOUR IMM')




class Keithley2280S(Instrument):
  def __init__(self,visa_name):
    super(Keithley2280S, self).__init__(visa_name)
    self.resource.write('*RST')
    self.resource.write(':INIT:CONT ON')
    self.sense = Keithley2280S_Sense(self)
    # self.resource.write(':FORMat:ELEMents "READ,SOURCE"')

  @property
  def output(self):
    return self.resource.query(":OUTPut?").strip("\n8")
  @output.setter
  def output(self,value):
    if isinstance(value, bool):
      translated_value = "ON" if value else "OFF"
      self.resource.write(f':OUTPut {translated_value}')

  @property
  def current(self):
    return float(self.resource.query("MEAS:CURR?").split(',')[0][:-1])
  @current.setter
  def current(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':CURR {value}')
    else:
      raise Exception("invalid value for current setting")
  @property
  def voltage(self):
    return float(self.resource.query("MEAS:VOLT?").split(',')[1][:-2])
  @voltage.setter
  def voltage(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':VOLT {value}')
    else:
      raise Exception("invalid value for current setting")