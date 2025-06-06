# Generated by Django 4.1.13 on 2025-05-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('years', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('database', 'Database'), ('devops', 'DevOps'), ('ds', 'Data Science')], max_length=20)),
                ('level', models.CharField(max_length=100)),
                ('years_exp', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='github_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='live_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='portfolio.technology'),
        ),
    ]
