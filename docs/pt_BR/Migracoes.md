## Migrações

### Criar novo script de migração

Crie uma nova migração com o seguinte comando:

```shell
alembic revision -m "alguma descrição"
```

Aqui está um esboço básico do que você precisa fazer:

1. **Função de Atualização (Upgrade Function)**: Esta função contém diretivas para aplicar alterações no esquema do banco de dados para levá-lo ao estado descrito neste script de migração.
2. **Função de Reversão (Downgrade Function)**: Esta função contém diretivas para reverter as alterações feitas na função de atualização, efetivamente retornando o esquema do banco de dados ao seu estado anterior.
3. **Identificador Down_revision**: Este identificador garante que o Alembic aplique as migrações na ordem correta. Ao criar uma nova revisão, o identificador down_revision no novo arquivo deve apontar para o identificador da revisão anterior.

⚠️ NOTA: Uma nova migração (ou seja, `<revision>_alguma_descrição.py`) será criada na [pasta de migrações](../../app/infrastructure/db/migrations/versions/).

### Executar migrações

Este comando executa todas as migrações pendentes para atualizar o banco de dados para a versão mais recente definida no estado atual de migração.

```shell
alembic upgrade head
```

### Reverter migrações (Rollback)

Este comando reverte todas as migrações aplicadas, retornando o banco de dados ao seu estado inicial.

```shell
alembic downgrade base
```

### Migrações relativas (Atualização/Reversão)

Este comando aplica migrações na ordem definida no estado atual de migração, movendo o esquema do banco de dados para frente em uma revisão.

```shell
alembic upgrade +1
```

Este comando reverte migrações na ordem definida no estado atual de migração, movendo o esquema do banco de dados para trás em uma revisão.

```shell
alembic downgrade +1
```
