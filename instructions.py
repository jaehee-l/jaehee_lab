# Create a  delivery_personnel class:
class delivery_personnel:
	def __init__(self, name, years_of_services, company, is_drone, zip_codes_covered):
		self.name = name
		self.years_of_services = years_of_services 
		self.company = company 
		self.is_drone = is_drone 
		self.zip_codes_covered = zip_codes_covered

	def get_years_of_service(self):
		return self.years_of_service

	def get_company(self):
		return self.company
	
	def get_zip_codes_covered(self):
		return self.zip_codes_covered

 
	def set_years_of_service(self, d):
		self.years_of_service = d

	def set_company(self, d):
		self.company = d
	
	def set_zip_codes_covered(self, d):
		self.zip_codes_covered = d

 
 
# Recursive deliver() method:
	def deliver(self, zip_codes):

 
# Filter out the the zip codes which are in the delivery_personnel’s zip_codes_covered (HINT: try to do this in one line of code)
		covered_zipcodes = [i for i in zip_codes if i in self.zip_codes_covered]

		if(len(covered_zipcodes) == 1):
			
			print("Delivering to " + str(covered_zipcodes[0]))

		else:

			mid  = int((len(covered_zipcodes)+1)/2)

			self.deliver(covered_zipcodes[:mid])	
			self.deliver(covered_zipcodes[mid:])	

 
# Prints out the the zip code when a delivery is completed

# (HINT: Use divide and conquer!!!)
# Use the following instructions (https://help.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line) to:
# Add your changes
# Commit your changes
# And push your changes to your repo
# Submit your solution along with your Github repo link commented in the solution, and make sure your repo is public.


zipcodes = [1, 2, 4, 6]
myzips = [1, 3, 4]

delivery_personnel_1 = delivery_personnel('Pat', 4, 'Fedex', True, zipcodes)
delivery_personnel_1.deliver(myzips)