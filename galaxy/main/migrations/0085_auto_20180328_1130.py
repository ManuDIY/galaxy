from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('main', '0084_content_block_update')]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='role_type',
            field=models.CharField(
                choices=[
                    ('ANS', 'Ansible'),
                    ('CON', 'Container Enabled'),
                    ('APP', 'Container App'),
                    ('DEM', 'Demo'),
                ],
                default=None,
                editable=False,
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(
                choices=[
                    ('role', 'Role'),
                    ('module', 'Module'),
                    ('apb', 'Ansible Playbook Bundle'),
                    ('action_plugin', 'Action Plugin'),
                    ('cache_plugin', 'Cache Plugin'),
                    ('callback_plugin', 'Callback Plugin'),
                    ('cliconf_plugin', 'CLI Conf Plugin'),
                    ('connection_plugin', 'Connection Plugin'),
                    ('filter_plugin', 'Filter Plugin'),
                    ('inventory_plugin', 'Inventory Plugin'),
                    ('lookup_plugin', 'Lookup Plugin'),
                    ('netconf_plugin', 'Netconf Plugin'),
                    ('shell_plugin', 'Shell Plugin'),
                    ('strategy_plugin', 'Strategy Plugin'),
                    ('terminal_plugin', 'Terminal Plugin'),
                    ('test_plugin', 'Test Plugin'),
                ],
                db_index=True,
                max_length=512,
                unique=True,
            ),
        ),
    ]
