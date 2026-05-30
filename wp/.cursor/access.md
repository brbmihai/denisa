# Local access — Denisa Dragomir WordPress

## Paths

| Item | Path |
|------|------|
| Project root (WordPress root) | `/media/mihai/data/www/denisadragomir/wp` |
| WP-CLI | `./wp` (wrapper → `wp-cli.phar`) |

## URLs (local dev)

| Purpose | URL |
|---------|-----|
| Front | http://wp.denisadragomir.ro/ |
| Admin | http://wp.denisadragomir.ro/wp-admin/ |

Configured in `wp-config.php` via `WP_HOME` and `WP_SITEURL`.

## Database (MariaDB/MySQL)

| Setting | Value |
|---------|--------|
| Database name | `denisa_wp` |
| Username | `admin` |
| Host | `localhost` |
| Password | Set in `wp-config.php` — `DB_PASSWORD` |
| Table prefix | `wp_` |

## WordPress admin (installed via WP-CLI)

| Field | Value |
|-------|--------|
| Username | `wpadmin` |
| Admin email | `admin@wp.denisadragomir.ro` |

Password was generated at install time; if lost, reset from the project root:

```bash
cd /media/mihai/data/www/denisadragomir/wp
./wp user update wpadmin --user_pass='NEW_PASSWORD_HERE'
```

## WP-CLI quick reference

```bash
cd /media/mihai/data/www/denisadragomir/wp
./wp db check
./wp plugin list
./wp theme list
```
