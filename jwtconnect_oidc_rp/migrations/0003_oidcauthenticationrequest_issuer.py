# Generated by Django 3.1.1 on 2021-03-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwtconnect_oidc_rp', '0002_auto_20210311_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='oidcauthenticationrequest',
            name='issuer',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
