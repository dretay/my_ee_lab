class PDVS2(SerialInstrument):
	def __init__(self,visa_name,baud_rate):
		super(PDVS2, self).__init__(visa_name, baud_rate)
		self._voltage = 0

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self,voltage):
		self.resource.write("<KeyVoltage, 0, {}>".format(voltage))
		time.sleep(0.5)
		self._voltage = voltage