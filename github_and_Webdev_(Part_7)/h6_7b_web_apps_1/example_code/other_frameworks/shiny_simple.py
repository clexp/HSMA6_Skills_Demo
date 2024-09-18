from shiny import ui, App

frontend = ui.page_fluid(
  "Hello World!"
)

def server(input, output, session):
  return True

app = App(frontend, server)

# To run:
# cd example_code/other_frameworks
# shiny run shiny_simple.py
