# Generated by Django 3.2 on 2023-05-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('ingredients', '0002_auto_20230521_1435'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cooking_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='ingredients.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(default='Default Value'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_images'),
        ),
    ]
