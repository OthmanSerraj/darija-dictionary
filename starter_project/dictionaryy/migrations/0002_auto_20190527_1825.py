# Generated by Django 2.2.1 on 2019-05-27 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionaryy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(choices=[('D', 'Darija'), ('A', 'Arabic'), ('E', 'English')], max_length=1)),
                ('plural', models.CharField(max_length=20)),
                ('root', models.CharField(max_length=10)),
                ('audio', models.FileField(upload_to='audio/')),
            ],
        ),
        migrations.RemoveField(
            model_name='word',
            name='arabic',
        ),
        migrations.RemoveField(
            model_name='word',
            name='author',
        ),
        migrations.RemoveField(
            model_name='word',
            name='darija',
        ),
        migrations.RemoveField(
            model_name='word',
            name='english',
        ),
        migrations.RemoveField(
            model_name='word',
            name='explanation',
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.CharField(max_length=10000)),
                ('picture', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('words', models.ManyToManyField(to='dictionaryy.Word')),
            ],
        ),
    ]