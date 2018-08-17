# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-17 17:23
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_grants', to='auth.Group')),
                ('parameter_values', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='The formal slug for this role, which should be unique', max_length=256, unique=True)),
                ('parameters_definition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), default=list, help_text='A set of strings which are the parameters for this role. Entered as a JSON list.', size=None)),
                ('scope', models.CharField(help_text='The permission scope', max_length=256)),
                ('description', models.TextField(blank=True, help_text='Description for this role')),
            ],
        ),
        migrations.CreateModel(
            name='UserGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_values', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_user_grants', to='user_roles.Permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_grants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='groupgrant',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_group_grants', to='user_roles.Permission'),
        ),
        migrations.AlterUniqueTogether(
            name='usergrant',
            unique_together=set([('user', 'permission', 'parameter_values')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupgrant',
            unique_together=set([('group', 'permission', 'parameter_values')]),
        ),
    ]
