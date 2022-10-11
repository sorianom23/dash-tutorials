# Callback functions are a type of Python function that can take inputs and return outputs
# in this case when the user changes the input, the output changes automatically

from dash import Input, Output

'''
Decorator:
@app.callback( 
    Output(component_id, component_property),
    Input(componenet_id, component_property)
)
Function:
def function_name(input_object):
    # body of the function
    return output_object
'''

# Component id: The id property or the variable name of the component
# Component property: One of the properties of the component (children of html, figure of dcc Graph)

