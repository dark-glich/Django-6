# Generated by Django 3.1.7 on 2021-03-25 07:43

from django.db import migrations
import main.textfield


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_civics_economics_geography_history_science'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maths',
            name='answer',
            field=main.textfield.NonStrippingTextField(),
        ),
    ]