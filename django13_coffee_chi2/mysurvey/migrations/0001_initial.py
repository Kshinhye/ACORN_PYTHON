# Generated by Django 4.1.2 on 2022-11-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("rnum", models.AutoField(primary_key=True, serialize=False)),
                ("gender", models.CharField(blank=True, max_length=4, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("co_survey", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={"db_table": "survey", "managed": False,},
        ),
    ]
