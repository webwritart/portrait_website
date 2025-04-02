from flask import Flask
from routes.main import main

app = Flask(__name__)
app.secret_key = 'rehgeriognerrghergn589y3y9uh&*ggn98HG(&g998RGHN*(fg98H84G'

app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
