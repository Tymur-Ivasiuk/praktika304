# Generated by Django 4.1.3 on 2022-12-02 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fonds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fonds',
            options={'verbose_name': 'Фонд', 'verbose_name_plural': 'Фонди'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ['my_order'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterModelOptions(
            name='quotes',
            options={'verbose_name': 'Цитата', 'verbose_name_plural': 'Цитати'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Розділ', 'verbose_name_plural': 'Розділи'},
        ),
        migrations.AddField(
            model_name='photos',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fonds',
            name='desc',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='fonds',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубліковано'),
        ),
        migrations.AlterField(
            model_name='fonds',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fonds.section', verbose_name='Розділ'),
        ),
        migrations.AlterField(
            model_name='fonds',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Назва фонду'),
        ),
        migrations.AlterField(
            model_name='fonds',
            name='url_global',
            field=models.CharField(max_length=1000, unique=True, verbose_name='URL-посилання'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='author',
            field=models.CharField(max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='desc',
            field=models.TextField(verbose_name='Цитата'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Назва'),
        ),
    ]