# Generated by Django 4.2.7 on 2023-12-04 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_article_image_alter_articleseries_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='series',
            new_name='dept',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='subtitle',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_slug',
            new_name='name_slug',
        ),
        migrations.RenameField(
            model_name='articleseries',
            old_name='subtitle',
            new_name='abbr',
        ),
        migrations.RenameField(
            model_name='articleseries',
            old_name='title',
            new_name='dept_name',
        ),
    ]
