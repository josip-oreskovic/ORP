from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Client, CompanyType, CompanySize
from pony.orm import db_session, select

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Configure SQLite database
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

# Initialize some sample data
with db_session:
    if not CompanyType.select().exists():
        CompanyType(name="D.O.O.")
        CompanyType(name="J.D.O.O.")
        CompanyType(name="Udruga")
        CompanyType(name="Obrt")
    
    if not CompanySize.select().exists():
        CompanySize(name="Mikro")
        CompanySize(name="Malo")
        CompanySize(name="Srednje")
        CompanySize(name="Veliko")

@app.route('/')
@db_session
def index():
    clients = select(c for c in Client)[:]
    return render_template('clients.html', clients=clients)

@app.route('/client/create', methods=['GET', 'POST'])
@db_session
def create_client():
    if request.method == 'POST':
        try:
            client = Client(
                name=request.form['name'],
                id_company_type=CompanyType[request.form['id_company_type']],
                id_size=CompanySize[request.form['id_size']],
                address=request.form.get('address'),
                city=request.form.get('city'),
                post_number=request.form.get('post_number'),
                country=request.form.get('country'),
                tel=request.form.get('tel'),
                mob=request.form.get('mob'),
                email=request.form.get('email'),
                fax=request.form.get('fax'),
                id_director=request.form.get('id_director'),
                pin=request.form.get('pin'),
                vat_num=request.form.get('vat_num'),
                reg_numb=request.form.get('reg_numb'),
                stat_num=request.form.get('stat_num'),
                activity_num=request.form.get('activity_num'),
                activity_desc=request.form.get('activity_desc'),
                hzmo_num=request.form.get('hzmo_num'),
                hzzo_num=request.form.get('hzzo_num'),
                vat_period=request.form.get('vat_period'),
                employee_num=int(request.form.get('employee_num', 0)),
                price=float(request.form.get('price', 0.0))
            )
            flash('Client created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error creating client: {str(e)}', 'danger')
    
    company_types = select(ct for ct in CompanyType)[:]
    company_sizes = select(cs for cs in CompanySize)[:]
    return render_template('create.html', company_types=company_types, company_sizes=company_sizes)

@app.route('/client/<int:id>')
@db_session
def view_client(id):
    client = Client.get(id_client=id)
    if not client:
        flash('Client not found', 'danger')
        return redirect(url_for('index'))
    return render_template('view.html', client=client)

@app.route('/client/edit/<int:id>', methods=['GET', 'POST'])
@db_session
def edit_client(id):
    client = Client.get(id_client=id)
    if not client:
        flash('Client not found', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            client.name = request.form['name']
            client.id_company_type = CompanyType[request.form['id_company_type']]
            client.id_size = CompanySize[request.form['id_size']]
            client.address = request.form.get('address')
            client.city = request.form.get('city')
            client.post_number = request.form.get('post_number')
            client.country = request.form.get('country')
            client.tel = request.form.get('tel')
            client.mob = request.form.get('mob')
            client.email = request.form.get('email')
            client.fax = request.form.get('fax')
            client.id_director = request.form.get('id_director')
            client.pin = request.form.get('pin')
            client.vat_num = request.form.get('vat_num')
            client.reg_numb = request.form.get('reg_numb')
            client.stat_num = request.form.get('stat_num')
            client.activity_num = request.form.get('activity_num')
            client.activity_desc = request.form.get('activity_desc')
            client.hzmo_num = request.form.get('hzmo_num')
            client.hzzo_num = request.form.get('hzzo_num')
            client.vat_period = request.form.get('vat_period')
            client.employee_num = int(request.form.get('employee_num', 0))
            client.price = float(request.form.get('price', 0.0))
            flash('Client updated successfully!', 'success')
            return redirect(url_for('view_client', id=id))
        except Exception as e:
            flash(f'Error updating client: {str(e)}', 'danger')
    
    company_types = select(ct for ct in CompanyType)[:]
    company_sizes = select(cs for cs in CompanySize)[:]
    return render_template('edit.html', client=client, company_types=company_types, company_sizes=company_sizes)

@app.route('/client/delete/<int:id>', methods=['POST'])
@db_session
def delete_client(id):
    client = Client.get(id_client=id)
    if client:
        client.delete()
        flash('Client deleted successfully!', 'success')
    else:
        flash('Client not found', 'danger')
    return redirect(url_for('index'))

@app.route('/clients/large')
@db_session
def large_clients():
    large_size = CompanySize.get(name="Veliko")
    clients = select(c for c in Client if c.id_size == large_size)[:]
    return render_template('clients.html', clients=clients, title="Veliki klijenti")

@app.route('/clients/high-value')
@db_session
def high_value_clients():
    clients = select(c for c in Client if c.price > 200)[:]
    return render_template('clients.html', clients=clients, title="Ključni klijenti")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)