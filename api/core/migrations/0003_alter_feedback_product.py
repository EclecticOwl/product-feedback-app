# Generated by Django 4.0.6 on 2022-07-08 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_product_name_feedback_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='core.product'),
        ),
    ]