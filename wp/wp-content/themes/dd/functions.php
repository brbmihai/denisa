<?php
/**
 * dd — Astra child theme.
 *
 * @package dd
 */

defined( 'ABSPATH' ) || exit;

/**
 * Enqueue child stylesheet after Astra’s main CSS.
 */
add_action( 'wp_enqueue_scripts', 'dd_enqueue_styles', 15 );

/**
 * Load child theme style.css.
 */
function dd_enqueue_styles() {
	wp_enqueue_style(
		'dd-child-style',
		get_stylesheet_directory_uri() . '/style.css',
		array( 'astra-theme-css' ),
		wp_get_theme()->get( 'Version' )
	);
}
