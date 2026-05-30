<?php
/**
 * WooCommerce symbols referenced by the theme for IDE/static analysis when the plugin is not in the workspace.
 * Do not require this file from the theme — it is only for tooling. At runtime WooCommerce provides these.
 *
 * @package solace
 */

// phpcs:disable Squiz.Commenting.FunctionComment.Missing

if ( ! function_exists( 'is_shop' ) ) {
	/**
	 * @return bool
	 */
	function is_shop() {
		return false;
	}
}

if ( ! function_exists( 'is_cart' ) ) {
	/**
	 * @return bool
	 */
	function is_cart() {
		return false;
	}
}

if ( ! function_exists( 'is_checkout' ) ) {
	/**
	 * @return bool
	 */
	function is_checkout() {
		return false;
	}
}

if ( ! function_exists( 'is_account_page' ) ) {
	/**
	 * @return bool
	 */
	function is_account_page() {
		return false;
	}
}

if ( ! function_exists( 'is_woocommerce' ) ) {
	/**
	 * @return bool
	 */
	function is_woocommerce() {
		return false;
	}
}

if ( ! function_exists( 'wc_get_page_id' ) ) {
	/**
	 * @param string $page Page slug.
	 * @return int
	 */
	function wc_get_page_id( $page ) {
		return 0;
	}
}

if ( ! function_exists( 'woocommerce_breadcrumb' ) ) {
	/**
	 * @param array<string, mixed>|null $args Breadcrumb args.
	 */
	function woocommerce_breadcrumb( $args = null ) {
	}
}
