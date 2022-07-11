# Generated by Django 3.2.13 on 2022-07-11 12:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0012_alter_bodyrole_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyrole',
            name='permissions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AddE', 'Add Event'), ('UpdE', 'Update Event'), ('DelE', 'Delete Event'), ('UpdB', 'Update Body'), ('Role', 'Modify Roles'), ('VerA', 'Verify Achievements'), ('ModP', 'Moderate Post'), ('ModC', 'Moderate Comment'), ('DelP', 'Delete Post'), ('DelC', 'Delete Comment')], max_length=49),
        ),
    ]