# Generated by Django 4.2.3 on 2023-08-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_title_articles_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(max_length=100, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(max_length=300, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
