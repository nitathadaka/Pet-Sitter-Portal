import functools
from flask import Flask,render_template,request,redirect,session,url_for,Blueprint,flash,g
#from flaskext.mysql import MySQL
import MySQLdb
from wtforms import Form,TextField,BooleanField,PasswordField,validators
import os
from datetime import date

cur_dir = os.getcwd()

from werkzeug.utils import secure_filename

#upload_cat = cur_dir + '/static/cats'
upload_pets = cur_dir + '/static/pets'
upload_userpro = cur_dir + '/static/owners'
imgs_ext = set(['png','jpeg','jpg'])
app = Flask(__name__)

#session['userid'] = None

app.secret_key = 'random string'
app.config['upload_userpro'] = upload_userpro
app.config['upload_pets'] = upload_pets
#app.config['upload_cat'] = upload_cat

def connect2db():
	conn = MySQLdb.connect(host="localhost",user="root",passwd="lenix1998",db="happypaws")
	c = conn.cursor()
	return c,conn

#@app.route('/register',methods)

#conn = MySQLdb.connect(host = "localhost", user="root",password="lenix1998",db="minipro")
#cursor = conn.cursor()

#@app.route('')
#testing date time addition

def login_required(view):
	@functools.wraps(view)
	def wrapped(*args,**kwargs):
		if session.get('email') is None:
			return redirect(url_for('loginpage'))
		return view(*args,**kwargs)
	return wrapped


@app.route("/")
def main():
	try:
		return render_template('happypaws.html',loggedIn=session['loggedIn'],username=session['email'])
	except:
		return render_template('happypaws.html')

@app.route("/BecomeaHost")
@login_required
def host():
	if session.get('userid'):
		c,conn = connect2db()
		#usermail = session['email']
		#checkpro = c.execute("SELECT * from sitters WHERE uid = (%s)",[userid])
		userid = session['userid']
		loggedIn = session['loggedIn']
		data = c.execute("SELECT * FROM sitters WHERE uid = (%s)",[userid])
		data = c.fetchone()
		if data is None:
			return render_template("aaa.html",loggedIn=session['loggedIn'],username=session['email'])
		else:
			return redirect(url_for('userdisp'))
	else:
		error = "Login Required to Become a Sitter"
		return render_template('login.html',error=error)

@app.route("/AddaPet")
@login_required
def petadd():
	return render_template("addpet.html",loggedIn=session['loggedIn'],username=session['email'])

@app.route("/addPet",methods=["GET","POST"])
def addpet():
	if request.method == "POST":
		name = request.form['name']
		age = request.form['age']
		#ageint = int(float(age))
		category = request.form['category']
		breed = request.form['breed']
		image = request.files['file']
		description = request.form['description']

		if image:
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config['upload_pets'],filename))
		imagename = filename

		usermail = session['email']
		userid = session['userid']


		c,conn  = connect2db()
		c.execute("INSERT INTO pets (pname,category,breed,age,descrip,image,uid) VALUES(%s,%s,%s,%s,%s,%s,%s)",([name],[category],[breed],[age],[description],[imagename],[userid]))
		conn.commit()
		c.close()
		conn.close()
		return redirect(url_for('main'))
	else:
		return redirect('404.html')


@app.route("/addHost",methods=[ "GET" , "POST" ])
def addhost():
	if request.method == "POST":
		#redirect(url_for('petadd'))
		name = request.form['name']
		location = request.form['location']
		address = request.form['address']
		phone = request.form['phone']
		#use request.files to get user image
		charges = request.form['charges']
		image = request.files['file']
		description = request.form['description']
		profession = request.form['prof']

		if image:
			filename = secure_filename(image.filename)
			image.save(os.path.join(app.config['upload_userpro'],filename))
		imagename = filename
		usermail = session['email']
		userid = session['userid']


		c,conn = connect2db()
		c.execute("INSERT INTO sitters (sname,Location,Addr,phno,image,description,smail,uid,prof,charges) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",([name],[location],[address],[phone],[imagename],[description],[usermail],[userid],[profession],[charges]))
		session['acc'] = True
		conn.commit()
		c.close()
		conn.close()

		return render_template("happypaws.html",loggedIn=session['loggedIn'],username=session['email'])
	else:
		return redirect('404.html')

@app.route("/admindisplay")
def admindata():
	c,conn = connect2db()
	c.execute("SELECT * FROM sitters WHERE prof='Sitter'")
	datasitt = c.fetchall()
	c.execute("SELECT * FROM sitters WHERE prof = 'Owner'")
	dataowner = c.fetchall()
	c.execute("SELECT * FROM pets")
	datapets = c.fetchall()
	c.execute("SELECT * FROM transactions")
	datatrans = c.fetchall()

	c.execute("SELECT COUNT(*) FROM sitters WHERE prof='Sitter'");
	csit = c.fetchall()
	c.execute("SELECT COUNT(*) FROM sitters WHERE prof='Owner'");
	cowner = c.fetchall()
	c.execute("SELECT COUNT(*) FROM pets");

	c.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Accepted'")
	caccp = c.fetchall()
	c.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Rejected'")
	crejec = c.fetchall()
	c.execute("SELECT COUNT(*) FROM transactions WHERE status = 'request'")
	cpending = c.fetchall()
	cpet = c.fetchall()
	c.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Paid'")
	cpaid = c.fetchall()
	c.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Cancelled'")
	ccancel = c.fetchall()

	return render_template("test1.html",datasitt=datasitt,dataowner=dataowner,datapets=datapets,datatrans = datatrans,csit=csit,cowner=cowner,cpet=cpet,caccp=caccp, crejec=crejec ,cpending=cpending,cpaid=cpaid,ccancel=ccancel)


@app.route("/howitworks")
def howitworks():
	return render_template("how.html",loggedIn=True)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.route("/register/",methods=["GET","POST"])
def register_pager():
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']
		c,conn = connect2db()
		x = c.execute("SELECT * FROM logins WHERE umail = (%s)",[email])

		if x>0:
			error = "User Already Exists "
			return render_template('login.html',error=error)
		else:
			c.execute("INSERT INTO logins (umail,password) VALUES(%s,%s)",([email],[password]))
			conn.commit()
			c.close()

			c,conn = connect2db()
			session['email'] = email
			session['loggedIn'] = True
			c.execute("SELECT * FROM logins WHERE umail = (%s) AND password = (%s)",([email],[password]))
			data = c.fetchone()
			session['userid'] = data[0]
			return render_template('happypaws.html',loggedIn=session['loggedIn'],username=session['email'])
	else:
		return render_template('signup.html')


#TODO: add a users page with action to become a sitter
@app.route("/sittersid/<userid>")
@login_required
def sitterid(userid):
	c,conn = connect2db()
	c.execute("SELECT * FROM sitters WHERE sid = (%s)",[userid])
	data = c.fetchone()
	return render_template('sitterdetails.html',loggedIn=session['loggedIn'],data=data)


@app.route("/sitters/<username>")
@login_required
def sitter(username):
	c,conn = connect2db()
	c.execute("SELECT * FROM sitters WHERE sname = (%s)",[username])
	data = c.fetchone()
	return render_template('sitterdetails.html',loggedIn=session['loggedIn'],data=data)


@app.route("/petsss/<petid>")
def pett(petid):
	c,conn = connect2db()
	c.execute("SELECT * FROM pets WHERE pid = (%s)",[petid])
	data = c.fetchone()
	return render_template('petdetails.html',loggedIn=session['loggedIn'],data=data)

@app.route("/admin",methods=["GET","POST"])
def adminlogin():
	if request.method == "POST":
		adminuser = request.form["username"]
		adminpass = request.form["password"]
		c,conn = connect2db()
		try:
			c.execute("SELECT * FROM admin WHERE aname = (%s) AND apass = (%s)",([adminuser],[adminpass]))
			data = c.fetchone()
			if data is None:
				return redirect('adminlogin.html')
			else:
				session['email'] = adminuser
				session['password'] = adminpass
				session['loggedIn'] = True
				return redirect(url_for("admindata"))
		except :
			return redirect("adminlogin.html")
	else:
		return redirect("adminlogin.html")

@app.route("/payment/<transid>",methods=["GET","POST"])
@login_required
def payment(transid):
	c,conn = connect2db()
	if request.method == "POST":
		option = request.form["Pay"]
		c.execute("UPDATE transactions SET status='Paid' WHERE tid = (%s)",[transid])
		conn.commit()
		c.execute("SELECT petid FROM transactions WHERE tid = (%s)",[transid])
		pid = c.fetchone()
		c.execute("UPDATE transactions SET status='Cancelled' WHERE petid=(%s) AND tid != (%s)",([pid],[transid]))
		conn.commit()

		return redirect(url_for('myorders'))
	else:
		c.execute("SELECT totaldue FROM transactions WHERE tid = (%s)",[transid])
		due = c.fetchone()
		return render_template("payment.html",totaldue = due)

@app.route("/reject/<transid>")
@login_required
def reject(transid):
	c,conn = connect2db()
	c.execute("UPDATE transactions SET status='Cancelled' WHERE tid = (%s)",[transid])
	conn.commit()
	c.close()
	return redirect(url_for("myorders"))

@app.route("/login/",methods=["GET","POST"])
def loginpage():
	#loggedIn=False
	error = ''
	if request.method == "POST":
		attempted_username = request.form['username']
		attempted_password = request.form['password']
		#search in database
		c,conn = connect2db()

		try:
			c.execute("SELECT * FROM logins WHERE umail = (%s) AND password = (%s)",([attempted_username],[attempted_password]))
			data = c.fetchone()
			userid = data[0]
			if data is None:
				return redirect("eqagge.html")
			else:
				loggedIn=True
				session['email'] = attempted_username
				session['loggedIn'] = True
				session['userid'] = userid
				return render_template('happypaws.html',loggedIn=loggedIn,username=attempted_username)
		except:
			error = "Invalid Credentials"
			return render_template('login.html',error=error)
		#return render_template("login.html")
	else:
		return render_template('login.html')


@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/user")
def userdisp():
	if session.get('email') is None:
		return redirect(url_for('main'))
	else:
		c,conn = connect2db()
		#usermail = session['email']
		#checkpro = c.execute("SELECT * from sitters WHERE uid = (%s)",[userid])
		userid = session['userid']
		loggedIn = session['loggedIn']
		data = c.execute("SELECT * FROM sitters WHERE uid = (%s)",[userid])
		data = c.fetchone()
		if data is None:
			return render_template("redirect.html")
		else:
			return render_template("userdetails.html",data=data,loggedIn=loggedIn)

@app.route("/gui")
def testgui():
	if session.get('email') is None:
		return redirect(url_for('main'))
	else:
		c,conn = connect2db()
		#usermail = session['email']
		#checkpro = c.execute("SELECT * from sitters WHERE uid = (%s)",[userid])
		userid = session['userid']
		loggedIn = session['loggedIn']
		data = c.execute("SELECT * FROM sitters WHERE uid = (%s)",[userid])
		data = c.fetchone()
		if data is None:
			return render_template("redirect.html")
		else:
			return render_template("prof.html",data=data,loggedIn=loggedIn)

@app.route("/mypets")
@login_required
def pets():
	if session.get('userid'):
		userid = session['userid']
		c,conn = connect2db()
		c.execute("SELECT * FROM pets WHERE uid = (%s)",[userid])
		data = c.fetchall()
		return render_template("mypets.html",data=data,loggedIn=session['loggedIn'],username=session['email'])
	else:
		return render_template(url_for("main"))


@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('main'))

@app.route("/findsitters",methods=["GET","POST"])
@login_required
def findusers():
	if request.method == "POST":
		locate = request.form['location']
		c,conn = connect2db()
		userid = session['userid']
		c.execute("SELECT image,Addr,sname FROM sitters WHERE Location = (%s) AND available = 'Y' AND prof= 'Sitter' AND uid != (%s)" ,([locate],[userid]))
		data = c.fetchall()
		if session.get('loggedIn'):
			return render_template('dynamicsearch.html',data=data,loggedIn=session['loggedIn'],username=session['email'])
		else:
			return render_template('dynamicsearch.html',data=data)
	else:
		if session.get('loggedIn'):
			return render_template('dynamicsearch.html',loggedIn=session['loggedIn'],username=session['email'])
		else:
			return render_template('dynamicsearch.html')


@app.route("/test",methods=['GET','POST'])
def testingdate():
	if request.method == "POST":
		start = str(request.form['start'])
		start = start[0:10]
		end = str(request.form['end'])
		end = end[0:10]
		c,conn = connect2db()
		c.execute("INSERT INTO test (starttime,endtime) VALUES(%s,%s)",([start],[end]))
		conn.commit()
		c.close()
		return render_template('happypaws.html')

	else:
		return render_template('test.html')

# @app.route("/requests")
# def requestss():
# 	userid = session['userid']
# 	c,conn = connect2db()
# 	c.execute("SELECT * FROM pets WHERE uid = (%s)",[userid])
# 	data = c.fetchall()
# 	#return render_template("mypets.html",data=data)
# 	return render_template("request.html",data=data)

@app.route("/request/<sitname>",methods=["GET","POST"])
def requestsit(sitname):
	if request.method == "POST":
		petid = request.form['pet']
		description = request.form['reqtext']
		startdatetime = str(request.form['start'])
		startdate = startdatetime[0:10]
		enddatetime = str(request.form['end'])
		enddate = enddatetime[0:10]
		due = calculate(startdate,enddate)
		c,conn = connect2db()
		#sid = sitid
		c.execute("SELECT sid,charges FROM sitters WHERE sname = (%s)",[sitname])
		data = c.fetchone()
		situserid = data[0]
		charges = data[1]
		totaldue = charges*due
		userid = session['userid']
		status = "request"
		c.execute("SELECT * FROM pets WHERE uid = (%s)",[userid])
		datap = c.fetchall()
		#important (add auto_increment)
		c.execute("SELECT COUNT(*) FROM transactions WHERE sitterid = (%s) AND petid = (%s) AND status = 'request' ",([situserid],[petid]))
		dup = c.fetchone()
		if int(dup[0])>0:
			return render_template("request.html",error = "Already Sent",data=datap)
		else:
			c.execute("INSERT into transactions (ownerid,sitterid,petid,startdate,enddate,status,totaldue) VALUES (%s,%s,%s,%s,%s,%s,%s)",([userid],[situserid],[petid],[startdate],[enddate],[status],[totaldue]))
			conn.commit()
			c.close()
			return redirect(url_for('main'))
			
		
	else:
		userid = session['userid']
		c,conn = connect2db()
		c.execute("SELECT * FROM pets WHERE uid = (%s)",[userid])
		data = c.fetchall()
		return render_template("request.html",data=data)



@app.route('/editProfile',methods=["GET","POST"])
@login_required
def edit():
	c,conn = connect2db()
	userid = session['userid']
	c.execute("SELECT * FROM sitters WHERE uid = (%s)",[userid])
	data = c.fetchone()
	return render_template('editProfile.html',profileData = data)


@app.route('/updateProfile',methods=["GET","POST"])
@login_required
def update():
	if request.method == "POST":
		image = request.files['file']
		name = request.form['name']
		location = request.form['location']
		address = request.form['address']
		phone = request.form['phone']
		charges = request.form['charges']
		#image = request.files['file']
		#description = request.form['description']
		if image:
			filenames = secure_filename(image.filename)
			image.save(os.path.join(app.config['upload_userpro'],filenames))
		else:
			c,conn = connect2db()
			userid = session['userid']
			c.execute("SELECT image FROM sitters WHERE uid = (%s)",[userid])
			filenames = c.fetchone()

		imagename = filenames

		status = request.form['status']
		userid = session['userid']
		profession = request.form['prof']

		c,conn = connect2db()
		c.execute("UPDATE sitters SET image = (%s),sname = (%s),Location = (%s),Addr = (%s),phno = (%s),available = (%s),prof = (%s),charges = (%s) WHERE uid = (%s)",([imagename],[name],[location],[address],[phone],[status],[profession],[charges],[userid]))
		conn.commit()
		c.close()
		return redirect(url_for('userdisp'))
	else:
		return redirect(url_for('edit'))

@app.route("/transact/<tid>",methods=["GET","POST"])
def mytrans(tid):
	if request.method == "POST":
		status = request.form['status']
		c,conn = connect2db()
		userid = session['userid']
		c.execute("SELECT sid FROM sitters WHERE uid = (%s)",[userid])
		usersid = c.fetchone()
		c.execute("UPDATE transactions SET status  = (%s) WHERE sitterid = (%s) AND status = 'request' AND tid = (%s)",([status],[usersid],[tid]))
		conn.commit()
		c.close()
		return redirect(url_for('myorders'))
	else:
		return redirect(url_for('myorders'))


@app.route("/plot")
def chart():
	c,conn = connect2db()
	c.execute("SELECT COUNT(*) FROM sitters WHERE prof='Sitter'");
	csit = c.fetchall()
	c.execute("SELECT COUNT(*) FROM sitters WHERE prof='Owner'");
	cowner = c.fetchall()
	c.execute("SELECT COUNT(*) FROM pets");
	cpet = c.fetchall()
	return render_template("test_plot.html",csit=csit,cowner=cowner,cpet=cpet)

def calculate(start,end):
	startmonth = start[0:2]
	startdate = start[3:5]
	startyear = start[6:11]
	endmonth = end[0:2]
	enddate = end[3:5]
	endyear = end[6:11]
	a = date(int(endyear),int(endmonth),int(enddate))
	b = date(int(startyear),int(startmonth),int(startdate))
	x = (a-b).days
	return x

@app.route("/transactions",methods=["GET","POST"])
@login_required
def myorders():
	c,conn = connect2db()
	userid = session['userid']
	c.execute("SELECT sid FROM sitters WHERE uid = (%s)",[userid])
	usersid = c.fetchone()
	c.execute("SELECT * from transactions,sitters WHERE transactions.ownerid = (%s) AND sitters.sid = transactions.sitterid",[userid])
	datareqs = c.fetchall()
	c.execute("SELECT * FROM transactions,sitters WHERE transactions.sitterid = (%s) AND transactions.ownerid = sitters.uid ",[usersid])
	datasent = c.fetchall()
	c.execute("SELECT * from transactions,sitters WHERE transactions.ownerid = (%s) AND sitters.sid = transactions.sitterid AND status = 'Accepted'",[userid])
	dataacc = c.fetchall()

	return render_template('reqs.html',datareqs=datareqs,datasent=datasent,dataacc=dataacc)



if __name__ == '__main__':
	app.run(debug=True)
