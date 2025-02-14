# Generated by Django 3.0 on 2019-12-10 16:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'AppliedMetadata',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('description', models.CharField(max_length=256)),
                ('path', models.CharField(max_length=256)),
                ('obj_name', models.CharField(max_length=32)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Engine',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sha256', models.CharField(max_length=64)),
                ('opcodes', models.BinaryField()),
                ('architecture', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Function',
            },
        ),
        migrations.CreateModel(
            name='FunctionApis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'FunctionApis',
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Metadata',
            },
        ),
        migrations.CreateModel(
            name='MetadataDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('prototype', models.CharField(max_length=256)),
                ('comment', models.CharField(max_length=512)),
                ('committed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'MetadataDetails',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('md5', models.CharField(max_length=32)),
                ('crc32', models.BigIntegerField()),
                ('sha1', models.CharField(blank=True, max_length=40, null=True)),
                ('sha256', models.CharField(blank=True, max_length=64, null=True)),
                ('last_seen', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Sample',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=254)),
                ('handle', models.CharField(max_length=32)),
                ('number', models.IntegerField()),
                ('api_key', models.UUIDField(unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('rank', models.BigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('service', models.CharField(max_length=16)),
                ('auth_data', models.TextField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['email'], name='User_email_ffa2e0_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['api_key'], name='User_api_key_c4f2d6_idx'),
        ),
        migrations.AlterIndexTogether(
            name='user',
            index_together={('handle', 'number')},
        ),
        migrations.AddField(
            model_name='sample',
            name='functions',
            field=models.ManyToManyField(to='www.Function'),
        ),
        migrations.AddField(
            model_name='sample',
            name='seen_by',
            field=models.ManyToManyField(to='www.User'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='details',
            field=models.ManyToManyField(to='www.MetadataDetails'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.User'),
        ),
        migrations.AddField(
            model_name='function',
            name='apis',
            field=models.ManyToManyField(to='www.FunctionApis'),
        ),
        migrations.AddField(
            model_name='function',
            name='metadata',
            field=models.ManyToManyField(to='www.Metadata'),
        ),
        migrations.AddField(
            model_name='engine',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.User'),
        ),
        migrations.AddField(
            model_name='appliedmetadata',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Metadata'),
        ),
        migrations.AddField(
            model_name='appliedmetadata',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Sample'),
        ),
        migrations.AddField(
            model_name='appliedmetadata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.User'),
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together={('md5', 'crc32')},
        ),
        migrations.AlterIndexTogether(
            name='sample',
            index_together={('md5', 'crc32')},
        ),
        migrations.AddIndex(
            model_name='metadata',
            index=models.Index(fields=['user'], name='Metadata_user_id_aea908_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='function',
            unique_together={('sha256', 'architecture')},
        ),
        migrations.AddIndex(
            model_name='engine',
            index=models.Index(fields=['name'], name='Engine_name_14ac74_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='appliedmetadata',
            unique_together={('metadata', 'sample', 'user')},
        ),
    ]
