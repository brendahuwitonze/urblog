# Generated by Django 2.2.6 on 2019-10-05 21:23

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30, unique=True)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('picture', models.ImageField(default='', null=True, upload_to='article_images')),
                ('author', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=800, unique=True)),
                ('description', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carticle.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carticle.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', max_length=160)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carticle.Article')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='carticle.Comment')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carticle.College'),
        ),
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='article_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
