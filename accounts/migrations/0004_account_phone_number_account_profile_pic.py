# Generated by Django 4.2.6 on 2024-05-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_remove_account_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="phone_number",
            field=models.CharField(default="77 ...", max_length=50),
        ),
        migrations.AddField(
            model_name="account",
            name="profile_pic",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
