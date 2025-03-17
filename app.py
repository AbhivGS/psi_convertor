from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion factors for pressure units
conversion_factors = {
    "PSI": {
        "Pa": 6894.76,
        "kPa": 6.89476,
        "bar": 0.0689476,
        "atm": 0.068046,
        "PSI": 1
    },
    "Pa": {
        "PSI": 0.000145038,
        "kPa": 0.001,
        "bar": 1e-5,
        "atm": 9.86923e-6,
        "Pa": 1
    },
    "kPa": {
        "PSI": 0.145038,
        "Pa": 1000,
        "bar": 0.01,
        "atm": 0.00986923,
        "kPa": 1
    },
    "bar": {
        "PSI": 14.5038,
        "Pa": 100000,
        "kPa": 100,
        "atm": 0.986923,
        "bar": 1
    },
    "atm": {
        "PSI": 14.696,
        "Pa": 101325,
        "kPa": 101.325,
        "bar": 1.01325,
        "atm": 1
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    initial_unit = "PSI"
    target_unit = "Pa"
    if request.method == "POST":
        value = float(request.form["value"])
        initial_unit = request.form["initial_unit"]
        target_unit = request.form["target_unit"]

        # Conversion calculation
        if initial_unit in conversion_factors and target_unit in conversion_factors[initial_unit]:
            result = value * conversion_factors[initial_unit][target_unit]

    return render_template("index.html", result=result, initial_unit=initial_unit, target_unit=target_unit)

if __name__ == "__main__":
    app.run(debug=True)
