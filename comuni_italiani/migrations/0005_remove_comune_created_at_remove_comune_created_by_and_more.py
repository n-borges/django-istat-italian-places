# Generated by Django 4.2.7 on 2023-11-02 15:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comuni_italiani", "0004_comune_geographic_partition"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comune",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="comune",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="comune",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="comune",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="provincia",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="provincia",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="provincia",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="provincia",
            name="updated_by",
        ),
        migrations.RemoveField(
            model_name="regione",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="regione",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="regione",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="regione",
            name="updated_by",
        ),
    ]
