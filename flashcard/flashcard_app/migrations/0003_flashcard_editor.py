# Generated by Django 4.1.4 on 2023-01-08 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("flashcard_app", "0002_alter_flashcard_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="flashcard",
            name="editor",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
