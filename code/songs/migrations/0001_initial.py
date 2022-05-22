# Generated by Django 4.0.3 on 2022-05-22 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=256)),
                ('time', models.TextField(max_length=50)),
                ('linkSave', models.TextField()),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]