from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    website = models.URLField(null=True)

    def __str__(self) -> str:
        return self.name

class ColourManager(models.Manager):
    def create(self, name, manufacturer, symbol=None):
        colour, _ = Colour.objects.get_or_create(name=name, manufacturer=manufacturer, symbol=symbol)
        return colour

class Colour(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=40, blank=True, null=True)
    objects = ColourManager()

    class Meta:
        unique_together = ["manufacturer", "name"]

    def __str__(self) -> str:
        return f"{self.name}, {self.manufacturer}"

class Fibre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ComponentManager(models.Manager):
    def create(self, fibre, percent):
        component, _ = Component.objects.get_or_create(fibre=fibre, percent=percent)
        return component

class Component(models.Model):
    fibre = models.ForeignKey(Fibre, on_delete=models.CASCADE)
    percent = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    objects = ComponentManager()
    
    def __str__(self) -> str:
        return f"{self.percent} {self.fibre.name}"

class Skein(models.Model):

    class CoulourType(models.IntegerChoices):
        UNI = 0
        DEGRADE = 1
        LONG = 2
        SHORT = 3

    class Form(models.IntegerChoices):
        BALL = 0
        ROLL = 1
        PRECEL = 2

    class Prepared(models.IntegerChoices):
        READY = 1
        OWN_CHOICE = 2
        ON_DEMAND = 3
        LIMITED = 4

    class Status(models.IntegerChoices):
        OWNED = 0
        BOUGHT = 1
        WANTED = 3

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    form = models.IntegerField(choices=Form.choices)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    composition = models.ManyToManyField(Component) # TODO sum validator
    threads_number = models.IntegerField(null=True)
    special_thread = models.CharField(max_length=20, blank=True, null=True)
    length = models.IntegerField()
    weight = models.IntegerField()
    colours = models.ManyToManyField(Colour)
    manufacturer_symbol = models.CharField(max_length=50, blank=True, null=True)
    prepared = models.IntegerField(choices=Prepared.choices)
    status = models.IntegerField(choices=Status.choices)
    web_link = models.URLField(null=True, blank=True)
    # picture = models.ImageField(null=True)

    def __str__(self) -> str:
        if self.name:
            return self.name
        return super().__str__()


'''
1. ombre
    1) kolory (lista wybierana)
    2) symbol
    3) rodzaj (gotowy / kręcony, własny wybór)
    11) liczba nitek
    12) dodatkowa nić
    4) skład
    5) długość
    6) gramatura
    7) sklep
    8) zdjęcie
    9) projekt
    10) popozycje (lista projektów)
2. uni
    1. kolor
    2. symbol
    3. skład
    4. waga
    5. długość
    6. druty
    7. szydełko


'''
