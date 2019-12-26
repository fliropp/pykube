# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from redis import Redis
from datetime import datetime
import json

app = Flask(__name__)
redis = Redis(host='redis-master', port=6379)
#redis = Redis(host='localhost', port=6379)


def get_response():
    dateTimeObj = datetime.now()
    tstr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    jdict = {
    'hits': redis.get('hits'),
    'source': 'Redis',
    'timestamp': tstr
    }
    jdict = json.dumps(jdict)
    resp = json.loads(jdict)
    return resp

@app.route('/')
def hello():
    redis.incr('hits')
    r = get_response()
    return jsonify(r), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)