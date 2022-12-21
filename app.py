#################################################
###        IMPORT NECESSARY LIBRARIES         ###
#################################################

import pandas as pd
from flask import (
    Flask,
    render_template,
    request,
    redirect)

# app_ = Flask(static_folder='E:\codegnan\templates\images')

#FLASK SETUP               
app = Flask(__name__)

#################################################
####              HOME ROUTE                 ####
#################################################
@app.route("/")
def home():
    # print(index.html)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

#################################################
####            END OF FLASK APP             ####
#################################################
