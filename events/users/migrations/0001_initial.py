# Generated by Django 5.0.3 on 2024-04-02 17:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=5, verbose_name='role')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='phone')),
                ('employer', models.CharField(blank=True, max_length=100, null=True, verbose_name='employer')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True, verbose_name='occupation')),
                ('experience', models.CharField(choices=[('no_experience', 'No experience'), ('more_1_year', 'More than 1 year'), ('more_3_years', 'More than 3 years'), ('more_5_years', 'More than 5 years'), ('other_experience', 'Other experience')], default='no_experience', max_length=20, verbose_name='experience')),
                ('preferred_format', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default='online', max_length=10, verbose_name='preferred format')),
                ('consent_personal_data_processing', models.BooleanField(default=False, verbose_name='consent of the personal data processing')),
                ('consent_personal_data_date', models.DateTimeField(blank=True, null=True, verbose_name='date of the personal data consent')),
                ('consent_vacancy_data_processing', models.BooleanField(default=False, verbose_name='consent of the vacancy data processing')),
                ('consent_vacancy_data_date', models.DateTimeField(blank=True, null=True, verbose_name='date of the vacancy data consent')),
                ('consent_random_coffee', models.BooleanField(default=False, verbose_name='consent to participate in random coffee')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.specialization')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
