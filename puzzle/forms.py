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
        fields='a'
        model = Horizontal2
        fields='a'
        model = Horizontal3
        fields='a'
        model = Horizontal4
        fields='a'
        model = Horizontal5
        fields='a'
        model = Horizontal6
        fields='a'
        model = Horizontal7
        fields='a'
        model = Horizontal8
        fields='a'
        model = Horizontal9
        fields='a'
        model = Horizontal10
        fields='a'
class Vertical2(ModelForm):
    class Meta:
        model = Horizontal1
        fields='b'
        model = Horizontal2
        fields='b'
        model = Horizontal3
        fields='b'
        model = Horizontal4
        fields='b'
        model = Horizontal5
        fields='b'
        model = Horizontal6
        fields='b'
        model = Horizontal7
        fields='b'
        model = Horizontal8
        fields='b'
        model = Horizontal9
        fields='b'
        model = Horizontal10
        fields='b'
class Vertical3(ModelForm):
    class Meta:
        model = Horizontal1
        fields='c'
        model = Horizontal2
        fields='c'
        model = Horizontal3
        fields='c'
        model = Horizontal4
        fields='c'
        model = Horizontal5
        fields='c'
        model = Horizontal6
        fields='c'
        model = Horizontal7
        fields='c'
        model = Horizontal8
        fields='c'
        model = Horizontal9
        fields='c'
        model = Horizontal10
        fields='c'
class Vertical4(ModelForm):
    class Meta:
        model = Horizontal1
        fields='d'
        model = Horizontal2
        fields='d'
        model = Horizontal3
        fields='d'
        model = Horizontal4
        fields='d'
        model = Horizontal5
        fields='d'
        model = Horizontal6
        fields='d'
        model = Horizontal7
        fields='d'
        model = Horizontal8
        fields='d'
        model = Horizontal9
        fields='d'
        model = Horizontal10
        fields='d'
class Vertical5(ModelForm):
    class Meta:
        model = Horizontal1
        fields='e'
        model = Horizontal2
        fields='e'
        model = Horizontal3
        fields='e'
        model = Horizontal4
        fields='e'
        model = Horizontal5
        fields='e'
        model = Horizontal6
        fields='e'
        model = Horizontal7
        fields='e'
        model = Horizontal8
        fields='e'
        model = Horizontal9
        fields='e'
        model = Horizontal10
        fields='e'
class Vertical6(ModelForm):
    class Meta:
        model = Horizontal1
        fields='f'
        model = Horizontal2
        fields='f'
        model = Horizontal3
        fields='f'
        model = Horizontal4
        fields='f'
        model = Horizontal5
        fields='f'
        model = Horizontal6
        fields='f'
        model = Horizontal7
        fields='f'
        model = Horizontal8
        fields='f'
        model = Horizontal9
        fields='f'
        model = Horizontal10
        fields='f'
class Vertical7(ModelForm):
    class Meta:
        model = Horizontal1
        fields='g'
        model = Horizontal2
        fields='g'
        model = Horizontal3
        fields='g'
        model = Horizontal4
        fields='g'
        model = Horizontal5
        fields='g'
        model = Horizontal6
        fields='g'
        model = Horizontal7
        fields='g'
        model = Horizontal8
        fields='g'
        model = Horizontal9
        fields='g'
        model = Horizontal10
        fields='g'
class Vertical8(ModelForm):
    class Meta:
        model = Horizontal1
        fields='h'
        model = Horizontal2
        fields='h'
        model = Horizontal3
        fields='h'
        model = Horizontal4
        fields='h'
        model = Horizontal5
        fields='h'
        model = Horizontal6
        fields='h'
        model = Horizontal7
        fields='h'
        model = Horizontal8
        fields='h'
        model = Horizontal9
        fields='h'
        model = Horizontal10
        fields='h'
class Vertical9(ModelForm):
    class Meta:
        model = Horizontal1
        fields='i'
        model = Horizontal2
        fields='i'
        model = Horizontal3
        fields='i'
        model = Horizontal4
        fields='i'
        model = Horizontal5
        fields='i'
        model = Horizontal6
        fields='i'
        model = Horizontal7
        fields='i'
        model = Horizontal8
        fields='i'
        model = Horizontal9
        fields='i'
        model = Horizontal10
        fields='i'
class Vertical10(ModelForm):
    class Meta:
        model = Horizontal1
        fields='j'
        model = Horizontal2
        fields='j'
        model = Horizontal3
        fields='j'
        model = Horizontal4
        fields='j'
        model = Horizontal5
        fields='j'
        model = Horizontal6
        fields='j'
        model = Horizontal7
        fields='j'
        model = Horizontal8
        fields='j'
        model = Horizontal9
        fields='j'
        model = Horizontal10
        fields='j'

