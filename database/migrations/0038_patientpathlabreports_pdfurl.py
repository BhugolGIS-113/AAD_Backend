# Generated by Django 4.2.5 on 2023-11-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0037_familymembers_cbacrequired'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientpathlabreports',
            name='pdfUrl',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
