from flask import Flask, render_template, url_for, request, redirect
from nltk_summarization import nltk_summarizer
from huggingbart import huggingBart
from extractAbstract import extractAbstract
from wikiScrape import scrapeClean

import time

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")
   
@app.route("/webdev",methods=["GET","POST"])
def webdev():
    return render_template("webdev.html")

@app.route("/sillyForm",methods=["GET","POST"])
def sillyForm():
    return render_template("sillyForm.html")

@app.route("/tributePage",methods=["GET","POST"])
def tributePage():
    return render_template("tributePage.html")

@app.route("/technicalPage",methods=["GET","POST"])
def technicalPage():
    return render_template("technicalPage.html")

@app.route("/lander",methods=["GET","POST"])
def lander():
    return render_template("lander.html")

@app.route("/projects",methods=["GET","POST"])
def projects():
    return render_template("projects.html")

@app.route("/bio",methods=["GET","POST"])
def bio():
    return render_template("bio.html")

@app.route("/NLP",methods=["GET","POST"])
def NLP():
    return render_template("NLP.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if request.method=="POST":

        raw_text=request.form["data"]
        text = ""

        if len(raw_text)<50:
            text = scrapeClean(inputText=raw_text)
        else:
            text = raw_text

        length=int(request.form["maxL"])
        text=text
        nltkOutput=nltk_summarizer(raw_text=text, maxL=length)
        HBoutput=huggingBart(text=text, length=length)
        extactiveResult, extabsResult = extractAbstract(text)
                #max_length=length, min_length=(int(length*.8))
        return render_template("NLP.html", textDataResult=text, nltkResult=nltkOutput, hugbartResult=HBoutput, extactiveResult=extactiveResult, extabsResult=extabsResult)
    else:
        return render_template("NLP.html")
    
@app.route('/ML11')
def ML11():
    return redirect("https://colab.research.google.com/drive/13dWVAX3PNbR83hxJwXkMWh7O3slTiCLK")

@app.route('/ML12')
def ML12():
    return redirect("https://colab.research.google.com/drive/1glO8td89AmJYtS6wcgDTP6elK1DBX0sV")

@app.route('/ML13')
def ML13():
    return redirect("https://colab.research.google.com/drive/1sHKupthEp1nfBcBwf4ZZRWUYv-WyRuyF")

@app.route('/ML14')
def ML14():
    return redirect("https://colab.research.google.com/drive/1WMWLqdHSBuIGvGCCXKz8OcfKs3dx-1uE")

@app.route('/ML15')
def ML15():
    return redirect("https://colab.research.google.com/drive/1OOnq-s0vb4wNLbmttUpmuDuxIsUSvCmq")

@app.route('/ML16')
def ML16():
    return redirect("https://colab.research.google.com/drive/1rC-5ndQwtzwNhjbhsTf6QbrawFCXaKU8")

@app.route('/ML17')
def ML17():
    return redirect("https://colab.research.google.com/drive/1Hzxlnr5K4rLp7TBIN290PLpkJO99qDfy ")

@app.route('/ML21')
def ML21():
    return redirect("https://colab.research.google.com/drive/1jUT4ndG14CmyyZclPAzGicDDF0F-9sPS")

@app.route('/ML22')
def ML22():
    return redirect("https://colab.research.google.com/drive/1PpS8O-nebftphZwHBCN4vhi5lEaHobwM")

@app.route('/ML23')
def ML23():
    return redirect("https://colab.research.google.com/drive/1K2XcQtkI3UVv5pvspMtJTZX79ZzN0QoP ")

@app.route('/ML24')
def ML24():
    return redirect("https://colab.research.google.com/drive/1asJK2VdCbPvXrcaOliQM9KOQW8XNWAFs")

@app.route('/ML25')
def ML25():
    return redirect("https://colab.research.google.com/drive/1qZ7RYaFTAsCOKouxTzsqAzgwNVkZ4miP")

@app.route('/ML26')
def ML26():
    return redirect("https://colab.research.google.com/drive/1IwTzRGu624Z4eqGViKYty1jj9efzMXa4")



if __name__=='__main__':
    app.run(debug=True)
