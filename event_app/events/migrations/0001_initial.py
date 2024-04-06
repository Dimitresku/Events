# Generated by Django 5.0.3 on 2024-04-06 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('registration_status', models.CharField(choices=[('not_started', 'Регистрация еще не началась'), ('open', 'Идет регистрация'), ('closed', 'Регистрация закрыта')], max_length=20, verbose_name='Статус регистрации')),
                ('organizer_name', models.CharField(max_length=100, verbose_name='Название организатора')),
                ('organizer_contacts', models.CharField(max_length=100, verbose_name='Контакты организатора')),
                ('description', models.TextField(verbose_name='Описание мероприятия')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время начала проведения мероприятия')),
                ('format', models.CharField(choices=[('online', 'Онлайн'), ('offline', 'Офлайн')], max_length=20, verbose_name='Формат мероприятия')),
                ('participant_limit', models.PositiveIntegerField(verbose_name='Лимит участников')),
                ('location_address', models.CharField(max_length=200, verbose_name='Адрес места проведения мероприятия')),
                ('location_coordinates', models.CharField(max_length=100, verbose_name='Координаты места проведения мероприятия')),
                ('image', models.ImageField(upload_to='events/image/', verbose_name='Обложка мероприятия')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('host_photo', models.ImageField(upload_to='events/hosts/image/', verbose_name='Фото ведущего')),
                ('host_full_name', models.CharField(max_length=100, verbose_name='ФИО ведущего')),
                ('host_contacts', models.CharField(max_length=100, verbose_name='Контакты ведущего')),
                ('host_company', models.CharField(max_length=100, verbose_name='Компания ведущего')),
                ('host_position', models.CharField(max_length=100, verbose_name='Должность ведущего')),
                ('event_link', models.URLField(verbose_name='Ссылка на мероприятие')),
                ('recording_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на запись мероприятия')),
                ('recording_link_start_date', models.DateTimeField(blank=True, null=True, verbose_name='Начало срока ссылки записи')),
                ('recording_link_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Конец срока ссылки записи')),
                ('online_stream_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на онлайн-трансляцию мероприятия')),
                ('online_stream_link_start_date', models.DateTimeField(blank=True, null=True, verbose_name='Начало срока ссылки трансляции')),
                ('online_stream_link_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Конец срока ссылки трансляции')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Участники мероприятия')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Subevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название программы')),
                ('time', models.TimeField(verbose_name='Время начала проведения программы')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subevents', to='events.event', verbose_name='Мероприятие, в котором программа')),
            ],
        ),
    ]
