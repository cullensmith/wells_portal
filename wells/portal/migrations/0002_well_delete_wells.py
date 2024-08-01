# Generated by Django 4.2.13 on 2024-08-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_num', models.CharField(blank=True, max_length=50, null=True)),
                ('other_id', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('stusps', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('municipality', models.CharField(blank=True, max_length=50, null=True)),
                ('well_name', models.CharField(blank=True, max_length=50, null=True)),
                ('operator', models.CharField(blank=True, max_length=50, null=True)),
                ('spud_date', models.CharField(blank=True, max_length=50, null=True)),
                ('plug_date', models.CharField(blank=True, max_length=50, null=True)),
                ('well_type', models.CharField(blank=True, max_length=50, null=True)),
                ('well_status', models.CharField(blank=True, max_length=50, null=True)),
                ('well_configuration', models.CharField(blank=True, max_length=50, null=True)),
                ('ft_category', models.CharField(blank=True, max_length=50, null=True)),
                ('wellwiki', models.CharField(blank=True, max_length=50, null=True)),
                ('ftuid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wells_240701',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Wells',
        ),
    ]