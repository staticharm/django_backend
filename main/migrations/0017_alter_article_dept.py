# Generated by Django 4.2.7 on 2023-12-04 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_article_options_alter_articleseries_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dept',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.articleseries', verbose_name='dept'),
        ),
    ]
