<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'denisa_wp' );

/** Database username */
define( 'DB_USER', 'admin' );

/** Database password (set the password for MySQL user `admin`) */
define( 'DB_PASSWORD', '1234567890' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          '>x+f/o>+Z Kv/:6B 4GfZmjq3U2=~f.JDyo]>t`z.Wgh.;cinL7qIdvoZunJ09<9' );
define( 'SECURE_AUTH_KEY',   'f3{AbZ0;aauXEVF<_(VDBj@(xn})J.la{7)+J[|f<c #w()6|r+tr6Fl+5X2xb7y' );
define( 'LOGGED_IN_KEY',     'pjbhp<tY?LDwfTj-HT(sBIh)a7@e$YW<K%XT1*nM|q3|C4HTCW$Y`/}NfT}Q-^?~' );
define( 'NONCE_KEY',         'oP1}F/c4`;j:#GZ7F6VZF1P jHH<W29^bk{pBe-q?rK&CQo<?^z#.;p!1p:[+,n9' );
define( 'AUTH_SALT',         'w>gU%+lKX+5TK.+l1uhh~GF#*L/)VsH30}&]i #k>4X{15W;PH#E7{5the0?;kQz' );
define( 'SECURE_AUTH_SALT',  'fNR/00=DMZMJ#r><PCW<_hkS+<c5$~v7KNQ]c=NwIQB,v9HE1<*@xSg Yd~EAl,l' );
define( 'LOGGED_IN_SALT',    '0D B4{3!:.P-=(Mf=Gyp,ki9m[Xht.@;!o>BA^1>h0H~l{k)Q)S?Vqy03^lD5@7[' );
define( 'NONCE_SALT',        '=o+L~i$0LEjz-Uq: 3uV0 $ki6)5in38=D1fLleX}/_OUNB%e`g#,1!jZnEKxT3V' );
define( 'WP_CACHE_KEY_SALT', '3F7*Ep,d/KDWvF(9SKh/[F^,bb#(K3;.6l&M*fA2XpSR_Q9;44o{AW&`yYf,Rkk^' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/** Site URL (must match how visitors reach the site, or assets load on the wrong scheme) */
define( 'WP_HOME', 'https://wp.denisadragomir.ro' );
define( 'WP_SITEURL', 'https://wp.denisadragomir.ro' );

/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

define('WPFC_CLEAR_CACHE_AFTER_THEME_UPDATE', true);
define('WP_MEMORY_LIMIT', '768M');
define('WP_MAX_MEMORY_LIMIT', '768M');

define('WPFC_CLEAR_CACHE_AFTER_PLUGIN_UPDATE', true);
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
