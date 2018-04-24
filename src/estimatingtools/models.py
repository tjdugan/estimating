from django.db import models

# Create your models here.

#############################################################################
#                                                                           #
#                            Materials data                                 #
#                                                                           #
#############################################################################
class Materials(models.Model):
	WATERPROOFING   = 'WP'
	DAMPPROOFING    = 'DP'
	CAULKING        = 'CK'
	SEALER          = 'SL'
	TRAFFIC_COATING = 'TC'
	EXPANSION_JOINT = 'EJ'
	FIRE_STOPPING   = 'FS'
	AIR_BARRIER     = 'AB'
	VAPOR_BARRIER   = 'VB'
	OTHER           = 'OT'

	FLUID_APPLIED_AIR_BARRIER = 'FAA'
	SHEET_AIR_BARRIER         = 'SAB'
	AIR_BARRIER_ACCESORY      = 'ABA'
	AIR_BARRIER_OTHER         = 'ABO'

	SHEET_WATERPROOFING         = 'SWP'
	FLUID_APPLIED_WATERPROOFING = 'FAW'
	DRAIN_MAT                   = 'DRM'
	PROTECTION_BOARD            = 'PRB'
	WATERPROOFING_ACCESSORY     = 'WPA'
	WATERPROOFING_OTHER         = 'WPO'

	SILICONE_SEALANT    = 'SIL'
	LATEX_SEALANT       = 'LAX'
	URETHANE_SEALANT    = 'URE'
	SANITARY_SEALANT    = 'SAN'
	SEALANT_ACCESSORIES = 'SAC'
	SEALANT_OTHER       = 'SEO'

	SUBCATEGORY_CHOICES = (
		(FLUID_APPLIED_AIR_BARRIER, 'Fluid-Applied Air Barrier'),
		(SHEET_AIR_BARRIER, 'Sheet Membrane Air Barrier'),
		(AIR_BARRIER_ACCESORY, 'Air Barrier Accessory'),
		(AIR_BARRIER_OTHER, 'Air Barrier Other'),
		(SHEET_WATERPROOFING, 'Sheet Waterproofing'),
		(FLUID_APPLIED_WATERPROOFING, 'Fluid-Applied Waterproofing'),
		(DRAIN_MAT, 'Drain Mat'),
		(PROTECTION_BOARD, 'Protection Board'),
		(WATERPROOFING_ACCESSORY, 'Waterproofing Accessory'),
		(WATERPROOFING_OTHER, 'Waterproofing Other'),
		(SILICONE_SEALANT, 'Silicone Sealant'),
		(LATEX_SEALANT, 'Latex Sealant'),
		(URETHANE_SEALANT, 'Urethane Sealant'),
		(SANITARY_SEALANT, 'Sanitary Sealant'),
		(SEALANT_ACCESSORIES, 'Sealant Accessory'),
		(SEALANT_OTHER, 'Sealant Other'),
		(OTHER, 'Other'),
		)

	MATERIAL_TYPE_CHOICES = (
		(WATERPROOFING, 'Waterproofing'),
		(DAMPPROOFING, 'Dampproofing'),
		(CAULKING, 'Caulking'),
		(SEALER, 'Sealar'),
		(TRAFFIC_COATING, 'Traffic Coating'),
		(EXPANSION_JOINT, 'Expansion Joint'),
		(FIRE_STOPPING, 'Fire Stopping'),
		(AIR_BARRIER, 'Air Barrier'),
		(VAPOR_BARRIER, 'Vapor Barrier'),
		(OTHER, 'Other'),
		)

	material       = models.CharField(max_length=220, )
	materialType   = models.CharField(max_length=2,
									  choices=MATERIAL_TYPE_CHOICES,
									  default=OTHER, )
	subCategory    = models.CharField(max_length=55,
									  choices=SUBCATEGORY_CHOICES,
									  default=OTHER, )
	footagePerUnit = models.DecimalField(max_digits=8, decimal_places=2, )
	costPerUnit    = models.DecimalField(max_digits=8, decimal_places=2, )
	manufacturer   = models.CharField(max_length=50, )
	dataSheetURL   = models.CharField(max_length=200, )
	sdsURL         = models.CharField(max_length=200, )
	distributor    = models.CharField(max_length=220, )
	updated        = models.DateTimeField(auto_now=True, )

	def __str__(self):
		return str(self.material)

	def get_absolute_url(self):
		return "/material/%s" %(self.id)

############################################################################
#                                                                           #
#                            Equipment data                                 #
#                                                                           #
#############################################################################
class Equipment(models.Model):
	equipment        = models.CharField(max_length=220, )
	daily            = models.DecimalField(max_digits=8, decimal_places=2, )
	weekly           = models.DecimalField(max_digits=8, decimal_places=2, )
	monthly          = models.DecimalField(max_digits=8, decimal_places=2, )
	additionalCost   = models.DecimalField(max_digits=8, decimal_places=2 )
	addCostDescript  = models.CharField(max_length=200, )
	distributor      = models.CharField(max_length=220, )
	updated          = models.DateTimeField(auto_now=True, )

	def __str__(self):
		return str(self.equipment)

	def get_absolute_url(self):
		return "/equipment/%s" %(self.id)

#############################################################################
#                                                                           #
#                           Manufacturers' data                             #
#                                                                           #
#############################################################################

class Manufacturer(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )
	productRep = models.CharField(max_length=25, )

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return "/manufacturer/%s" %(self.id)

#############################################################################
#                                                                           #
#                             People data                                   #
#                                                                           #
#############################################################################

class ProductRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

	def get_absolute_url(self):
		return "/productrep/%s" %(self.id)

class SalesRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

	def get_absolute_url(self):
		return "/salesrep/%s" %(self.id)

class ContractorRep(models.Model):
	firstname = models.CharField(max_length=25, )
	lastname = models.CharField(max_length=35, )
	officenumber = models.CharField(max_length=30, )
	mobile = models.CharField(max_length=30, )
	email = models.CharField(max_length=55, )
	company = models.CharField(max_length=55, )

	def __str__(self):
		return str(self.firstname + ' ' + self.lastname)

	def get_absolute_url(self):
		return "/contractorrep/%s" %(self.id)

#############################################################################
#                                                                           #
#                           Distributor data                                #
#                                                                           #
#############################################################################

class Distributor(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )
	salesRep   = models.CharField(max_length=25, )

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return "/distributor/%s" %(self.id)

#############################################################################
#                                                                           #
#                           Contractor data                                 #
#                                                                           #
#############################################################################

class Contractor(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return "/contractor/%s" %(self.id)

#############################################################################
#                                                                           #
#                           Architect data                                  #
#                                                                           #
#############################################################################

class Architect(models.Model):
	name       = models.CharField(max_length=50, )
	address    = models.CharField(max_length=50, )
	address2   = models.CharField(max_length=50, )
	phone      = models.CharField(max_length=20, )
	website    = models.CharField(max_length=220, )

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return "/architect/%s" %(self.id)


#############################################################################
#                                                                           #
#                            Production data                                #
#                                                                           #
#############################################################################

class ProductionRate(models.Model):
	SQUARE_FOOTAGE     = 'SF'
	LINEAL_FOOTAGE     = 'LF'
	COUNT              = 'CT'
	MAN_DAY            = 'MD'
	MAN_HOUR           = 'MH'
	TWO_MAN_CREW_DAY   = '2D'
	THREE_MAN_CREW_DAY = '3D'
	FOUR_MAN_CREW_DAY  = '4D'
	WATERPROOFING   = 'WP'
	DAMPPROOFING    = 'DP'
	CAULKING        = 'CK'
	SEALER          = 'SL'
	TRAFFIC_COATING = 'TC'
	EXPANSION_JOINT = 'EJ'
	FIRE_STOPPING   = 'FS'
	AIR_BARRIER     = 'AB'
	VAPOR_BARRIER   = 'VB'
	OTHER           = 'OT'

	SCOPE_CHOICES = (
		(WATERPROOFING, 'Waterproofing'),
		(DAMPPROOFING, 'Dampproofing'),
		(CAULKING, 'Caulking'),
		(SEALER, 'Sealer'),
		(TRAFFIC_COATING, 'Traffic Coating'),
		(EXPANSION_JOINT, 'Expansion Joint'),
		(FIRE_STOPPING, 'Fire Stopping'),
		(AIR_BARRIER, 'Air Barrier'),
		(VAPOR_BARRIER, 'Vapor Barrier'),
		(OTHER, 'Other'),
	)

	FOOTAGE_TYPE_CHOICES = (
		(SQUARE_FOOTAGE, 'Square Footage'),
		(LINEAL_FOOTAGE, 'Lineal Footage'),
		(COUNT, 'Count')
	)
	PRODUCTION_TIME_CHOICES = (
		(MAN_DAY, 'Man Day'),
		(MAN_HOUR, 'Man Hour'),
		(TWO_MAN_CREW_DAY, 'Two Man Crew - 1 Day'),
		(THREE_MAN_CREW_DAY, 'Three Man Crew - 1 Day'),
		(FOUR_MAN_CREW_DAY, 'Four Man Crew - 1 Day'),
	)

	task = models.CharField(max_length=50, )
	footageType = models.CharField(
		max_length=2,
		choices=FOOTAGE_TYPE_CHOICES, 
		default=SQUARE_FOOTAGE,
	)
	scope = models.CharField(
		max_length=2,
		choices=SCOPE_CHOICES,
		default=OTHER,
	)
	productionTime = models.CharField(
		max_length=2,
		choices=PRODUCTION_TIME_CHOICES,
		default=MAN_HOUR,
	)
	production = models.IntegerField()

	def __str__(self):
		return str(self.task)

	def get_absolute_url(self):
		return "/productionrate/%s" %(self.id)

#############################################################################
#                                                                           #
#                              Labor Rates                                  #
#                                                                           #
#############################################################################
class LaborRate(models.Model):
	state            = models.CharField(max_length=2, )
	city			 = models.CharField(max_length=20, )
	local            = models.CharField(max_length=2, )
	rate             = models.DecimalField(max_digits=8, decimal_places=2, )
	fringes          = models.DecimalField(max_digits=8, decimal_places=2, )
	fica             = models.DecimalField(max_digits=8, decimal_places=2, )
	futa             = models.DecimalField(max_digits=8, decimal_places=2, )
	sui              = models.DecimalField(max_digits=8, decimal_places=2, )
	comp             = models.DecimalField(max_digits=8, decimal_places=2, )
	liability        = models.DecimalField(max_digits=8, decimal_places=2, )
	disability       = models.DecimalField(max_digits=8, decimal_places=2, )
	roomboard        = models.DecimalField(max_digits=8, decimal_places=2, )
	travel           = models.DecimalField(max_digits=8, decimal_places=2, )
	tools            = models.DecimalField(max_digits=8, decimal_places=2, )
	total            = models.DecimalField(max_digits=8, decimal_places=2, )
	

	def __str__(self):
		return str(self.local)

	def get_absolute_url(self):
		return "/local/%s" %(self.id)
