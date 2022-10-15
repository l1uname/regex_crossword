from django import forms
from .models import Hex, Square, Horizontal1, Horizontal2, Horizontal3, Horizontal4, Horizontal5, Horizontal6, Horizontal7, Horizontal8, Horizontal9, Horizontal10
from django.forms import ModelForm


PUZZLE_CHOICES =[
    ("1", "Square"),
    ("2", "Hex"),
]
 
class SubmitForm(forms.Form):
    first_choice = forms.ChoiceField(label="Select board type:",choices = PUZZLE_CHOICES)

class HexForm(ModelForm):
    class Meta:
        model = Hex
        fields='__all__'

class SquareForm(ModelForm):
    class Meta:
        model = Square
        fields='__all__'


class Vertical1(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical2(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical3(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical4(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical5(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical6(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical7(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical8(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical9(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'
class Vertical10(ModelForm):
    class Meta:
        model = Horizontal1
        fields='__all__'
        model = Horizontal2
        fields='__all__'
        model = Horizontal3
        fields='__all__'
        model = Horizontal4
        fields='__all__'
        model = Horizontal5
        fields='__all__'
        model = Horizontal6
        fields='__all__'
        model = Horizontal7
        fields='__all__'
        model = Horizontal8
        fields='__all__'
        model = Horizontal9
        fields='__all__'
        model = Horizontal10
        fields='__all__'

