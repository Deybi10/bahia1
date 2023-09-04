from flask import Flask, render_template, redirect, url_for, request,session,make_response,abort,json
from werkzeug.utils import secure_filename
from flask_login import LoginManager, logout_user, login_required,current_user ,login_user,UserMixin  # pip install Flask-Login
import stripe   # pip install stripe
import os
from datetime import datetime
from flask_wtf.csrf import CSRFProtect   #from flask_wtf import FlaskForm,CSRFProtect  # pip install Flask-WTF
from sqlalchemy import ForeignKey,Column,String,Integer,CHAR,Numeric,Float,Boolean,DECIMAL,DateTime,create_engine
from sqlalchemy.ext.declarative import declarative_base
#import pdfkit   # pip install pdfkit    pip install wkhtmltopdf
from sqlalchemy.orm import sessionmaker,scoped_session,relationship
app = Flask(__name__, static_folder="static", template_folder="templates")
#app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
csrf = CSRFProtect(app)  
#engine=create_engine('mysql://root:zzxx@localhost/bahia1')  # ,echo=True
#engine=create_engine('mysql://bahia1_user:@db4free.net/bahia11')  # ,echo=True
engine=create_engine('postgresql://bahia1_user:lD83Npcsk32SSn3elsL1jwyqw7nBdilt@dpg-cjpchde1208c739pc5p0-a/bahia1')  # ,echo=True
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars_api"
Model=declarative_base()
db=scoped_session(sessionmaker(engine))
class sub_cat(Model):
    __tablename__ = "sub_cat"
    id = Column(Integer,primary_key=True)                            
    nombre=Column(String(30))
    relacion2 = relationship("articulos", back_populates="relacion3" ) # backref="categoriasx"'''
############################################################
class articulos(Model):
    __tablename__ = "articulos"
    id = Column(Integer,autoincrement=True,primary_key=True);          nombre = Column(String(50), nullable=False)   # unique=True
    precio = Column(Float, default=0);                                 iva = Column(Float,default=0.12,nullable=False)
    descripcion = Column(String(50))                           
    imagen = Column(String(50))
    #imagen2 = Column(String(50))   #imagen3 = Column(String(50))
    stock = Column(Integer, default=1)
    cat_id = Column(Integer, ForeignKey('sub_cat.id'),default=1,nullable=False)
    relacion3 = relationship("sub_cat", back_populates="relacion2")
###########################################################
class usuarios(Model):        # UserMixin ya implementa x interno flask-login
    __tablename__ = "usuarios"
    id = Column(Integer,autoincrement=True, primary_key=True);           nombre = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False);                       password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False);                         admin = Column(Boolean,default=False)
    #fecha = Column(DateTime, default=datetime.now)
    fecha = Column(DateTime, default=datetime.today)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)#return unicode(self.id) 
    def is_admin(self):
        return self.admin  # True+False=1  True+True=2   print(true)=True   False+False=0
Model.metadata.create_all(engine)
#Model.metadata.create_all(bind=engine)
try:
    query1=usuarios(nombre="dave",username="davex",password="dave10",email="gdave0930@gmail.com",admin=True)
    query2=usuarios(nombre="dave",username="deybi",password="qqww",email="gdave0930@gmail.com",admin=False)

    query3=sub_cat(id=1,nombre="blusas")
    query4=sub_cat(id=2,nombre="Faldas/vestidos")
    query5=sub_cat(id=3,nombre="calzado-damas")
    query6=sub_cat(id=4,nombre="accesorio")

    query7=sub_cat(id=5,nombre="camisas/camisetas")
    query8=sub_cat(id=6,nombre="Pantalones")
    query9=sub_cat(id=7,nombre="calzado-caballeros")
    query10=sub_cat(id=8,nombre="accesorio")

    query11=sub_cat(id=9,nombre="blusas")
    query12=sub_cat(id=10,nombre="Faldas/vestidos")
    query13=sub_cat(id=11,nombre="calzado-niña")
    query14=sub_cat(id=12,nombre="accesorio-niño")

    query15=sub_cat(id=13,nombre="camisa/camisetas")
    query16=sub_cat(id=14,nombre="Pantalones")
    query17=sub_cat(id=15,nombre="calzado-niño")
    query18=sub_cat(id=16,nombre="accesorio-niña")
    # mujer
    query19=articulos(imagen="blusa1.webp",nombre="ok1",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=1) 
    query20=articulos(imagen="blusa2.webp",nombre="ok2",precio=20.22,iva=0.12,descripcion="xxx",stock=2,cat_id=1)
    query21=articulos(imagen="chaqueta1.webp",nombre="ok3",precio=30.22,iva=0.12,descripcion="xxx",stock=3,cat_id=1)
    query22=articulos(imagen="chaqueta-casual1.jpg",nombre="ok4",precio=40.22,iva=0.12,descripcion="xxx",stock=4,cat_id=1)

    query23=articulos(imagen="falda1.jpg",nombre="ok5",precio=10.22,iva=0.12,descripcion="xxx",stock=5,cat_id=2) 
    query24=articulos(imagen="falda2.jpg",nombre="ok6",precio=20.22,iva=0.12,descripcion="xxx",stock=6,cat_id=2)
    query25=articulos(imagen="vestido1.jpg",nombre="ok7",precio=30.22,iva=0.12,descripcion="xxx",stock=7,cat_id=2)
    query26=articulos(imagen="vestido2.jpg",nombre="ok8",precio=40.22,iva=0.12,descripcion="xxx",stock=8,cat_id=2)

    query27=articulos(imagen="zapato1.webp",nombre="ok9",precio=10.22,iva=0.12,descripcion="xxx",stock=9,cat_id=3)
    query28=articulos(imagen="zapato6.jpg",nombre="ok10",precio=20.22,iva=0.12,descripcion="xxx",stock=10,cat_id=3)
    query29=articulos(imagen="zapato11.jpg",nombre="ok11",precio=30.22,iva=0.12,descripcion="xxx",stock=11,cat_id=3)
    query30=articulos(imagen="zapato2.webp",nombre="ok12",precio=40.22,iva=0.12,descripcion="xxx",stock=12,cat_id=3)

    query31=articulos(imagen="cartera1.png",nombre="ok13",precio=10.22,iva=0.12,descripcion="xxx",stock=13,cat_id=4) 
    query32=articulos(imagen="cartera2.jpg",nombre="ok14",precio=20.22,iva=0.12,descripcion="xxx",stock=14,cat_id=4)
    query33=articulos(imagen="gafa1.webp",nombre="ok15",precio=30.22,iva=0.12,descripcion="xxx",stock=15,cat_id=4)
    query34=articulos(imagen="gafa2.webp",nombre="ok16",precio=40.22,iva=0.12,descripcion="xxx",stock=16,cat_id=4)
    # hombre
    query35=articulos(imagen="zcamisa1.jpg",nombre="ok17",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=5) 
    query36=articulos(imagen="zcamisa2.webp",nombre="ok18",precio=20.22,iva=0.12,descripcion="xxx",stock=2,cat_id=5)
    query37=articulos(imagen="zcamisa3.webp",nombre="ok19",precio=30.22,iva=0.12,descripcion="xxx",stock=3,cat_id=5)
    query38=articulos(imagen="zcamisa4.webp",nombre="ok20",precio=40.22,iva=0.12,descripcion="xxx",stock=4,cat_id=5)

    query39=articulos(imagen="zpantalon-h1.webp",nombre="ok21",precio=10.22,iva=0.12,descripcion="xxx",stock=5,cat_id=6) 
    query40=articulos(imagen="zpantalon-h2.jpeg",nombre="ok22",precio=20.22,iva=0.12,descripcion="xxx",stock=6,cat_id=6)
    query41=articulos(imagen="zpantalon-h3.jpg",nombre="ok23",precio=30.22,iva=0.12,descripcion="xxx",stock=7,cat_id=6)
    query42=articulos(imagen="zpantalon-h6.webp",nombre="ok24",precio=40.22,iva=0.12,descripcion="xxx",stock=8,cat_id=6)

    query43=articulos(imagen="zapato-h1.jpg",nombre="ok25",precio=10.22,iva=0.12,descripcion="xxx",stock=9,cat_id=7) 
    query44=articulos(imagen="zapato-h2.webp",nombre="ok26",precio=20.22,iva=0.12,descripcion="xxx",stock=10,cat_id=7)
    query45=articulos(imagen="zapato-h13.jpg",nombre="ok27",precio=30.22,iva=0.12,descripcion="xxx",stock=11,cat_id=7)
    query46=articulos(imagen="zapato-h5.jpg",nombre="ok28",precio=40.22,iva=0.12,descripcion="xxx",stock=12,cat_id=7)

    query47=articulos(imagen="zgafa-h1.jpg",nombre="ok29",precio=10.22,iva=0.12,descripcion="xxx",stock=13,cat_id=8) 
    query48=articulos(imagen="zgorra-h1.jpg",nombre="ok30",precio=20.22,iva=0.12,descripcion="xxx",stock=14,cat_id=8)
    query49=articulos(imagen="zgafa-h1.jpg",nombre="ok31",precio=30.22,iva=0.12,descripcion="xxx",stock=15,cat_id=8)
    query50=articulos(imagen="zgorra-h1.jpg",nombre="ok32",precio=40.22,iva=0.12,descripcion="xxx",stock=16,cat_id=8)
    # niños
    query51=articulos(imagen="zcamisa-niño1.jpg",nombre="ok33",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=9) 
    query52=articulos(imagen="zcamisa-niño2.webp",nombre="ok34",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=9)
    query53=articulos(imagen="zcamisa-niño3.jpg",nombre="ok35",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=9)
    query54=articulos(imagen="zcamisa-niño5.jpg",nombre="ok36",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=9)

    query55=articulos(imagen="zpantalon-niño1.webp",nombre="ok37",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=10) 
    query56=articulos(imagen="zpantalon-niño3.jpg",nombre="ok38",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=10)
    query57=articulos(imagen="zpantalon-niño2.jpg",nombre="ok39",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=10)
    query58=articulos(imagen="zpantalon-niño3.jpg",nombre="ok40",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=10)

    query59=articulos(imagen="zapato-niño2.jpg",nombre="ok41",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=11)
    query60=articulos(imagen="zapato-niño3.webp",nombre="ok42",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=11)
    query61=articulos(imagen="zapato-niño5.jpg",nombre="ok43",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=11)
    query62=articulos(imagen="zapato-niño7.jpg",nombre="ok44",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=11)

    query63=articulos(imagen="zgorra-niño1.jpg",nombre="ok45",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=12) 
    query64=articulos(imagen="zgorra-niño2.jpg",nombre="ok46",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=12)
    query65=articulos(imagen="zgorra-niño3.jpg",nombre="ok47",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=12)
    query66=articulos(imagen="zgorra-niño4.jpg",nombre="ok48",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=12)
    # niñas
    query67=articulos(imagen="zblusa-niña1.png",nombre="ok49",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=13) 
    query68=articulos(imagen="zblusa-niña2.jpg",nombre="ok50",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=13)
    query69=articulos(imagen="zblusa-niña3.png",nombre="ok51",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=13)
    query70=articulos(imagen="zblusa-niña4.webp",nombre="ok52",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=13)

    query71=articulos(imagen="zpantalon-niña1.webp",nombre="ok53",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=14) 
    query72=articulos(imagen="zpantalon-niña2.webp",nombre="ok54",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=14)
    query73=articulos(imagen="zpantalon-niña3.webp",nombre="ok55",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=14)
    query74=articulos(imagen="zvestido-niña2.webp",nombre="ok56",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=14)

    query75=articulos(imagen="zapato-niña1.jpg",nombre="ok57",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=15) 
    query76=articulos(imagen="zapato-niña3.webp",nombre="ok58",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=15)
    query77=articulos(imagen="zapato-niña4.jpg",nombre="ok59",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=15)
    query78=articulos(imagen="zapato-niña5.webp",nombre="ok60",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=15)

    query79=articulos(imagen="zgafa-niña1.jpeg",nombre="ok61",precio=10.22,iva=0.12,descripcion="xxx",stock=1,cat_id=16) 
    query80=articulos(imagen="zgafa-niña2.jpg",nombre="ok62",precio=20.22,iva=0.12,descripcion="xxx",stock=1,cat_id=16)
    query81=articulos(imagen="zgafa-niña3.jpg",nombre="ok63",precio=30.22,iva=0.12,descripcion="xxx",stock=1,cat_id=16)
    query82=articulos(imagen="zgafa-h1.jpg",nombre="ok64",precio=40.22,iva=0.12,descripcion="xxx",stock=1,cat_id=16)
    db.add_all([query1,query2,query3,query4,query5,query6,query7,query8,query9,query10,query11,query12,query13,query14,query15,query16,query17,query18,
                query19,query20,query21,query22,query23,query24,query25,query26,query27,query28,query29,query30,query31,query32,query33,query34,query35,
                query36,query37,query38,query39,query40,query41,query42,query43,query44,query45,query46,
                query47,query48,query49,query50,query51,query52,query53,query54,query55,query56,query57,query58,query59,query60,
                query61,query62,query63,query64,query65,query66,query67,query68,query69,query70,query71,query72,query73,query74,
                query75,query76,query77,query78,query79,query80,query81,query82])
    db.commit()
except:
    pass

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "loginx"

@login_manager.user_loader
def load_user(user_id): return db.query(usuarios).get(int(user_id))

@app.route("/logout")
def logoutx():
    logout_user()
    return redirect("login")
########################################################## login #############################################
@app.route('/login', methods=['get', 'post'])
def loginx():
    msg=""
    if request.method == 'POST':       #if flask.request.method == 'GET':
        #usernamex = request.form['username']; passwordx = request.form['password']
        #remember = True if request.form.get('remember') else False
        existe_usuario = db.query(usuarios).filter_by(username=request.form['username'], password=request.form['password']).first()
        if existe_usuario is not None:
            #session['admin'] = current_user.username
            #login_user(existe_usuario,remember=remember)
            session['loggedin'] = True
            session['id'] = existe_usuario.id
            login_user(existe_usuario)
            return redirect("/")
        else:
            msg="credenciales invalidas"
    return render_template('usuarios/login-form-normal.html',msg=msg)

@app.route("/registro", methods=["get", "post"])
def registrox():
    msg=""
    if request.method == 'POST':
        nombre = request.form['nombre']; usernamex = request.form['username']; passwordx = request.form['password']; email = request.form['email']
        userx = db.query(usuarios).filter_by(username=usernamex).first()
        msg = "usuario ya existe"
        if userx is None and current_user.is_authenticated:
            user = usuarios(username=usernamex,password=passwordx,nombre=nombre,email=email)  # ,admin=admin
            user.admin=True
            db.add(user), db.commit()
            msg="se registro con exito un admin"   #return redirect("/login")
        elif userx is None and not current_user.is_authenticated:
            user = usuarios(username=usernamex,password=passwordx,nombre=nombre,email=email)  # ,admin=admin
            user.admin=False
            db.add(user), db.commit()
            msg="se registro con exito"   #return redirect("/login")
    return render_template("usuarios/register-normal.html",msg=msg)
#####################################################################################################
@app.route('/detalles/<id>', methods=["get","post"])
def detallesx(id):
    product = db.query(articulos).filter_by(id=id).first()
    #product = db.query(articulos).filter_by(id=id) # este si es iterable
    #artx = Articulos.query.get(id) # este no es iterable
    #product = db.query(articulos).get(id=1) # este no es iterable
    #product = db.query(articulos).filter_by(cat_id=id) # este no es iterable
    request.form.get("id"==id)
    #request.form.get(id==id)
    if request.method == 'POST' and product.stock >= int(request.form['cantidad']):   #if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        #artx.stock >= cantidadx
        #pass
        try: datos = json.loads(request.cookies.get(str(current_user.id)))
        except:
            datos = []
        actualizar = False
        for x in datos:
            print(x) # {"id": "1" , "cantidad": 1}
            if x["id"] == id:
                #contador + 1
                x["cantidad"] = cantidadx     #x["cantidad"] = int(request.form['cantidad'])
                actualizar = True
        if not actualizar:
            datos.append({"id": id , "cantidad": cantidadx})
        resp = make_response(redirect(url_for('inicio1')))
        resp.set_cookie(str(current_user.id), json.dumps(datos)) # set_cookie
        return resp
    return render_template("detalles.html", product=product)
##############################################################  inicio  #######################################################
@app.route('/')
@app.route('/inicio')
@app.route('/inicio/<id>', methods=["get", "post"]) # "/carrito1"
def inicio1(id=1):
    cat_1 = db.query(sub_cat).filter_by(id=1)
    cat_2 = db.query(sub_cat).filter_by(id=2)
    cat_3 = db.query(sub_cat).filter_by(id=3)
    cat_4 = db.query(sub_cat).filter_by(id=4)
    cat_5 = db.query(sub_cat).filter_by(id=5)
    cat_6 = db.query(sub_cat).filter_by(id=6)
    cat_7 = db.query(sub_cat).filter_by(id=7)
    cat_8 = db.query(sub_cat).filter_by(id=8)
    cat_9 = db.query(sub_cat).filter_by(id=9)
    cat_10 = db.query(sub_cat).filter_by(id=10)
    cat_11 = db.query(sub_cat).filter_by(id=11)
    cat_12 = db.query(sub_cat).filter_by(id=12)
    cat_13 = db.query(sub_cat).filter_by(id=13)
    cat_14 = db.query(sub_cat).filter_by(id=14)
    cat_15 = db.query(sub_cat).filter_by(id=15)
    cat_16 = db.query(sub_cat).filter_by(id=16)
    art1 = db.query(articulos).filter_by(cat_id=id)#.all() # este si es iterable
    artx = db.query(articulos).get(id) # este no es iterable
    request.form.get("id"==id)
    if request.method == 'POST' and artx.stock >= int(request.form['cantidad']):   #if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        try: datos = json.loads(request.cookies.get(str(current_user.id)))
        except:
            datos = []
        actualizar = False
        for x in datos:
            print(x) # {"id": "1" , "cantidad": 1}
            if x["id"] == id:
                #contador + 1
                x["cantidad"] = cantidadx     #x["cantidad"] = int(request.form['cantidad'])
                actualizar = True
        if not actualizar:
            datos.append({"id": id , "cantidad": cantidadx})
        resp = make_response(redirect(url_for('inicio1')))
        resp.set_cookie(str(current_user.id), json.dumps(datos)) # set_cookie
        return resp
    return render_template("index-grid1.html", articulos=art1, cat_1=cat_1,cat_2=cat_2,cat_3=cat_3,cat_4=cat_4,cat_5=cat_5,cat_6=cat_6,cat_7=cat_7,cat_8=cat_8,
                           cat_9=cat_9,cat_10=cat_10,cat_11=cat_11,cat_12=cat_12,cat_13=cat_13,cat_14=cat_14,cat_15=cat_15,cat_16=cat_16)
########################################################################## categorias ##################################################
@app.route('/categorias')
def categoriasxx():
    categorias = db.query(sub_cat).all()
    return render_template("categorias/categorias.html", categorias=categorias)

@app.route('/categoria_new', methods=["get", "post"])
@login_required
def categoria_newx():
    if request.method == 'POST':
        cat = sub_cat(nombre=request.form['nombre'])
        #nombrex = request.form['nombre']
        #cat = categoriasx(nombre=nombrex)
        db.add(cat), db.commit()
        return redirect("categorias")
    return render_template("categorias/categoria-new.html")

@app.route('/update_categoria/<id>', methods=["get", "post"])
@login_required
def update_categoriax(id):
    cat = db.query(sub_cat).get(id)
    #cat = db.query(categoriasx).update(nombre=id)
    #cat = db.execute(categoriasx)
    if request.method == 'POST':
        cat.nombre = request.form['nombre']
        db.commit()
        return redirect("/categorias")
    return render_template("categorias/categoria-update.html", cat=cat)

@app.route('/delete_categoria/<id>', methods=["get", "post"])
@login_required
def delete_categoriax(id):
    cat = db.query(sub_cat).get(id)
    if request.method == 'POST':
        if id>"1" and request.form['si']:  # no se puede eliminar categoria 1, elimina la categoria q sea 2 o superior
            db.delete(cat), db.commit()
            return redirect("/categorias")
    return render_template("categorias/categorias_delete.html",cat=cat)
###################################################  articulos  ########################################################
@app.route('/articulos', methods=["get", "post"])
def articulosx():
    cat1 = db.query(articulos).filter_by(categoria_id=1) # este si es iterable
    cat2 = db.query(articulos).filter_by(categoria_id=2) # este si es iterable
    cat3 = db.query(articulos).filter_by(categoria_id=3) # este si es iterable
    cat4 = db.query(articulos).filter_by(categoria_id=4) # este si es iterable
    cat5 = db.query(articulos).filter_by(categoria_id=5) # este si es iterable
    cat6 = db.query(articulos).filter_by(categoria_id=6) # este si es iterable
    return render_template("articulos/lista-articulos.html", cat1=cat1, cat2=cat2, cat3=cat3, cat4=cat4, cat5=cat5, cat6=cat6)

@app.route('/articulo_new', methods=["get", "post"])
@login_required
def articulo_newx():
    categorias = db.query(sub_cat).all()
    #categorias = db.query(cat_mujer).join(cat_hombre)
    if request.method == 'POST':
        filex1 = request.files["imagenx"]
        #filex2 = request.files["imagen2"]
        #filex3 = request.files["imagen3"]
        nombre = request.form['nombre']; precio = request.form['precio']; iva = request.form['iva']; descripcion = request.form['descripcion']
        stock = request.form['stock']; categoria_id = request.form['categoria_id']
        #nombre_archivo = secure_filename(filex.filename)  
        nombre_archivo = secure_filename(filex1.filename)  
        #nombre_archivo = secure_filename(filex2.filename)  
        #nombre_archivo = secure_filename(filex3.filename)  
        #filex1.save(os.path.join("C:/Practicas-Deybi/python/apps/app-gacela/app-gacela-normal/static/",nombre_archivo))
        #filex1.save(os.chdir("C:/Practicas-Deybi/python/apps/app-gacela/static/upload/"))
        #filex1=open(os.chdir("C:/Practicas-Deybi/python/apps/app-gacela/app-gacela-normal/static",nombre_archivo))
        #filex1.save(app.root_path + "././static/upload/" + nombre_archivo)
        #art = Articulos(imagen1=filex1,imagen2=filex2,imagen3=filex3,nombre=nombre,precio=precio,iva=iva,descripcion=descripcion,stock=stock,categoria_id=categoria_id)
        art = articulos(imagen1=filex1,nombre=nombre,precio=precio,iva=iva,descripcion=descripcion,stock=stock,categoria_id=categoria_id)
        art.imagen = nombre_archivo
        #art.imagen2 = nombre_archivo
        #art.imagen3 = nombre_archivo
        db.add(art), db.commit()
        return redirect("/inicio")
    return render_template("articulos/articulo-new-update3.html",categorias=categorias)

@app.route('/edit_articulo/<id>', methods=["get", "post"])
@login_required
def edit_articulox(id):
    art = db.query(articulos).get(id)
    categorias = db.query(sub_cat).all()
    if request.method == 'POST':
        filex = request.files["imagenx"]
        art.nombre = request.form['nombre']
        art.precio = request.form['precio']
        art.iva = request.form['iva']
        art.descripcion = request.form['descripcion']
        art.stock = request.form['stock']
        art.categoria_id = request.form['categoria_id']
        nombre_archivo = secure_filename(filex.filename) 
        #filex.save(app.root_path + "/static/upload/" + nombre_archivo)
        art.imagen = nombre_archivo
        db.commit()
        return redirect("/inicio")
    return render_template("articulos/articulo-new-update3.html",categorias=categorias,articulo=True,art=art)

@app.route('/delete_articulo/<id>', methods=["get", "post"])
@login_required
def delete_articulox(id):   # /delete_articulo/{{art.id}}
    art = db.query(articulos).get(id)
    if request.method=="POST":
        if id>"1" and request.form['si']:
            #if art.imagen != "":
            #    os.remove(app.root_path+"/static/upload/"+art.imagen)
            db.delete(art), db.commit()
            return redirect("/articulos")
    return render_template("articulos/articulo-delete.html",art=art)
###############################################################################################################
@app.route('/perfil', methods=["get", "post"])
@login_required
def perfilx():
    if current_user.is_authenticated and 'loggedin' in session:    #if 'loggedin' in session:
        cuenta = db.query(usuarios).filter_by(id=session['id']).first()
        return render_template("usuarios/perfil-normal.html",cuenta=cuenta)
    return redirect('/inicio')
#######################################################################
@app.route('/changepassword/<username>', methods=["get", "post"])
@login_required
def changepasswordx(username):
    user = db.query(usuarios).filter_by(username=username).first()
    if request.method == 'POST':
        user.password = request.form['password']
        db.commit()
        return redirect("/inicio")
    return render_template("usuarios/cambio-contraseña.html")
####################################################################################################################################
@app.route('/carrito_add2/<id>', methods=["get", "post"])
@login_required
def carrito_add2x(id):
    total=0
    artx = db.query(articulos).get(id)
    #form.id.data = id
    request.form.get("id"==id)
    if request.method == 'POST' and artx.stock >= int(request.form['cantidad']):   #if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        datos = json.loads(request.cookies.get(str(current_user.id)))
        for x in datos:
            if x["id"] == id:
                x["cantidad"] = cantidadx    #x["cantidad"] = int(request.form['cantidad'])
        resp = make_response(redirect(url_for('carritox')))
        resp.set_cookie(str(current_user.id), json.dumps(datos)) # set_cookie
        return resp
    msg='NO HAY LA  CANTIDAD QUE QUIERE2'
    return render_template("carrito-normal.html",art=artx,msg=msg, total=total)
################################################################ carrito ########################################################
@app.route('/carrito', methods=["get", "post"])
#@login_required
def carritox():
    try: datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos=[]
        datos = json.loads(request.cookies.get(str(current_user.id)))
    articulosx = []
    cantidadesx = []
    #totalx=[]
    total = 0
    for x in datos:    # {{ form.csrf_token }}
        #print(x) # {'id': '4', 'cantidad': 1}
        #z=list(x.values())
        #print(z) # ['4', 1]
        articulosx.append(db.query(articulos).get(x["id"])) # articulos.append(Articulos.query.get(z[0]))
        cantidadesx.append(x["cantidad"])  # cantidades.append(z[1])
        #sub_total = float(Articulos.query.get(z[0]).precio * z[1]) solo en caso q nomas se obtengas los values()
        sub_total = float(db.query(articulos).get(x["id"]).precio * x["cantidad"])
        total = float("{:.2f}".format(total + db.query(articulos).get(x["id"]).precio * x["cantidad"] + sub_total * 12/100))
        #totalx.append(total)    
    articulosz = zip(articulosx, cantidadesx)
#    for x in datos:
#        db.query(articulos).get(x["id"]).stock - x["cantidad"]
#        db.commit()
    #for x in articulosz:
        #    re=list(x)
        #    precio_mas_iva=re[0].precio * re[1]
            #print(re[0])# [<Articulos 1>, 1]    [<Articulos 4>, 1]
    #carrito=[]
        #carrito.append(articulosz)
        #for xx in carrito:
        #    a=list(xx)
        #    print(a)
    if request.method == "POST":   # 12/23 889
        stripe.api_key = "sk_test_51LJBxwEpqu9KnJeFKsKsZSeGMNI51RAcOrG7SYa4LrtP7vkvLNXUdjsAXt8flVgb3VITVYqSAJUGMYeDxiaAgRhA002OY7g4L3"
        session = stripe.checkout.Session.create(
        #session = stripe.PaymentIntent.create(
                    payment_method_types=['card'],
                    #type=['card'],
                    #images= ["static"],
                    line_items=[{"price_data":  {
                                                "currency": "usd",
                                                #"images": {"src":"static"},
                                                #"description": "My First Test Customer",
                                                #"city": "San Francisco",
                                                #"label": {"name": "Carrito Purchase",},
                                                #"product_data": {"name": x["id"],},
                                                "product_data": {"name": current_user.username,},
                                                #"product_data": {"name": articulosx[0].nombre,},
                                                #"product_data": {"name": current_user.id,},
                                                #"product_data": {"name": db.query(Articulos).get(x["id"]).nombre,},
                                                "unit_amount": round((float(total) * 100)),},
                                                #"amount": round((float(total) * 100)),},
                                                "quantity": 1
                    }],
                    mode="payment",
                    #success_url="http://localhost:5000/gracias",
                    #cancel_url="http://localhost:5000/"
                    #https://app1-ey6x.onrender.com/
                    #success_url="http://localhost:5000/gracias",
                    success_url="https://app1-ey6x.onrender.com/gracias",
                    #cancel_url="http://localhost:5000/"
                    cancel_url="https://app1-ey6x.onrender.com/carrito"
                )
        return redirect(session.url, 303)
    return render_template("carrito-normal.html",articulosz=articulosz,total=total)

@app.route('/gracias')
@login_required
def graciasx():
    if ok=="hola":
        try: datos = json.loads(request.cookies.get(str(current_user.id)))
        except:
            datos = []
        total = 0
        for articulo in datos:
            total = total + db.query(articulos).get(articulo["id"]).precio * articulo["cantidad"]
            db.query(articulos).get(articulo["id"]).stock -= articulo["cantidad"]
            db.commit()
        resp = make_response(render_template("pedido.html", total=total))
        resp.set_cookie(str(current_user.id), "", expires=0)
        return resp
    return "gracias por su compra,{ok}"   
####################################################################################################################
@app.route('/carrito_delete/<id>')
@login_required
def carrito_deletex(id):
    try: datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    new_datos = []
    for dato in datos:
        if dato["id"] != id:
            new_datos.append(dato)
    resp = make_response(redirect(url_for('carritox')))
    resp.set_cookie(str(current_user.id), json.dumps(new_datos))
    return resp

@app.context_processor
def contar_carrito():
    if not current_user.is_authenticated:
        return {'num_articulos': 0}
    if request.cookies.get(str(current_user.id)) is None:
        return {'num_articulos': 0}
    else:
        datos = json.loads(request.cookies.get(str(current_user.id)))
        return {'num_articulos': len(datos)}

@app.route('/pedido')
@login_required
def pedidox():
    try: datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    total = 0
    for articulo in datos:
        total = total + db.query(articulos).get(articulo["id"]).precio * articulo["cantidad"]
        db.query(articulos).get(articulo["id"]).stock -= articulo["cantidad"]
        db.commit()
    resp = make_response(render_template("pedido.html", total=total))
    resp.set_cookie(str(current_user.id), "", expires=0)
    return resp

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
