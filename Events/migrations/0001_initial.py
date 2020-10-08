# Generated by Django 3.1.1 on 2020-09-25 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_comments_xtd', '0006_auto_20181204_0948'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('slug', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('xtdcomment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_comments_xtd.xtdcomment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ('submit_date',),
                'permissions': [('can_moderate', 'Can moderate comments')],
                'abstract': False,
            },
            bases=('django_comments_xtd.xtdcomment',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', tinymce.models.HTMLField(verbose_name='Description')),
                ('event_img', models.ImageField(default='default.jpg', upload_to='event_pics')),
                ('event_date', models.DateTimeField()),
                ('event_location', mapbox_location_field.models.LocationField(map_attrs={})),
                ('slug', models.SlugField(blank=True)),
                ('open_slot', models.IntegerField(default=5, null=True)),
                ('attend', models.ManyToManyField(blank=True, default=None, related_name='attendees', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='category', to='Events.category', verbose_name='Categories')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]