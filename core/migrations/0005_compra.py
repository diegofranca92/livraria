# Generated by Django 4.2.3 on 2023-07-18 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_livro_autores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizada'), (3, 'Paga'), (4, 'Entregue')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
