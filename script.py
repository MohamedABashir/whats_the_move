import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WhereTheMove.settings")
django.setup()
from Events.models import Category, Event
from django.contrib.auth.models import User
from WhereTheMove.settings import MEDIA_ROOT
from users.models import Profile
from Events.models import Category, Event
from django.utils.text import slugify 
from django.core import files
from io import BytesIO
import requests
from mapbox_location_field.models import LocationField
import json
from PIL import Image
from django.core.files import File
import random
# import pandas as pd 




# # df = pd.read_csv('mn_cities.csv')
# # print()
# # x = list(zip(df.LATITUDE, df.LONGITUDE))
# # for i in x:
# # 	print((i[1], i[0]), ',')

# # LONGITUDE 
cord = [
(47.315597, -96.503569) ,
(43.559119, -92.730494) ,
(46.841, -92.2201) ,
(43.619683, -95.927261) ,
(44.86965, -92.823358) ,
(46.242778, -93.274722) ,
(46.479929, -93.645413) ,
(47.000987, -94.72343000000001) ,
(45.615114, -94.574022) ,
(43.653678, -93.370672) ,
(45.557086, -96.04977199999999) ,
(45.253425, -93.646899) ,
(46.978229, -92.557937) ,
(43.646586, -93.582307) ,
(46.402538, -94.992017) ,
(45.881747, -95.38199399999999) ,
(45.491389, -92.785278) ,
(43.594594, -94.905088) ,
(44.136114, -91.974474) ,
(48.201968, -96.991457) ,
(43.890326, -94.177353) ,
(45.250679999999996, -93.284531) ,
(49.324923999999996, -95.090248) ,
(47.757738, -92.64133199999999) ,
(45.248272, -94.106072) ,
(45.238537, -93.407822) ,
(45.20543, -95.994872) ,
(44.409147, -96.199913) ,
(48.331418, -96.86709599999999) ,
(44.615279, -94.076195) ,
(46.078066, -95.82141700000001) ,
(46.196408, -92.752812) ,
(45.111645, -94.793779) ,
(46.871887, -95.988136) ,
(47.495096000000004, -92.241486) ,
(43.669538, -92.978374) ,
(43.970553, -95.60015200000001) ,
(45.612168, -94.436029) ,
(47.709121, -91.956951) ,
(46.869904999999996, -94.39591800000001) ,
(48.791294, -96.096523) ,
(47.487024, -95.41334) ,
(44.225253, -95.88377) ,
(46.677296000000005, -96.37269) ,
(46.519616, -92.62916700000001) ,
(45.899555, -95.87539100000001) ,
(45.547446, -96.56052700000001) ,
(46.314175, -95.714395) ,
(48.692724, -94.599479) ,
(46.343333, -94.286389) ,
(45.021405, -92.784375) ,
(45.553855, -96.706013) ,
(47.257778, -91.300278) ,
(43.622343, -96.369771) ,
(45.436539, -93.84096600000001) ,
(47.449090000000005, -95.945423) ,
(45.486521999999994, -94.969877) ,
(44.613852, -93.76039399999999) ,
(45.155626, -96.32235) ,
(47.572117999999996, -96.454864) ,
(44.605486, -95.317757) ,
(47.488071000000005, -94.848809) ,
(47.347732, -94.251921) ,
(47.158056, -94.690278) ,
(45.312903999999996, -95.57664399999999) ,
(46.251457, -95.035733) ,
(45.394114, -93.233088) ,
(48.156028000000006, -93.729629) ,
(45.350648, -93.739917) ,
(43.533612, -95.651527) ,
(47.750227, -93.670699) ,
(43.894155, -95.04571) ,
(48.624696, -94.167652) ,
(44.750729, -94.871634) ,
(47.533056, -92.34) ,
(47.738136, -94.496072) ,
(44.939512, -95.063955) ,
(43.897732, -93.06081) ,
(43.639426, -94.09237900000001) ,
(46.491795, -95.22359200000001) ,
(45.784427, -93.553658) ,
(47.189640999999995, -96.55296899999999) ,
(47.286788, -93.372322) ,
(45.81212, -94.41753299999999) ,
(47.543056, -93.796389) ,
(44.850725, -95.942102) ,
(45.717546999999996, -93.203695) ,
(46.357219, -94.20187299999999) ,
(46.0039, -95.578769) ,
(46.27966, -96.56222) ,
(43.703223, -95.480676) ,
(43.574628000000004, -93.821081) ,
(47.314161999999996, -91.862521) ,
(47.654959999999996, -92.632062) ,
(45.938694, -92.98347) ,
(47.812942, -96.011663) ,
(46.838425, -92.643005) ,
(45.493171000000004, -95.090049) ,
(46.090525, -94.834581) ,
(45.606934, -96.80625) ,
(43.724761, -92.873752) ,
(43.670732, -91.301226) ,
(44.728145, -94.330611) ,
(46.284496000000004, -92.618994) ,
(45.8975, -94.093333) ,
(45.181371, -93.863479) ,
(44.770885, -94.591207) ,
(47.493611, -92.777778) ,
(44.767778, -93.2775) ,
(45.88803, -94.696214) ,
(43.965416999999995, -94.795627) ,
(44.037333000000004, -92.630753) ,
(43.622079, -91.483657) ,
(47.007642, -95.94396400000001) ,
(47.321944, -93.276667) ,
(47.321944, -93.276667) ,
(47.321944, -93.276667) ,
(47.321944, -93.276667) ,
(47.321944, -93.276667) ,
(47.812942, -96.011663) ,
(46.838425, -92.643005) ,
(45.493171000000004, -95.090049) ,
(46.090525, -94.834581) ,
(45.606934, -96.80625) ,
(43.724761, -92.873752) ,
(43.670732, -91.301226) ,
(44.728145, -94.330611) ,
(46.284496000000004, -92.618994) ,
(45.8975, -94.093333) ,
(45.181371, -93.863479) ,
(44.770885, -94.591207) ,
(47.493611, -92.777778) ,
(44.767778, -93.2775) ,
(47.812942, -96.011663) ,
(46.838425, -92.643005) ,
(45.493171000000004, -95.090049) ,
(46.090525, -94.834581) ,
(45.606934, -96.80625) ,
(43.724761, -92.873752) ,
(43.670732, -91.301226) ,
(44.728145, -94.330611) ,
(46.284496000000004, -92.618994) ,
(45.8975, -94.093333) ,
(45.181371, -93.863479) ,
(44.770885, -94.591207) ,
(47.493611, -92.777778) ,
(44.767778, -93.2775) ,
]

cat = ['Outdoors & Adventure', 'Tech', 'Family', 'Health & Wellness', 'Sports & Fitness', 'Learning', 'Photography', 'Food & Drink', 'Writing', 'Language & Culture', 'Music', 'Movements', 'Film', 'Sci-Fi & Games', 'Beliefs', 'Arts', 'Book Clubs', 'Dance', 'Pets', 'Hobbies & Crafts', 'Fashion & Beauty', 'Social', 'Career & Business']

# for i in cat:
# 	Category.objects.create(name=i, slug=slugify(i))






bio = ['Sin gawkier teetotaler voucher eriophyllous underisory hysterectomized paleopathological. Redenied nonrhythm uncontemned upheaval flattener pendency nobble reunifying. Keratinizing repreparing hector slakeable adenoidal reception resharing bowelling.',
       'Unacceding puritan hematuric sambur preclose whoremastery feverish langset. Capitation coefficiently sunray spectacularity framer auditorially keitel breton. Affiliated mesolonghi overafflict nonconditional carcaneted quadrivalent nonopposition alethia.',
       'Prechallenging prostatic unenlightened interinsular notifiable anticommercial futileness deliverer. Adfreeze kriemhild leash expertly decrescent hemispheroidal precyclone qto. Assessable misnarrated kapfenberg unbluffed killeen telestich pereira incrassated.',
       'Hypochromic esotropia lento bilobate schematising puntillas seculariser frustulum. Commensal misdoubt anticonstitutionalism leukas knightliness reconstruct electrodialysis subfestive. Somnolently preholding therme paramilitary danton rehoning quarrellingly swith.', 
        'Concord repechage acnodal ungiving ecuadorean uncollated animistic kettledrummer. Unnorthern bouncing motey riding subcivilization nonfanatic phlogistic aglycone. Theorbist contused unmutual applique epenthetic frizzes eunuchise irksomeness.', 
        'Vaguio gnostic madwort magnesite gila impressing ordovician intervenient. Rehem oophoric suburies bicyclist sepharvites elbie dolomitisation hennepin. Stibial lowerclassman rewash misdirect rummaged whangdoodle groggiest evacuated.', 
        'Mucose iterance myoneuralgia cheerier topically presidentship margaric supernation. Topple legally saloop fideicommissum plainstanes carillon lanthanon anomic. Murrine donizetti except uam ghazzah misanthropical poinsettia autono.',
        'Devocalized transposal animalizing hibachi nonrecuperatory condyloma unhastily unperilous. Unsatiated unpedigreed embitter gyrostatic hypersensitized atwain burhel tashusai. Anstï¿¥ï¾¡sse misphrased halle pantomimist retiring deaminizing wedeling ageless.',
        'Rosinante allotropicity borgerhout gramarye nonary boswellian bozo skating. Lawsuit hushful preexhaustion succulent zapotec scaramouch enclasp koord. Underregistration juicier ouida kenhorst abate urbiculture cayce presuggest.',
       'Thought dorï¿¥ï¾½ sidelong multiradial stretcher jacklighter noncongruous neoprene. Aflutter calaverite microbalance lugubriosity beeline quarte satiricalness burlesquely. Tent kermit lixiviation lucullean unreelable belat landseer kettering.',]
# print(len(name), len(bio))

# date = ["03-19-1912","04-16-2074","10-26-2021","03-01-2071","03-06-1911","06-10-1957","07-08-2061","05-10-1933","06-21-1906","03-27-2073 "]

def main():
	u_id = [1, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
	secure_random = random.SystemRandom()
	# print()

	k=0
	u=0
	for j in cat:
		if k>= 99:
			k = 0
		for i in range(5):
			if u > len(u_id):
				u = 0
			e = Event()
			e.host = User.objects.filter(id=secure_random.choice(u_id)).first()
			print(e.host)
			e.title = secure_random.choice(bio)[0:20]
			e.description = secure_random.choice(bio)
			# url = img_list[k].get("download_url")
			# resp = requests.get(url)
			# if resp.status_code != requests.codes.ok:
			# 	print("shit")
			# 	pass
			# fp = BytesIO()
			# fp.write(resp.content)
			# file_name = f'{k}-image.jpg' # There's probably a better way of doing this but this is just a quick example
			# e.event_img.save(file_name, files.File(fp))
			e.categories = Category.objects.filter(name=j).first()			
			e.slug = f'{slugify(e.title)}-{e.pk}'
			e.event_location = cord[k]
			e.save()
			u+=1
			for _ in range(6):
				e.attend.add(User.objects.filter(id=secure_random.choice(u_id)).first())
			if k<99:
				k+=1
# main()

# if __name__ == '__main__':
# 	main()
names = ['Olivia', 'Isla', 'Aurora', 'Luna', 'Charlotte', 'Ada', 'Cora', 'Amelia', 'Maeve', 'Ophelia', 'Amara', 'Ava', 'Eleanor', 'Genevieve', 'Alice', 'Evelyn', 'Elodie', 'Ivy', 'Eloise', 'Rose', 'Aurelia', 'Lucy', 'Violet']
# for i in names:
# 	user = User.objects.create_user(username=i,
#                                  email=f'{i}@gmail.com',
#                                  password='testing321')

def main1():
	with open("Sample.json", "r") as read_it: 
		img_list = json.load(read_it) 
	k=0
	cat = Event.objects.all()
	for i in range(len(cat)):
		if k>99:
			k=0
		url = img_list[k].get("download_url")
		resp = requests.get(url)
		if resp.status_code != requests.codes.ok:
			print("shit")
			pass
		blob = BytesIO()
		img = Image.open(BytesIO(resp.content))
		img.save(blob, 'JPEG')
		cat[i].event_img.save( f'{cat[i]}.jpg', File(blob))
		k+=1

# main1()

color_options = ['beige', 'black', 'blue', 'cadetblue', 'darkblue', 'darkgreen', 'darkpurple', 'darkred', 'gray', 'green', 'lightblue', 'lightgray', 
				'lightgreen', 'lightred', 'orange', 'pink', 'purple', 'red', 'white']


icon_option = {
	'Outdoors & Adventure': {'color': 'white', 'icon': ''},
	'Tech': {'color': 'red', 'icon': 'laptop'},
	'Family': {'color': 'purple', 'icon': 'globe'},
	'Health & Wellness': {'color': 'pink', 'icon': ''},
	'Sports & Fitness': {'color': 'orange', 'icon': ''},
	'Learning': {'color': 'lightred', 'icon': ''},
	'Photography': {'color': 'lightgreen', 'icon': 'camera'},
	'Food & Drink': {'color': 'lightgray', 'icon': 'cutlery'},
	'Writing': {'color': 'lightblue', 'icon': 'pen'},
	'Language & Culture': {'color': 'green', 'icon': ''},
	'Music': {'color': 'gray', 'icon': 'music'},
	'Movements': {'color': 'darkred', 'icon': 'bullhorn'},
	'Film': {'color': 'darkpurple', 'icon': ''},
	'Sci-Fi & Games': {'color': 'darkgreen', 'icon': ''},
	'Beliefs': {'color': 'darkblue', 'icon': ''},
	'Arts': {'color': 'cadetblue', 'icon': ''},
	'Book Clubs': {'color': 'blue', 'icon': ''},
	'Dance': {'color': 'black', 'icon': ''},
	'Pets': {'color': 'beige', 'icon': ''},
	'Hobbies & Crafts': {'color': 'blue', 'icon': ''},
	'Fashion & Beauty': {'color': 'black', 'icon': ''},
	'Social': {'color': 'beige', 'icon': ''},
	'Career & Business': {'color': 'blue', 'icon': ''}
}

# print(icon_option["Tech"]["color"])
# import geopy
# from geopy.geocoders import Nominatim
# locator = Nominatim(user_agent="myGeocoder")
# location = locator.reverse(44.990440,-93.304820)