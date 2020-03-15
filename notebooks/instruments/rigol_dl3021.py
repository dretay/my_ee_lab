from instruments import Instrument

SourceCurrentRangeMapping = {
  'minimum': 'min',
  'maximum': 'max',
  'default': 'def'}

class RigolDL3021_Source_Current():
  def __init__(self,parent):
    self.resource = parent.resource
  #Sets the load's regulated current in CC mode
  @property
  def level(self):
    return float(self.resource.query(":SOUR:CURR:LEV:IMM?").strip("\n8"))
  @level.setter
  def level(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':SOUR:CURR:LEV:IMM {value}')
    else:
      raise Exception("invalid value for current setting")
  #Sets the current range in CC mode and transient operation mode to be a high range or a low one.
  @property
  def range(self):
    return int(self.resource.query(":SOUR:CURR:RANG?").strip("\n"))
  @range.setter
  def range(self,value):
    if value not in SourceCurrentRangeMapping:
      raise "invalid value for sourcing current range"
    else:
      self.resource.write(f':SOUR:CURR:RANG {value}')
  #Sets the starting voltage in CC mode.
  @property
  def voltage_on(self):
    return float(self.resource.query(":SOUR:CURR:VON?").strip("\n8"))
  @voltage_on.setter
  def voltage_on(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':SOUR:CURR:VON {value}')
    else:
      raise Exception("invalid value for voltage on setting")
  #Sets the voltage limit in CC mode
  @property
  def voltage_limit(self):
    return float(self.resource.query(":SOUR:CURR:VLIM?").strip("\n8"))
  @voltage_limit.setter
  def voltage_limit(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':SOUR:CURR:VLIM  {value}')
    else:
      raise Exception("invalid value for voltage limit setting")
  #Sets the current limit in CC mode. Note "1" means one amp
  @property
  def current_limit(self):
    return float(self.resource.query(":SOUR:CURR:ILIM?").strip("\n8"))
  @current_limit.setter
  def current_limit(self,value):
    if isinstance(value, int) or isinstance(value, float):
      self.resource.write(f':SOUR:CURR:ILIM {value}')
    else:
      raise Exception("invalid value for current limit setting")

class RigolDL3021(Instrument):
  def __init__(self,visa_name):
    super(RigolDL3021, self).__init__(visa_name)
    self.cc = RigolDL3021_Source_Current(self)
  ### Measurements
  @property
  def voltage(self):
    return float(self.resource.query("MEASure:VOLTage?").strip("\nH"))
  @property
  def max_voltage(self):
    return float(self.resource.query("MEASure:VOLTage:MAX?").strip("\nH"))
  @property
  def min_voltage(self):
    return float(self.resource.query("MEASure:VOLTage:MIN?").strip("\nH"))
  @property
  def current(self):
    return float(self.resource.query("MEASure:CURRent?").strip("\n\x00"))
  @property
  def max_current(self):
    return float(self.resource.query("MEASure:CURRent:MAX?").strip("\nH"))
  @property
  def min_current(self):
    return float(self.resource.query("MEASure:CURRent:MIN?").strip("\nH"))
  @property
  def resistance(self):
    return float(self.resource.query("MEASure:RESistance?").strip("\nH"))
  @property
  def power(self):
    return float(self.resource.query("MEASure:POWer?").strip("\nH"))
  @property
  def capability(self):
    return self.resource.query("MEASure:CAPability?")
  @property
  def watthours(self):
    return self.resource.query("MEASure:WATThours?")
  @property
  def discharging_time(self):
    return self.resource.query("MEASure:DISChargingTime?")
  @property
  def wavedata(self):
    return self.resource.query("MEASure:WAVedata?")
  @property
  def input(self):
    return self.resource.query(":SOUR:INP:STAT?")

  @input.setter
  def input(self,value):
    if isinstance(value, bool):
      translated_value = "1" if value else "0"
      self.resource.write(f':SOUR:INP:STAT {translated_value}')
