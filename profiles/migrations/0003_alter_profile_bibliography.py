<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-10-25 19:40
=======
# Generated by Django 4.2.6 on 2023-10-25 19:44
>>>>>>> ddae69216d5203a2310e0e39c99fbf23af76f570

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_bibliography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bibliography',
            field=models.TextField(blank=True, default=None, max_length=500),
        ),
    ]