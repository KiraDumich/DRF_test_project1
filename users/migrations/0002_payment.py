# Generated by Django 4.2.1 on 2024-05-27 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payments_date', models.DateTimeField(auto_now=True, verbose_name='дата оплаты')),
                ('payment_sum', models.PositiveIntegerField(verbose_name='сумма платежа')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('card', 'банковский перевод')], default='card', max_length=50, verbose_name='способ оплаты')),
                ('payment_link', models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату')),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='идентификатор платежа')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
                'ordering': ['-payments_date'],
            },
        ),
    ]