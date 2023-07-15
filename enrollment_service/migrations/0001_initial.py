# Generated by Django 4.1 on 2023-07-15 14:09

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_service', '0001_initial'),
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_course', to='course_service.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student', to='user_service.studentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('checkout_id', models.CharField(max_length=500)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='enrollment_service.enrollment')),
            ],
        ),
    ]
