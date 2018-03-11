# # coding:utf-8
# from flask import Flask
# app= Flask(__name__)
#
# @app.route('/')
# def index():
#     return "hello world"
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,request,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#     <form method ="GET" action ="/search">
#         <input type ="text" placeholder="input keywords"
#         value="python Flask" name="q">
#         <input type="submit" value="search">
#     </form>
#     '''
# @app.route('/search')
# def v_search():
#     if 'q'in request.args:
#         ret='<p>searching %s... \
#             </p>' % request.args['q']
#     else:
#         ret='what do you want to search?'
#     return ret
# app.run(debug=True)


# # coding:utf-8
# from flask import Flask,make_response,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '<a href="%s">ping</a>' % url_for('v_ping')
# @app.route('/ping')
# def v_ping():
#     return 'pong'
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,request,make_response,url_for
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     rsp=make_response('go <a href="%s">page2</a>' % url_for('v_page2'))
#     rsp.set_cookie('user','yanchaoxiu')
#     return rsp
# @app.route('/page2')
# def v_page2():
#     user=request.cookies['user']
#     return 'you are %s'% user
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,json
# app=Flask(__name__)
# users=['linda','marion','race']
# @app.route('/')
# def v_index():
#     return json.dumps(users),200,[('Content-Type','application/json;charset=utf-8')]
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,redirect
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return redirect('/newbies')
# @app.route('/newbies')
# def v_newbies():
#     return 'this page is for newbies only'
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,abort,request
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return '''
#         <ul>
#             <li><a href="admin?token=111">allowed</a></li>
#             <li><a href="/admin">forbidden</a></li>
#         </ul>
#     '''
# @app.route('/admin')
# def v_admin():
#     if 'token' in request.args:
#         return 'you are a good girl'
#     else:
#         abort(401)
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,session,request
# app=Flask(__name__)
# app.secret_key='yan123'
# @app.route('/')
# def v_index():
#     if 'counter' not in session:
#         session['counter']=0
#     session['counter']=session['counter']+1
#     return 'this is your %d times visit' % session['counter']
# app.run(debug=True)

# # coding:utf-8
# from flask import Flask,session,request
# from flask.globals import _request_ctx_stack,_app_ctx_stack
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     print request
#     print _request_ctx_stack.top.request
#     print _app_ctx_stack.top
#     return 'see console output'
# print _request_ctx_stack.top
# print _app_ctx_stack.top
# app.run(debug=True)


# # coding:utf-8
# from flask import Flask,session,request,url_for
# from flask.globals import _request_ctx_stack,_app_ctx_stack
# app=Flask(__name__)
# @app.route('/')
# def v_index():
#     return 'home page'
# @app.route('/genius')
# def v_genius():
#     return 'nothing special'
# with app.app_context():
#     print url_for('v_genius')
#
# app.config['SERVER_NAME']='coupled.com'
# ctx=app.app_context()
# ctx.push()
# print url_for('genuis')
# ctx.pop()
#
# app.config['SERVER_NAME']='coupled.com'
# with app.app_context():
#     print url_for('genuis')

# #coding:utf-8
# from flask import Flask,url_for
# app=Flask(__name__)
# app.config['SERVER_NAME'] = 'coupled.com'
# @app.route('/')
# def v_index():
#     return 'home page'
# @app.route('/genius')
# def v_genius():
#     return 'nothing special'
# with app.app_context():
#     print url_for('v_genius')

# # coding:utf-8
# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def index():
#     return 'this is not the point'
# @app.before_first_request
# def before_first_req():
#     print 'before process first request'
# @app.before_request
# def before_req():
#     print 'before process request'
# @app.after_request
# def after_req(rsq):
#     print 'after process request'
#     return rsq
# @app.teardown_request
# def teardown_reqctx(e):
#     print 'teardown process context'
# @app.teardown_appcontext
# def teardown_appctx(e):
#     print 'teardown application context'
# app.run(debug=True)

# # coding:utf-8
# from flask import render_template
# from app import app
# @app.route('/')
# @app.route('/index')
# def index():
#     user={'nickname':'Miguel'}
#     return render_template("index.html",title='Home',user=user)
# app.run(debug=True)

# @app.route('/user/<uname>')
# def show_user_profile(uname):
#     return render_template_string('<h1>welcome,{{uname}}</h1>',uname=uname)
#
# @app.route('/user/<uname>')
# def v_user(username):
#     return render_template('user.html',username=username)
#
# tpl='name:{{name}} age:{{age}}'
# print render_template_string(tpl,name='marion5',age=12)
#
#
# tpl='name:{{u["name"]}} name again:{{u.name}}'
# print render_template_string(tpl,u={'name':'marion5','age':12})
#
# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# tpl='name:{{u.name}} name again:{{u["name"]}}'
# print render_template_string(tpl,u=User('Mary',20))
#

# # coding:utf-8
# from flask import render_template_string
# from app import app
# @app.route('/')
# def v_index():
#     tpl='welcome back,{{session.username}}'
#     return render_template_string(tpl)
# app.run(debug=True)

# # coding:utf-8
# from flask import render_template_string
# from app import app
# @app.context_processor
# def vendor_processor():
#     return dict(vendor='hubwiz')
# @app.route('/')
# def v_index():
#     tpl='powered by {{vendor}}'
#     return render_template_string(tpl)
# app.run(debug=True)
#
# @app.context_processor
# def utility_processor():
#     def format_price(amount,currency=u'$'):
#         return u'{0:.2f}{1}'.format(amount,currency)
#     return dict(format_price=format_price)
#
# class User:
#     def __init__(self,id,name,age):
#         self.id=id
#         self.name=name
#         self.age=age
#
# user1=User(1,'zhang3',20)
# user2=User(1,'li4',30)
# user3=User(1,'wang5',30)

# from flask import Flask
# import os
# from flask_sqlalchemy import SQLAlchemy
# app=Flask(__name__)
# basedir=os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db=SQLAlchemy(app)
# class User(db.Model):
#     __tablename__='ezuser'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(64),unique=True,index=True)
#     age=db.Column(db.Integer)
# db.create_all()
# db.drop_all()
# # 以下我不是很懂
# db.session.add(obj)
# db.session.add([obj1,obj2,obj3])
# db.session.commit()
# user.save()
# account1.balance=account1.balance-100
# account2.balance=account2.balance+100
# account1.save()
# account2.save()
#
# __begin_transaction__
# account1.save()
# account2.save()
# __commit_transaction__
#
# users=User.query.all()
# user=User.query.filter_by(id=1).first()
# db.session.delete(user).db.session.commit()
#
# user.age=21
# db.session.add(user)
# db.session.commit()


# from flask import Flask,Blueprint
# ezbp=Blueprint("ezbp",__name__)
# from app import app
# # http://127.0.0.1:5000/ezbp/
# @ezbp.route('/')
# def ezbp_index():
#     return 'welcome to my blueprint'
# # http://127.0.0.1:5000/ezbp/page1
# @ezbp.route('/page1')
# def page1():
#     return 'blueprint page1'
# app.register_blueprint(ezbp,url_prefix='/ezbp')
# app.run(debug=True)


# from flask import Flask,Blueprint
# admin=Blueprint("admin",__name__,static_folder='ezstatic')
# from app import app
# @admin.route('/')
# def ezbp_index():
#     return 'welcome to my blueprint'
# app.register_blueprint(admin,url_prefix='/admin')
# app.run(debug=True)

# from flask import Flask,Blueprint
# admin=Blueprint("admin",__name__,static_folder='ezstatic',static_url_path='/lib')
# from app import app
# @admin.route('/')
# def ezbp_index():
#     return 'welcome to my blueprint'
# app.register_blueprint(admin,url_prefix='/admin')
# app.run(debug=True)


# from app import app
# @app.route('/')
# @app.route('/index')
# def index():
#     user={'nickname':'Miguel'}
#     return '''
#     <html>
#     <head>
#     <title>home page</title>
#     </head>
#     <body>
#     <h1>hello,'''+user['nickname']+'''</h1>
#     </body>
#     </html>
#     '''
# app.run(debug=True)

# from flask import Flask,flash,redirect,render_template
# from app import app
# import config
# app=Flask(__name__)
# from forms import LoginForm
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         flash('login requested for OpenID="'+
#               form.openid.data+'",remember_me='+
#               str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])
#
# app.run(debug=True)

# from flask import Flask,render_template
# from flask_login import login_required
# from app import app
# @app.route('/')
# @app.route('/index')
# @login_required
# def index():
#     user=g.user
#     posts=[
#         {'author':{'nickname':'JOhn'},'body':'beautiful day in basi'},
#         {'author':{'nickname':'su'},'body':'the movie was so cool'}
#     ]
#     return render_template('index.html',title='home',user=user,posta=posts)
# app.run(debug=True)

