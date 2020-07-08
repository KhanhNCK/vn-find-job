# Generated by Django 2.2.2 on 2020-07-02 18:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(default=None, max_length=200, null=True)),
                ('images_user', models.TextField(default=None, null=True)),
                ('gender', models.IntegerField(default=0)),
                ('birth_day', models.DateField(null=True)),
                ('dia_chi_tinh_thanh_pho', models.CharField(default=None, max_length=200, null=True)),
                ('dia_chi_quan_huyen', models.CharField(default=None, max_length=200, null=True)),
                ('dia_chi_chi_tiet', models.CharField(default=None, max_length=200, null=True)),
                ('loai_user', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'token',
            },
        ),
        migrations.CreateModel(
            name='ResetToken',
            fields=[
                ('reset_token', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Reset token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reset_token', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'db_table': 'reset_token',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('num_date', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lịch sử đăng nhập login ',
                'verbose_name_plural': 'Lịch sử đăng nhập login ',
            },
        ),
        migrations.CreateModel(
            name='ConfirmEmailToken',
            fields=[
                ('token', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirm_email_token', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'db_table': 'confirm_email_token',
            },
        ),
    ]
