from flask import Flask, render_template, request, redirect,session
from DBConnection import Db
import datetime

app = Flask(__name__)
app.secret_key="hc"

path="C:\\Users\\Nadakkal\\PycharmProjects\\untitled17\\static\\"
@app.route('/')
def login ():
    return render_template('medical council/med log.html')
@app.route('/loginpost',methods=['post'])
def loginpost():
    user=request.form['textfield']
    password=request.form['textfield2']
    Db1=Db()
    qry=Db1.selectOne('select * from login where username="'+user+'" and password="'+password+'" ')
    print(qry)
    if qry is not  None:
        type=qry['usertype']
        session['loginid']=qry['Log_id']
        print(type,str(session['Log_id']))
        if type=='admin':
            return medicalcouncilhome()
        elif type=='hospital':
            return hospitalhome()
        else:
            return '<script>alert("Invalid User");window.location="/"</script>'
    else:
        return '<script>alert("Invalid User");window.location="/"</script>'
# ===================================================================================================
@app.route('/pharmacy_reg')
def pharmacy_reg():
    return render_template('pharmacyreg.html')
@app.route('/pharmacylog',methods=['post'])
def pharamacylog():
    pharmacyname=request.form['textfield']
    Licencenumber=request.form['textfield2']
    place=request.form['textfield3']
    postoffice=request.form['textfield4']
    pin=request.form['textfield5']
    district=request.form['select']
    phonenumber=request.form['textfield6']
    emailid=request.form['textfield7']
    photo=request.files['fileField']
    workingtime=request.form['textarea']
    password=request.form['textfield9']
    confirmpassword=request.form['textfield10']

    Db1=Db()
    qry2=Db1.selectOne("select * from login where username='"+emailid+"'")
    if qry2 is None:
        if password==confirmpassword:
            data=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            photo.save(path+"profilephoto\\"+data+".jpg")
            path1="/static/profilephoto/"+data+".jpg"
            qry=Db1.insert("insert into login(username,password,usertype) values('"+emailid+"','"+password+"','pending')")
            qry1=Db1.insert("insert into pharmacy(ph_id,licience_no,ph_name,place,pin,post,district,phone_number,email_id,photo,working_time) values('"+str(qry)+"','"+Licencenumber+"','"+pharmacyname+"','"+place+"','"+pin+"','"+postoffice+"','"+district+"','"+phonenumber+"','"+emailid+"','"+path1+"','"+workingtime+"')")
            return "<script>alert('successfully inserted');window.location='/pharmacy_reg'</script>"
        else:
            return '<script>alert("Password does not match");window.location="/pharmacy_reg"</script>'
    else:
        return '<script>alert("Email alredy exsisting......");window.location="/pharmacy_reg"</script>'


# ===================================================================================================


@app.route('/lab_reg')
def lab_reg():
    return render_template('lab reg.html')
@app.route('/lablog',methods=['post'])
def lablog():
    labname=request.form['textfield2']
    licence=request.form['textfield']
    place=request.form['textfield3']
    post=request.form['textfield9']
    pin=request.form['textfield4']
    dis=request.form['select']
    phoneno=request.form['textfield5']
    email=request.form['textfield6']
    photo=request.files['fileField2']
    workingtime=request.form['textarea2']
    passwd=request.form['textfield7']
    conpasswd=request.form['textfield8']
    Db1=Db()
    qry2=Db1.selectOne("select * from login where  username='"+email+"'")
    if qry2 is None:
        if passwd==conpasswd:
            data=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            photo.save(path+"profilephoto\\"+data+".jpg")
            path1="/static/profilephoto/"+data+".jpg"
            qry=Db1.insert("insert into login(username,password,usertype) values('"+email+"','"+passwd+"','pending')")
            qry1=Db1.insert("insert into lab(Lab_id,L_name,L_place,L_post,L_pincode,L_district,L_phonenumber,L_emailid,L_workingtime,photo,L_licencenumber) values ('"+str(qry)+"','"+labname+"','"+place+"','"+post+"','"+pin+"','"+dis+"','"+phoneno+"','"+email+"','"+workingtime+"','"+path1+"','"+licence+"')")
            return "<script>alert('successfully inserted');window.location='/lab_reg'</script>"
        else:
            return '<script>alert("Password does not match");window.location="/lab_reg"</script>'
    else:
        return '<script>alert("Email alredy exsisting......");window.location="/lab_reg"</script>'




# ======================================================================================================

@app.route('/hospital_reg')
def hospital_reg():
    return render_template('hospital reg.html')
@app.route('/hospitallog',methods=['post'])
def hospitallog():
    hospitalname=request.form['textfield']
    licenseno=request.form['textfield2']
    place=request.form['textfield3']
    postoffice=request.form['textfield4']
    pin=request.form['textfield5']
    district=request.form['select']
    phoneno=request.form['textfield6']
    email=request.form['textfield7']
    photo=request.files['fileField']
    password=request.form['textfield8']
    confirmpassword=request.form['textfield9']
    Db1 = Db()
    qry2 = Db1.selectOne("select * from login where username='" + email + "'")
    if qry2 is None:
        if password == confirmpassword:
            data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            photo.save(path + "profilephoto\\" + data + ".jpg")
            path1 = "/static/profilephoto/" + data + ".jpg"
            qry=Db1.insert("insert into login(username,password,usertype) values('"+email+"','"+password+"','pending')")
            qry1=Db1.insert("insert into hospital(h_id,h_name,h_place,h_pin,h_post,h_district,h_phonenumber,h_emailid,h_photo,h_licencenumber) values('"+str(qry)+"','"+hospitalname+"','"+place+"','"+pin+"','"+postoffice+"','"+district+"','"+phoneno+"','"+email+"','"+path1+"','"+licenseno+"')")
            return "<script>alert('successfully inserted');window.location='/hospital_reg'</script>"
        else:
            return '<script>alert("Password does not match");window.location="/hospital_reg"</script>'
    else:
        return '<script>alert("Email alredy exsisting......");window.location="/hospital_reg"</script>'













# ====================================================================================================




@app.route('/view_pharmacy')
def view_pharmacy():
    Db1=Db()
    qry=Db1.select("select * from pharmacy,login where login.Log_id=pharmacy.ph_id and usertype='pending'")
    return render_template('medical council/view phar.html',data=qry)

@app.route('/approve_pharmacy/<i>')
def approve_pharmacy(i):
    d=i
    Db1 = Db()
    qry = Db1.selectOne("select * from pharmacy where ph_id='"+d+"'")
    return render_template('medical council/app phar.html',data=qry)
@app.route('/approve_pharmacypost/<i>',methods=['post'])
def approve_pharmacypost(i):
    d=i

    Db1 = Db()
    btn1=request.form['btn']
    print(btn1)
    if btn1=='Approve':
        qry=Db1.update("update login set usertype='pharmacy' where Log_id='"+d+"'")
        return view_pharmacy()
    else:
        qry = Db1.update("update login set usertype='rejected' where Log_id='" + d + "'")
        return view_pharmacy()






# ========================================================================================================
@app.route('/view_lab')
def view_lab():
    Db1=Db()
    qry=Db1.select("select * from lab,login where login.Log_id=lab.Lab_id and usertype='pending'")
    return render_template('medical council/view lab.html',data=qry)
@app.route('/approve_lab/<i>')
def approve_lab(i):
    d=i
    Db1=Db()
    qry=Db1.selectOne("select * from lab where Lab_id='"+d+"'")
    return render_template('medical council/app Lab .html',data=qry)
@app.route('/appove_labpost/<i>',methods=['post'])
def appove_labpost(i):
    d=i
    Db1=Db()
    ab=request.form['ab']
    print(ab)
    if ab=='Approve':
        qry=Db1.update("update login set usertype='Hospital' where Log_id='"+d+"'")
        return view_lab()
    else:
        qry=Db1.update("update login set usertype='Rejected' where Log_id='"+d+"'")
        return view_lab()

# =============================================================================================================
@app.route('/view_hospital')
def view_hospital():
    Db1=Db()
    qry=Db1.select("select * from hospital,login where login.Log_id=hospital.h_id and login.usertype='pending'")
    return render_template('medical council/view hos.html',data=qry)



@app.route('/approve_hospital/<i>')
def approve_hospital (i):
    d=i
    Db1=Db()
    qry=Db1.selectOne("select * from hospital where h_id='"+d+"'")
    return render_template('medical council/app hos .html',data=qry)
@app.route('/approve_hospitalpost/<i>',methods=['post'])
def approve_hospitalpost(i):
    d=i
    Db1=Db()
    abc=request.form['abc']
    if abc=='Approve':
        qry=Db1.update("update login set usertype='hospital' where Log_id='"+d+"'")
        return view_hospital()
    else:
        qry=Db1.update("update login set usertype='Rejected' where Log_id='"+d+"'")
        return view_hospital()



# ===========================================================================================
@app.route('/medicine_management')
def medicine_management():
    return render_template('medical council/med man.html')
@app.route('/medicinpost',methods=['post'])
def medicinpost():
    medicinename=request.form['m1']
    incrediant=request.form['n1']
    price=request.form['m2']
    purpose=request.form['n2']
    sideeffect=request.form['n3']
    photo=request.files['b1']
    data = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    photo.save(path + "profilephoto\\" + data + ".jpg")
    path1 = "/static/profilephoto/" + data + ".jpg"
    Db1=Db()
    qry=Db1.insert(" insert into medicine (Medicine_Name,Incrediants,Side_effects,Purpose,Price,photo) values('"+medicinename+"','"+incrediant+"','"+sideeffect+"','"+purpose+"','"+price+"','"+path1+"')")
    return redirect('/medicine_management')

@app.route('/view_medicine')
def view_medicine ():
    Db1=Db()
    qry=Db1.select("select * from  medicine")
    return render_template('medical council/Med view.html',data=qry)
@app.route('/viewmore_medicine/<i>')
def viewmore_medicine(i):
    d=i

    Db1=Db()
    qry=Db1.selectOne("select * from medicine where mid='"+d+"'")
    return render_template('medical council/med view more.html',data=qry)
@app.route('/medicine_updatedlt/<i>',methods=['post'])
def medicine_updatedlt(i):
    d=i
    btn=request.form['Add']
    if btn=="Delete":
        Db1 = Db()
        qry = Db1.delete("delete  from  medicine where mid='"+d+"'")

        return "ok"
    else:
        return "updated...."
# ===================================================================================================


# @app.route('/add_medicine')
# def add_medicine():
#     return render_template('medical council/add med sum.html')
@app.route('/view_payment')
def view_payment():
    return render_template('medical council/Payment.html')
@app.route('/payment_details')
def payment_details ():
    return render_template('medical council/user datails sumb.html')
@app.route('/lab_view')
def lab_view():
    return render_template('medical council/laboratary.html')

@app.route('/pharmacy_view')
def pharmacy_view ():
    return render_template('medical council/pharmacy.html')
@app.route('/hospital_view')
def hospital_view ():
    return render_template('medical council/hospital.html')
@app.route('/viewmore_lab')
def viewmore_lab():
    return render_template('medical council/laboratary view.html')

@app.route('/viewmore_pharmacy')
def viewmore_pharmacy():
    return render_template('medical council/pharmacy view.html')
@app.route('/viewmore_hospital')
def viewmore_hospital ():
    return render_template('medical council/hospital view.html')
@app.route('/view_doctor')
def view_doctor():
    return render_template('medical council/view doctors.html')
@app.route('/review_doctor')
def review_doctor():
    return render_template('medical council/review dot.html')

@app.route('/review_pharmacy')
def review_pharmacy():
    return render_template('medical council/review ph.html')
@app.route('/review_hospital')
def review_hospital ():
    return render_template('medical council/review hos.html')
@app.route('/review_lab')
def review_lab():
    return render_template('medical council/review lab.html')

@app.route('/view_forward')
def view_forward():
    return render_template('medical council/view and forward.html')

@app.route('/history')
def history():
    return render_template('medical council/History.html')
@app.route('/prescription')
def prescription():
    return render_template('medical council/Prescription.html')

@app.route('/medicalcouncilhome')
def medicalcouncilhome():
    return render_template('medical council/medicalcouncilhome.html')


if __name__ == '__main__':
    app.run()
