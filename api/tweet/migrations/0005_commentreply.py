# Generated by Django 3.1.2 on 2020-11-01 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0004_delete_commentreply'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=280, null=True)),
                ('photos', models.ImageField(blank=True, max_length=1000, null=True, upload_to='retweets/images/')),
                ('gif', models.ImageField(blank=True, max_length=5000, null=True, upload_to='retweets/gifs/')),
                ('videos', models.FileField(blank=True, max_length=100000, null=True, upload_to='retweets/videos/')),
                ('topic', models.CharField(blank=True, max_length=140, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.comment')),
                ('replying_to', models.ManyToManyField(related_name='comment_replying_to', to=settings.AUTH_USER_MODEL)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyingto_tweet', to='tweet.tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
