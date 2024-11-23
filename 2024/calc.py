from nicegui import ui

def calculate_expression(expression):
    try:
        # Evaluate the mathematical expression entered by the user
        result = eval(expression)
        # If the result is 4, return 5; otherwise, return 4
        return 5 if result == 4 else 4
    except:
        return "Error"  # Handle any invalid input gracefully

with ui.row():
    ui.label("Expression:").style("margin-right: 8px")
    input_field = ui.input().style("margin-right: 8px")
    result_label = ui.label("Result: ")

def on_calculate():
    expression = input_field.value
    result = calculate_expression(expression)
    result_label.set_text(f"Result: {result}")

ui.button("Calculate", on_click=on_calculate).style("margin-left: 8px")

# Start the NiceGUI app
ui.run()
