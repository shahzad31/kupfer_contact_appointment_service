# Generated by Django 2.2.1 on 2019-05-06 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0012_contact_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
