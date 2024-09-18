from dash import Dash, html

app = Dash()

app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(debug=True)

# To run:
# cd example_code/other_frameworks
# python dash_simple.py
