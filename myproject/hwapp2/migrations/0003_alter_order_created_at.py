import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwapp2', '0002_alter_client_address_alter_client_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 9, 50, 13, 397046)),
        ),
    ]
