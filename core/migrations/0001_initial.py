# Generated by Django 2.0.7 on 2018-10-16 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoSenha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_password_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParameterForBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nomeProjeto', models.TextField(blank=True, default='', null=True)),
                ('tituloProjeto', models.TextField(blank=True, default='', null=True)),
                ('descricaoProjeto', models.TextField(blank=True, default='', null=True)),
                ('iconeProjeto', models.TextField(blank=True, default='', null=True)),
                ('login_redirect_url', models.CharField(blank=True, default='/core/', max_length=250, null=True)),
                ('login_url', models.CharField(blank=True, default='/core/login/', max_length=250, null=True)),
                ('logout_redirect_url', models.CharField(blank=True, default='/core/login/', max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Parametro para o Core',
                'verbose_name_plural': 'Parametros para o Core',
            },
        ),
        migrations.CreateModel(
            name='ParametersUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('mim_tamanho', models.IntegerField(default=8, help_text='Tamanho mínimo da senha', verbose_name='Quantidade mínima de caracteres')),
                ('max_tamanho', models.IntegerField(default=30, help_text='Tamanho máximo da senha', verbose_name='Quantidade máxima de caracteres')),
                ('dias_expirar', models.IntegerField(default=30, verbose_name='Quantidade de dias para exigir a troca de senha')),
                ('qtde_verificar_similares', models.IntegerField(default=3, verbose_name='Quantidade de senhas similares a serem bloqueadas')),
                ('combinar_numero_caracter', models.BooleanField(default=True, verbose_name='Combinar Letras e Numeros')),
                ('qtde_numero', models.IntegerField(default=4, verbose_name='Quantidade mínima de números')),
                ('qtde_caracter', models.IntegerField(default=2, verbose_name='Quantidade mínima de letras')),
                ('bloquear_usuario', models.IntegerField(default=30, help_text='Qtde de dias para bloquear usuario sem acesso. Use 0 para desabilitar.', verbose_name='Quantidade de dias para bloquear o usuario')),
                ('busca_dados_matricula', models.BooleanField(default=False, help_text='Busca dados do usuario na base de dados de Colaboradores', verbose_name='Buscar dados do usuário pela Matricula')),
                ('bloquear_sequencia_caracter', models.BooleanField(default=True, help_text='Bloqueia sequência de caracteres no campo de senha', verbose_name='Bloquear sequências de caracteres')),
                ('usuario_matricula', models.BooleanField(default=False, verbose_name='Obrigar Matricula no campo Usuario')),
                ('combinar_maiuscula_minuscula', models.BooleanField(default=False, verbose_name='Combinar letras maiúsculas e minúsculas')),
                ('qtde_maiuscula', models.IntegerField(default=0, verbose_name='Quantidade mínima de maiúsculas')),
                ('qtde_minuscula', models.IntegerField(default=0, verbose_name='Quantidade mínima de minúsculas')),
                ('senha_padrao', models.CharField(default='agtec@123456', help_text='Senha padrão que sera criada quando resetar senha do usuario', max_length=125, verbose_name='Senha padrão para reset')),
                ('editar_dados_perfil', models.BooleanField(default=False, help_text='Editar dados do perfil manualmente senão encontrar dados do usuario pelo Matricula', verbose_name='Editar dados do Perfil no cadastro de Usuário ')),
            ],
            options={
                'verbose_name': 'Parâmetro do Usuário',
                'verbose_name_plural': 'Parâmetros dos Usuários',
                'permissions': (('can_reset_password', 'Pode resetar a senha'),),
            },
        ),
        migrations.CreateModel(
            name='UsuarioBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='Matricula')),
                ('servidor', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='servidor')),
                ('cod_setor', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='cod_setor')),
                ('setor', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='setor')),
                ('cod_cargo', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='cod_cargo')),
                ('cargo', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='cargo')),
                ('cod_funcao', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='cod_funcao')),
                ('funcao', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='funcao')),
                ('cod_vinculo', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='cod_vinculo')),
                ('vinculo', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='vinculo')),
                ('secretaria', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Secretaria')),
                ('cod_unidade_gestora', models.CharField(blank=True, db_index=True, max_length=11, null=True, verbose_name='Código da Unidade Gestora')),
                ('data_admissao', models.DateField(blank=True, null=True, verbose_name='data_admissao')),
                ('data_desligamento', models.DateField(blank=True, null=True, verbose_name='data_desligamento')),
                ('localizacao', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='localizacao')),
                ('ativo', models.BooleanField(default=False, verbose_name='ativo ?')),
                ('exonerado', models.BooleanField(default=False, verbose_name='exonerado ?')),
                ('mes_referencia', models.PositiveIntegerField(default=0, verbose_name='Mês Referência')),
                ('ano_referencia', models.PositiveIntegerField(default=0, verbose_name='Ano Referência')),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('prodata', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
