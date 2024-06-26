# Generated by Django 4.2.3 on 2024-05-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_alter_certificate_certifying_institution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.profile",
            ),
        ),
    ]
