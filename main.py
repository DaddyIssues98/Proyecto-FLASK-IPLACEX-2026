from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola, {nombre}. Esta es una ruta con parámetros."


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                abort(400, description="Las notas deben estar entre 10 y 70.")
            if not (0 <= asistencia <= 100):
                abort(400, description="La asistencia debe estar entre 0 y 100.")

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "APROBADO" if (promedio >= 40 and asistencia >= 75) else "REPROBADO"

            return render_template('ejercicio1.html', promedio=round(promedio, 1), estado=estado)
        
        except ValueError:
            abort(400, description="Por favor, ingrese valores numéricos válidos.")

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('ejercicio2.html', 
                               nombre_mas_largo=nombre_mas_largo, 
                               cantidad=cantidad_caracteres)

    return render_template('ejercicio2.html')

@app.errorhandler(400)
def bad_request(error):
    return render_template('index.html', error=error.description), 400

if __name__ == '__main__':
    app.run(debug=True)