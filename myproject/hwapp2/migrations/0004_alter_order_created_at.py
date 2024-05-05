import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwapp2', '0003_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 9, 53, 36, 224946, tzinfo=datetime.timezone.utc)),
        ),
    ]
