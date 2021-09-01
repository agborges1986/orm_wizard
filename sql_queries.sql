SELECT * FROM db_wizard.wizard;
/* Wizard.objects.create(name="Luna Lovegood", house="Ravenclaw", pet="None", year="4")*/
INSERT INTO db_wizard.wizard (name, house, pet, year) VALUES ('Luna Lovegood', 'Ravenclaw', 'None', '4');
/*ORM Django
Wizard.objects.create(name="Padma Patil", house="Ravenclaw", pet="None", year="5")
*/
INSERT INTO db_wizard.wizard (name, house, pet, year) VALUES ('Padma Patil', 'Ravenclaw', 'None', '5');
/* ORM Django
ravenclaws = Wizard.objects.filter(house="Ravenclaw")
*/
SELECT * FROM db_wizard.wizard WHERE house = 'Ravenclaw';
/*ORM Django
luna = Wizard.objects.get(name="Luna Lovegood")
luna.year = 5
luna.save()
*/
UPDATE db_wizard.wizard SET year = '5' WHERE name = 'Luna Lovegood';