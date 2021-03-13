# Generated by Django 3.1.1 on 2021-03-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwtconnect_oidc_rp', '0006_auto_20210313_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='oidcauthenticationrequest',
            name='jwks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='oidcauthenticationrequest',
            name='provider_configuration',
            field=models.TextField(blank=True, null=True),
        ),
    ]
