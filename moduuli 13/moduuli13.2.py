app= Flask(__name__)

@app.route('/kenttä/<icao>')
def lentokenttä(icao):
    yhteys=mysql.connector.connect(
        host='localhost',
        port:3306,
        database ='flight_game',
        user='root',
        password=''
        autocommit=True

    )
    sql="SELECT name, municipality FFROM airport WHERE indent ='"+icao+
    kursori=yhteys.cursor()
    kursori.execute(sql)
    tulos =kursori.fetchone()

    vastaus={
    "ICAO":icao,
    "Name": tulos[0]
    "Municipality":tulos[1]
    }

    return vastaus

if __name__ =='__main__':
    app.run(use_reloader=True, host'127.0.0.1', port=3000)