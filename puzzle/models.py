from email import message
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_odd(value):
    if value % 2 == 0:
        raise ValidationError(
            _('Please provide an odd number of Horizontal rows.'),
            params={'value': value},
        )

# Create your models here.
class Hex(models.Model):
    horizontal_rows = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20),validate_odd])
    vertical_rows = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])

class Square(models.Model):
    horizontal_rows = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])
    vertical_rows = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])


class Horizontal1(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal2(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal3(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal4(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal5(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal6(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal7(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )
class Horizontal8(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal9(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )

class Horizontal10(models.Model):
    a = models.TextField(
        max_length=1,
        validators=[RegexValidator(r'^1')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="A",
        help_text="1",
    )

    b = models.TextField(
        max_length=2,
        validators=[RegexValidator(r'^2')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="B",
        help_text="2",
    )

    c = models.TextField(
        max_length=3,
        validators=[RegexValidator(r'^3')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="C",
        help_text="3",
    )

    d = models.TextField(
        max_length=4,
        validators=[RegexValidator(r'^4')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="D",
        help_text="4",
    )

    e = models.TextField(
        max_length=5,
        validators=[RegexValidator(r'^5')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="E",
        help_text="5",
    )

    f = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^6')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="F",
        help_text="6",
    )

    g = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^7')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="G",
        help_text="7",
    )
    H = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^8')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="8",
        help_text="8",
    )
    i = models.TextField(
        max_length=9,
        validators=[RegexValidator(r'^9')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="I",
        help_text="9",
    )
    J = models.TextField(
        max_length=6,
        validators=[RegexValidator(r'^10')],
        unique=True,
        null=False,
        blank=False,
        verbose_name="10",
        help_text="10",
    )