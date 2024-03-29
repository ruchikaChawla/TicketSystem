# Generated by Django 2.2.5 on 2019-10-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='issue_type',
            field=models.CharField(choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('Service', 'Service')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone_no',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=4),
        ),
    ]
