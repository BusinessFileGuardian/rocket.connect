# Generated by Django 3.2.13 on 2022-05-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0010_connector_secondary_connectors'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='external_url',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='connector',
            name='managers',
            field=models.CharField(blank=True, help_text='separate users or channels with comma, eg: user1,user2,user3,#channel1,#channel2', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='admin_user_id',
            field=models.CharField(blank=True, help_text='Admin User Personal Access Token', max_length=50),
        ),
        migrations.AlterField(
            model_name='server',
            name='bot_user_id',
            field=models.CharField(blank=True, help_text='Bot User Personal Access Token', max_length=50),
        ),
        migrations.AlterField(
            model_name='server',
            name='managers',
            field=models.CharField(help_text='separate users or channels with comma, eg: user1,user2,user3,#channel1,#channel2', max_length=50),
        ),
        migrations.AlterField(
            model_name='server',
            name='secret_token',
            field=models.CharField(blank=True, help_text='same secret_token used at Rocket.Chat Omnichannel Webhook Config', max_length=50, null=True),
        ),
    ]
