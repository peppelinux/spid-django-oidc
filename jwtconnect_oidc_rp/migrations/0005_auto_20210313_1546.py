# Generated by Django 3.1.1 on 2021-03-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwtconnect_oidc_rp', '0004_oidcauthenticationrequest_issuer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='oidcauthenticationrequest',
            name='authz_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='oidcauthenticationrequest',
            name='endpoint',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='oidcauthenticationrequest',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
    ]
