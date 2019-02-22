from flask import Flask, request

# Objeto flask
app = Flask(__name__)

# Rota para /nome

@app.route('/')
def principal():
    return'<html>' \
          '     <head>' \
          '         <title>' \
          '             Pagina Inicial' \
          '         </title>' \
          '     </head>' \
          '' \
          '      <body>' \
          '         <h1><a href=''/nome''>Meu nome é</a>' \
          '     </h1>' \
          '     </body>' \
          '</html>'

@app.route('/nome')
@app.route('/meunome')

def nome ():
    metodo= request.method
    return 'eu'

@app.route('/exibir')
def exibir():
    nome = request.args.get('nome')
    return nome


# iniciar o app

if __name__ == '__main__':
    app.run(debug=True)


