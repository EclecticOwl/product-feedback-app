# Generated by Django 4.0.6 on 2022-07-06 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_feedback_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='product_name',
            new_name='product_id',
        ),
    ]
