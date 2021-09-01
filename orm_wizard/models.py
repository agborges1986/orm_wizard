from django.db import models

# Create your models here.
class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'wizard'


if __name__ =="__main__":

    from orm_wizard.models import *
    # SQL-> INSERT INTO Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');
    Wizard.objects.create(name="Harry Potter", house='Gryffindor', pet='Hedwig', year='5')
    # SQL-> INSERT INTO Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');
    Wizard.objects.create(name="Hermione Granger", house='Gryffindor', pet='Crookshanks', year='5')
    # SQL-> SELECT * FROM Wizard WHERE id = 1;
    Wizard.objects.filter(id="1")
    # SQL-> SELECT * FROM Wizard WHERE house = 'Gryffindor';
    Wizard.objects.filter(house="Gryffindor")
    # SQL-> UPDATE Wizard SET year = '6' WHERE id = 1;
    a=Wizard.objects.get(id="1")
    a.year="6"
    a.save()