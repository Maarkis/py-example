## Migrations

### Create new migration script

Create a new migration with the following command:

```shell
alembic revision -m "some description"
```

Here's a basic outline of what you need to do:

1. **Upgrade Function**: This function contains directives to apply changes to the database schema to bring it to the state described in this migration script.
2. **Downgrade Function**: This function contains directives to revert the changes made in the upgrade function, effectively rolling back the database schema to its previous state.
3. **Down_revision Identifier**: This identifier ensures that Alembic applies migrations in the correct order. When creating a new revision, the down_revision identifier in the new file should point to the previous revision's identifier.

⚠️ NOTE : A new migration (i.e. `<revision>_some_description.py`) will be created in the [migrations folder](../../app/infrastructure/db/migrations/versions/).

### Run migrations

This command executes all pending migrations to update the database to the latest version defined in the migration head.

```shell
alembic upgrade head
```

### Downgrade migrations (Rollback)

This command reverses all applied migrations, taking the database back to its initial state.

```shell
alembic downgrade base
```

### Relative migrations (Upgrade/Downgrade)

This command applies migrations in the order defined in the migration head, moving the database schema forward by one revision.

```shell
alembic upgrade +1
```

This command reverts migrations in the order defined in the migration head, moving the database schema backward by one revision.

```shell
alembic downgrade +1
```
