from flask import Flask, render_template
app = Flask(__name__)

# This is the main page
@app.route("/")
def index():
	return render_template("Index.html")


#This is the frame pages
@app.route("/frame")
def frame():
	intro = "The frame is the backbone and skin of the drone. It protects the internal electronics and can have vast differance in size  and use. We messure the dementions and test the hardnes and cuality of the materials used. As well as privide a general information on shape and what the frame was ment to be used for."
	Ritems = ["ROTOR RIOT CL1"]
	Sitems = ["SABOTAGERC DINGO"]
	Titems = ["TBS SOURCE ONE"]
	return render_template("List.html", Ritems=Ritems, Sitems=Sitems, Titems=Titems, intro=intro)

@app.route("/item/ROTOR RIOT CL1")
def ROTORRIOTCL1():
	name = "ROTOR RIOT CL1"
	pic = "Rotorriotcl1.png"
	material = "Carbon Fiber"
	style = "Stretch X"
	size = "5 inch"
	use = "free style"
	fickness = "2.5 mm"
	motors = "2260 to 2570"
	FC = "40x40 mm"
	video = ["https://www.youtube.com/watch?v=Trc8xsmFAM8"]
	return render_template("frame.html", pic=pic, name=name, material=material, style=style, size=size, use=use, fickness=fickness, motors=motors, FC=FC, video=video)

@app.route("/item/SABOTAGERC DINGO")
def SABOTAGERCDINGO():
	name = "SABOTAGERC DINGO"
	pic = "sabotagercdingo.jpg"
	material = "Carbon Fiber"
	style = "Stretch X"
	size = "3 inch"
	use = "raceing"
	fickness = "2 mm"
	motors = "2440 to 2660"
	FC = "40x40 mm"
	video = ["https://www.youtube.com/watch?v=sdMGdYoWjQY"]
	return render_template("frame.html", pic=pic, name=name, material=material, style=style, size=size, use=use, fickness=fickness, motors=motors, FC=FC, video=video)

@app.route("/item/TBS SOURCE ONE")
def TBSSOURSEONE():
	name = "TBS SOURSE ONE"
	pic = "tbssourseone.jpeg"
	material = "Carbon Fiber"
	style = "Stretch X"
	size = "6 inch"
	use = "free style, photography"
	fickness = "3.5 mm"
	motors = "2240 to 2880"
	FC = "40x40 and 60x60 mm"
	video = ["https://www.youtube.com/watch?v=60AvkzhMTYA"]
	return render_template("frame.html", pic=pic, name=name, material=material, style=style, size=size, use=use,
fickness=fickness, motors=motors, FC=FC, video=video)

 
# Fligth Controlers
@app.route("/flightcontroller")
def flightcontroller():
	intro = "The Flight Controler is the most important part of the drone.It is the brain and controls everything from speed to autolevel and have wild veriaty of options, therefore picking the right one for the rigth use is extreamly inportant."
	Kitems = ["KK 2.X"]
	Citems = ["CC3D"]
	Nitems = ["Naze32"]	
	return render_template("List.html", Kitems=Kitems,Citems=Citems, Nitems=Nitems, intro=intro)
@app.route("/item/KK 2.X")
def KK2X ():
	name = "KK 2.X"
	pic = "KK2x.jpeg"
	return render_template("Flightcontrollers.html", name=name, pic=pic)
@app.route("/item/CC3D")
def CC3D():
	name = "CC3D"
	pic = "CC3D.jpg"
	return render_template("Flightcontrollers.html", name=name, pic=pic)
@app.route("/item/Naze32")
def naze32():
	name = "Naze32"
	pic = "Naze32.jpg"
	return render_template("Flightcontrollers.html", name=name, pic=pic)

#Mottors
@app.route("/motors")
def motors():
	intro = "********************************** ********* * ************* ************* ************* ************ ***************** ****************** ***************** *********** * *************** ********** ************ *************** ************* ********** ** # Motors are Important!!!"
	Bitems = ["Brother Hobby Returner R6"]
	Ditems = ["Dragonfly Hurricane 2207"]
	Sitems = ["Sunnysky Edge Racing"]
	return render_template("List.html", intro=intro, Bitems=Bitems, Ditems=Ditems, Sitems=Sitems)
@app.route("/item/Brother Hobby Returner R6")
def brotherhobbyreturnerr6():
	name = "Brother Hobby Returner R6"
	pic = "brotherhobbyreturnerr6.jpeg"
	return render_template("Motors.html", name=name, pic=pic)
@app.route("/item/Dragonfly Hurricane 2207")
def dragonflyhurricane2207():
	name = "Dragonfly Hurricane 2207"
	pic = "dragonflyhurricane2207.jpg"
	return render_template("Motors.html", name=name, pic=pic)
@app.route("/item/Sunnysky Edge Racing")
def sunnyskyedgerasing():
	name = "Sunnysky Edge Racing"
	pic = "sunnyskyedgeracing.jpg"
	return render_template("Motors.html", name=name, pic=pic)
#ESC
@app.route("/esc")
def esc():
	intro = "************* ************* ************ ************* ************ ********** *  ************** ************* ************ ************ ************ ************** ************ ********** ************ ************ ************ ************* ************* ************ ************ ******** ESC."
	Ritems = ["Racerstar RS30A V2 ESC"]
	Ditems = ["DYS Aria 35A BLHeli_32 ESC"]
	Kitems = ["KISS 32A ESC"]
	return render_template("List.html", intro=intro, Ritems=Ritems, Ditems=Ditems, Kitems=Kitems)
@app.route("/item/Racerstar RS30A V2 ESC")
def raserstarrs30av2esc():
	name = "Racerstar RS30A V2 ESC"
	pic = "racerstarrs30av2esc.jpg"
	return render_template("ESC.html", name=name, pic=pic)
@app.route("/item/DYS Aria 35A BLHeli_32 ESC")
def dysaria35ablheli32esc():
	name = "DYS Aria 35A BLHeli_32 ESC"
	pic = "dysaria35ablheli32esc.jpg"
	return render_template("ESC.html", name=name, pic=pic)
@app.route("/item/KISS 32A ESC")
def kiss32aesc():
	name = "KISS 32A ESC"
	pic = "kiss32aesc.jpg"
	return render_template("ESC.html", name=name, pic=pic)

#Camera
@app.route("/camera")
def camra():
	intro = "************ ********** ************** *************** ************** ************** *********** ************** ************* ************* ************* ************** ************** **************** ************** *************** ************** *************** ************ *Cameras."
	Fitems = ["Foxeer Predator Micro"]
	Ritems = ["Runcam Micro Eagle"]
	Citems = ["Caddx Micro SDR1"]
	return render_template("List.html", intro=intro, Ritems=Ritems, Fitems=Fitems, Citems=Citems )
@app.route("/item/Foxeer Predator Micro")
def foxeerpredatormicro():
	name = "Foxeer Predator Micro"
	pic = "foxeerpredatormicro.jpg"
	return render_template("camera.html", name=name, pic=pic)
@app.route("/item/Runcam Micro Eagle")
def runcammicroeagle():
	name = "Runcam Micro Eagle"
	pic = "euncammicroeagle.png"
	return render_template("camera.html", name=name, pic=pic)
@app.route("/item/Caddx Micro SDR1")
def caddxmicrosdr1():
	name = "Caddx Micro SDR1"
	pic = "caddxmicrosdr1.png"
	return render_template("camera.html", name=name, pic=pic)

#Battery
@app.route("/battery")
def battery():
	intro = "Batteries are VERY important as if treated badly or missused or even poorly manifactured can EXPLODE and /or cath on FIRE. Choose cerfaly and buy the ones that we have tested and confurmed that are up to the manifacturer spesafications."
	Titems = ["Turnigy Graphene 4S 1300mah 65C","Tattu R-Line 1550","Tattu R-Line 4S 1300mAh 95C"]
	return render_template("List.html", intro=intro, Titems=Titems)
@app.route("/item/Turnigy Graphene 4S 1300mah 65C")
def turnigygraphene4s1300mah65c():
	name = "Turnigy Graphene 4S 1300mah 65C"
	pic = "turnigygraphene4s1300mah65c.jpg"
	return render_template("battery.html", name=name, pic=pic)
@app.route("/item/Tattu R-Line 1550")
def tatturline1550():
	name = "Tattu R-Line 1550"
	pic = "tatturline1550.jpg"
	return render_template("battery.html", name=name, pic=pic)
@app.route("/item/Tattu R-Line 4S 1300mAh 95C")
def tatturline4s1300mah95c():
	name = "Tattu R-Line 4S 1300mAh 95C"
	pic = "tatturline4s1300mah95c.jpg"
	return render_template("battery.html", name=name, pic=pic)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

