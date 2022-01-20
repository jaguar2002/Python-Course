class Piglet:
	name = "piglet"
	years = 0
	def speak(self):
		print("Oink I'm {} Oink!".format(self.name))
	def pig_years(self):
		return self.years * 18
hamlet = Piglet()
hamlet.name = "hamlet"
hamlet.speak()
