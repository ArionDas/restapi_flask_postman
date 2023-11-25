from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'item1',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]

@app.route('/')
def home():
    return "hey"

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['name'])
        
    return jsonify({'message':'Store not found'})

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
        
    return jsonify({'message':'Store not found'})

@app.route('/store', methods=['POST'])
def create_store():
    req_data = request.get_json()
    new_store={
        'name':req_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    req_data = request.get_json()
    for store in stores:
        if(store['name']==name):
            new_item = {
                'name':req_data['name'],
                'price':req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    
    return jsonify({'message':'Store not found'})


app.run(port=8000)