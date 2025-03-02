from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def home():
    '''A simple routes that takes the user to '/'
    the first page which he will see when the website is rendered
    '''
    return jsonify({"message":'Welcome to the Home page'}),200

#Lets test some commonly used status codes.

@app.route('/success')
def success():
    '''Returns a 200 OK status response when a request is successful'''
    return jsonify({"Message":"The request worked."}), 200

@app.route('/created',methods=['GET']) #<-- do methods = ['POST] when testing
def created():
    '''Stimulates Resource creation with 201 Status'''
    return jsonify({"Message":"Resourced created Successfully"}), 201

@app.route('/redirect',methods=['GET'])
def found():
    '''302 Found: occours when redirecting to another page'''
    return redirect('/',code=302)

@app.route('/bad-request',methods=['GET'])
def unauthorised():
    '''400 Bad Request occours when the information sent by user is invalid'''

    return jsonify({"message":"Bad Request"}),400


@app.route('/unauthorized',methods=['GET'])
def unauthorized():
    '''401: Unauthorized error shows up when the user is not authenticated 
    and is trying to access a protected route'''

    return jsonify({"message":"Login Required"}), 401

@app.route('/forbidden',methods=['GET'])
def forbidden():
    '''403: occours when a user is authenticated but does not have the
    authority to view the specific route'''

    return jsonify({"Message":'You cannot perform that function'}), 403

@app.route('/not-found',methods=['GET'])
def not_found():
    '''404: is a classic status code, it occours when the user is trying to access
    a route that does not exists.'''

    return jsonify({"Message":'Item not found'}),404

@app.route('/not-allowed',methods=['GET']) #<--- same as 201 created change to post for testig
def not_allowed():
    '''405: Error that occours when the user tries to use the wrong method on a pirticular view'''
    return jsonify({"Message":'Method Not Allowed'}), 405


@app.route('/internal-server-error',methods=['GET'])
def internal_error():
    '''500: Error which occours when there is an error in the server side.'''
    return jsonify({'message':'an error has occoured'}),500


if __name__ == '__main__':
    app.run(debug=True)