from flask import Flask
app= Flask(__name__)


@app.route('/alkuluku/<luku>')
def jaollisuus(luku):
    jaollinen=False
    alkuluku=False
    #lukua 1 ei ole alkuluku
    lukuint=int(luku)
    if lukuint!=1:
        for lukuint %jakaja ==0:
            jaollinen =True
            break
        if jaollinen:
            alkuluku = False
        else:
            alkuluku=True
        alkuluku==1:
            alkuluku=False
    if lukuint ==1:
vastaus= {
    "Number": lukuint,
    "Isprime" :alkuluku
}
return vastaus

if __name__ =='__main__'
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

