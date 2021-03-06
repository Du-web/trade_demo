# Generated by Django 2.0.6 on 2020-12-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_num', models.CharField(blank=True, max_length=50, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'accout_db',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_amount', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('trade_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, '交易中'), (1, '交易成功'), (2, '交易失败')], default=0, null=True)),
                ('accout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.Accout')),
            ],
            options={
                'db_table': 'trade_db',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'user_db',
            },
        ),
        migrations.AddField(
            model_name='trade',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
        migrations.AddField(
            model_name='accout',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.User'),
        ),
    ]
