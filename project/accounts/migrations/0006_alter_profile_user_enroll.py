# Generated by Django 5.0.4 on 2024-06-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_alter_profile_user_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_enroll",
            field=models.CharField(
                blank=True,
                choices=[("재학", "재학"), ("휴학", "휴학"), ("졸업", "졸업"), ("교직원", "교직원")],
                max_length=50,
                null=True,
            ),
        ),
    ]
