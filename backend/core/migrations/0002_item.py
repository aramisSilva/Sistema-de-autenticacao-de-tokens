# Generated by Django 4.0.4 on 2022-04-28 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.list')),
            ],
        ),
    ]
