import visa

class Instrument(object):
	def __init__(self, visa_name):
		rm = visa.ResourceManager()
		self.resource = rm.open_resource(visa_name)