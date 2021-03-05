# Generated by Django 3.1.7 on 2021-03-03 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0010_turno_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='turno',
            field=models.CharField(max_length=200, unique=True, verbose_name=(models.DateField(), models.CharField(choices=[('5PM - 6PM', '5PM - 6PM'), ('6PM - 7PM', '6PM - 7PM'), ('7PM - 8PM', '7PM - 8PM'), ('8PM - 9PM', '8PM - 9PM'), ('9PM - 10PM', '9PM - 10PM'), ('10PM - 11PM', '10PM - 11PM'), ('11PM - 00AM', '11PM - 00AM')], max_length=20))),
        ),
    ]
