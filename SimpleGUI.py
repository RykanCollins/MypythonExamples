import  pyforms
from    pyforms             import BaseWidget
from    pyforms.controls    import ControlText
from    pyforms.controls    import ControlButton

class SimpleExample1(BaseWidget):
    def __init__(self):
        super(SimpleExample1,self).__init__('Simple Example 1')

        #Definition of the forms fields
        #self._firstname     = ControlText('First name','Default value')
        #self._middlename    = ControlText('Middle name')
        #self._lastname      = ControlText('Last name')
        self._outputtext    = ControlText('Output')
        self._quittext      = ControlText('See you next time')
        self._button        = ControlButton('Press this button')
        self._viewbutton    = ControlButton('View')
        self._addbutton     = ControlButton('Add')
        self._deletebutton  = ControlButton('Delete')
        self._quitbutton    = ControlButton('Quit')

        #Layout of the buttons
        self.formset = ['_outputtext','_viewbutton','_addbutton','_deletebutton','_quitbutton', ' ' ]
        

        #Define the button action
        self._quitbutton.value = self._quitprogram

        #self.formset = [('_firstname','_middlename','_lastname'), '_button', '_fullname', ' ' ]

        #tabs gui
##        self.formset = [ {
##            'Tab1':['_firstname','||', '_middlename','||','_lastname'],
##            'Tab2':['_fullname']}, '=',(' ', '_button', ' ') ]
##
    def _quitprogram(self):
        self.popup('See you next time')
        #conn.close()   #close the db connection
        sys.exit() # quit program

#Execute the application
if __name__ == "__main__":    pyforms.start_app(SimpleExample1, geometry=(200, 200, 400, 400))
