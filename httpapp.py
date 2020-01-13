#!/usr/bin/pythona
# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from redis import Redis
from datetime import datetime
import grpcserver
import threading
#import grpcclient
import json
try:
    app = Flask(__name__)
    redis = Redis(host='redis-master', port=6379)
    #redis = Redis(host='localhost', port=6379)

    def start_grpc_server():
        grpcserver.StartGrpcServer()

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

    @app.route('/pykube')
    def hello():
        redis.incr('hits')
        r = get_response()
        return "OK", 200


    @app.route('/ping')
    def ping():
        return "Ok, computer", 200

    if __name__ == "__main__":
        grpcs = threading.Thread(target=start_grpc_server, args=())
        grpcs.deamon=True
        grpcs.start()
        app.run(host="0.0.0.0", debug=True)

except KeyboardInterrupt:
    grpcs.stop()
    print("shut down . . .")