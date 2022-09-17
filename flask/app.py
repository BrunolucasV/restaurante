from flask import Flask, render_template, url_for 
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        curry="ou carne ou frango, cenora, cebola, batata e golden curry"
        risoto="camarão, vinho branco seco, champignom, tomates, cebola, alho, salsão, creme de leite, Sal, parmesão, curry, salsinha, folha de louro e azeite"
        Coquetel="camarão, iogute sem lactose, molho inglês, mostarda D'jon, catchup, conhaque e abacaxi"
        espetinhos="suco de limão, mel, primenta do reino, filé mignon, bacon e gergelim"
        Quiche="farinha de trigo, ovos, creme de leite, batata, cenora, berinjela, champignom, queijo parmesao e primenta do reino"
        Quibe= "trigo para quibe, batata, hortelã, primenta síria, alho, azeite de oliva, tofu, limão, azeite e orégano"
        qnhoque= "mandioquinha, azeite, amido de milho e molho de tomate"
        escondidinhoVegetariano= "batata,manteiga, leite, pimento do reino, azeite, cebola, alho, tomate, cenora, vagem, ervilhas, páprica, muçarela e oregano"
        return  render_template('index.html',curry=curry, risoto=risoto,Coquetel=Coquetel, espetinhos=espetinhos, Quiche=Quiche, Quibe=Quibe,qnhoque=qnhoque,escondidinhoVegetariano=escondidinhoVegetariano )
    return app
app = create_app()
