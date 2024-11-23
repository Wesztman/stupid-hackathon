from nicegui import ui

# Initialize the current expression
expression = ""

def add_to_expression(symbol):
    """Append a symbol to the global expression."""
    global expression
    expression += str(symbol)
    display.set_text(expression)

def clear_expression():
    """Clear the global expression."""
    global expression
    expression = ""
    display.set_text(expression)
    
def calculate():
    """Evaluate the expression and display the quirky result."""
    global expression
    try:
        # Evaluate the mathematical expression
        result = eval(expression)
        # Apply the quirky logic
        final_result = 5 if result == 4 else 4
    except:
        final_result = "Error"
    display.set_text(str(final_result))
    expression = ""  # Reset the expression after calculation

# Create the calculator UI
with ui.column().style("align-items: center; max-width: 220px; margin: auto;"):
    ui.label("The Four-gotten Calculator").style(
        "font-size: 24px; font-weight: bold; margin-bottom: 15px; text-align: center;"
    )
    display = ui.label(expression).style(
        "font-size: 32px; margin-bottom: 15px; text-align: center; width: 100%; background: #eaeaea; padding: 10px; border-radius: 5px;"
    )

    # Create buttons for numbers and operations in a compact grid
    with ui.grid(columns=4).style("gap: 10px;"):
        for button in ["7", "8", "9", "+",
                       "4", "5", "6", "-",
                       "1", "2", "3", "*",
                       "C", "0", "=", "/"]:
            if button == "C":
                ui.button(button, on_click=clear_expression).style("height: 50px; width: 50px; font-size: 18px;")
            elif button == "=":
                ui.button(button, on_click=calculate).style("height: 50px; width: 50px; font-size: 18px;")
            else:
                ui.button(button, on_click=lambda b=button: add_to_expression(b)).style("height: 50px; width: 50px; font-size: 18px;")

# Start the NiceGUI app
ui.run()
