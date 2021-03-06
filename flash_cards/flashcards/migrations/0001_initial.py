# Generated by Django 3.1.7 on 2021-05-03 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_side', models.CharField(max_length=500)),
                ('back_side', models.CharField(max_length=1000)),
                ('collection', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flashcards.collection')),
            ],
        ),
    ]
