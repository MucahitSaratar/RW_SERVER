from flask import Flask, request
import time as T
import hashlib as H
import os


def kaydet(data):
	komut = "echo {} ---to--- {} >> ziyaretciler.txt".format(T.ctime(), data)
	print "isleniyor... : ", komut
	os.system(komut)


def oku():
	ac = open("ziyaretciler.txt", "r").readlines()[-1].replace("\n" ,"")[-1]
	return ac



app = Flask(__name__)

@app.route("/")
def main():
	return "Ana Sayfada Bisi yok .d"


@app.route("/write", methods = ["GET", "POST"])
def write():
	if request.method == "GET":
		hash = request.args.get("key")
		durum = request.args.get("status")
		if str(int(T.ctime()[11:16].replace(":" ,"")[::-1])*7) == str(hash):
			kaydet(durum)
			return "Successfull: {}".format(durum)
		else:
			return "Unsuccessfull"
	else:
		return "POST YOOOOK xd"


@app.route("/readata")
def read():
	return oku()



app.run(debug=True)
