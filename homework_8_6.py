from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = session.get("last_result", None)
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]
            if operation == "add":
                result = num1 + num2
            elif operation == "substract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Помилка: Ділення на нуль"
            session["last_result"] = result
        except ValueError:
            result = "Помилка: Введіть коректні числа"
    return render_template("calculator.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)