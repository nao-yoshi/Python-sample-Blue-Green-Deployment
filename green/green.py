#!/usr/bin/python

import os
import uuid
import urlparse
import json
from flask import Flask

app = Flask(__name__)
port = int(os.getenv("PORT"))
myuuid = str(uuid.uuid1())
myinstance = str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/')
def main():
    return """
    <html>
    <head>
      <title> Pivotal Web Service </title>
    </head>
    <body>
      <center><FONT size="6" color="black">=== VMware Tanzu Application Service ===</FONT>
      <center><b><FONT size="7" color="blue">This is GREEN environment!</FONT></b>
      <br>
      <br>
      <br>
      <center><h1> App Instance : <font color="green"> {}
      <br>
      <br>
      <center><FONT size="4" color="blue">UUID : {}</FONT>
      <br>
      <br>
      </center>
    </body>
    </html>
    """.format(myinstance, myuuid, )
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)

