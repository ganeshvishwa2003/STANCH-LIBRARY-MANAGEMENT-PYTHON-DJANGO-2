# Generated by Django 5.0.3 on 2024-03-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_category_alter_studentextra_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Title',
            field=models.CharField(default='Untitled', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='bookID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn13',
            field=models.PositiveIntegerField(default='Untitled'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='Untitled', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='num_page',
            field=models.PositiveIntegerField(default='Untitled'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='Untitled', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='ratings',
            field=models.PositiveIntegerField(default='Untitled'),
            preserve_default=False,
        ),
    ]
