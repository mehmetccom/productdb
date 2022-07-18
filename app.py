from flask import Flask, request, render_template, redirect, flash, abort, url_for
from database import db, Category, Product
 
def setup_app(app):

    @app.route('/demotest_route/<demo_test_value>')
    def demotest(demo_test_value):
        return render_template('hello.html', name=demo_test_value)
        
    @app.route('/')
    def index(id=None):
        if id:
            _products = Product.query.filter_by(id=id).all()
        else:
            _products = Product.query.all() 
        if not _products:
            abort(404) 
        return render_template('index.html', product_list=_products)

    @app.route('/addproductform/')
    def show_product_add_form():
        return render_template('add.html')

    @app.route('/addproduct', methods = ['POST', 'GET'])
    def add_product():

        if request.method == 'POST' and request.form['save']:
            p_name = request.form['name']        
            p_price = request.form['price']
            p_category_id = request.form['categoryid'] 
            
            product_to_add = Product(name=p_name, price=p_price,  category_id=p_category_id)
            
            db.session.add(product_to_add)
            db.session.flush()
            if product_to_add.id > 0:
                db.session.commit()
                flash("A new product has been added..")
            else:
                flash("A new product can not be added")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

    @app.route('/deleteproduct/<int:id>/')
    def delete_product(id):
        if id:
            query = db.session.query(Product)
            query = query.filter(Product.id == id)
            product_to_delete = query.one()
            db.session.delete(product_to_delete)
            db.session.commit()
            product_to_delete = query.first()        
            if product_to_delete == None:
                flash("Product deleted.")
                return redirect(url_for('index'))
            else:
                flash("Error occured while deleting the product..")
                return redirect(url_for('index'))
        else:
            flash("Error occured while deleting the product..")
            return redirect(url_for('index'))

    @app.route('/updateproductform/<int:id>')
    def show_product_update_form(id):
        product_to_update = Product.query.filter_by(id=id).one()
        return render_template('update.html', product = product_to_update)
        
    @app.route('/updateproduct/', methods = ['POST'])
    def update_product():	
        if request.form['product_id']:
            product_id = request.form['product_id']
            p_name = request.form['name']        
            p_price = request.form['price']        
            
            query = db.session.query(Product)
            product_to_update = query.filter(Product.id == product_id).one()
            product_to_update.name = p_name
            product_to_update.price = p_price        
            db.session.commit()
            
            flash("Product updated.")
            return redirect(url_for('index'))
        else:
            flash("Error occured while deleting the product..")

def app_factory(name=__name__, debug=False):
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/testdb'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mehmetcoskun:deneme123@10.0.0.5:3306/testdb'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True    
    app.secret_key = "this5is5our5secret5key55513"
    app.debug = True
    db.init_app(app)    
    setup_app(app)
    return app
 
if __name__ == '__main__':
    app = app_factory(debug=True)    
    app.run(host='0.0.0.0') 
	
