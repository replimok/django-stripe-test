# Generated by Django 4.1.1 on 2022-09-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='order',
            new_name='orders',
        ),
    ]
