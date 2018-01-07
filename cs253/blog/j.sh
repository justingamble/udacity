#!/bin/bash

# Instructions:
# $ source env/bin/activate
# $ ./j.sh
# and then in your browser, head to... localhost:8080

# This assumes you have installed Google App Engine.  I followed the 
# notes at https://developers.google.com/appengine
dev_appserver.py app.yaml
